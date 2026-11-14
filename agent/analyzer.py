
import json
import re

from agent.models import AnalysisResult, Finding, ToolResult
from backend.security.finding_rules import SecurityRuleEvaluator


class ADAnalyzer:
    """Analyzes results returned by the registered AD security tools."""

    def analyze(self, result: ToolResult) -> AnalysisResult:
        """Dispatch each tool result to its corresponding analyzer."""

        if result.status.lower() not in ("success", "completed"):
            return AnalysisResult(
                summary=f"Tool '{result.tool}' did not complete successfully: "
                        f"{result.status}. {result.output[:300]}",
                findings=[],
                recommended_next_step="Check tool configuration and execution output.",
            )

        analyzers = {
            "network_discovery": self._analyze_network_discovery,
            "domain_enumeration": self._analyze_domain_enum,
            "ad_user_enumeration": self._analyze_ad_users,
            "check_admin_access": self._analyze_admin_access,
            "smb_anonymous_audit": self._analyze_smb_anonymous,
        }

        analyzer = analyzers.get(result.tool)

        if analyzer is None:
            return AnalysisResult(
                summary=f"Received output from {result.tool}. No specialized analyzer is configured.",
                findings=[],
                recommended_next_step="Review the tool output manually.",
            )

        return analyzer(result)

    def _analyze_network_discovery(self, result: ToolResult) -> AnalysisResult:
        """Identify open Active Directory-related network ports."""

        output = result.output or ""
        port_details = {
            88: ("Kerberos", "Active Directory authentication service detected."),
            389: ("LDAP", "LDAP directory service detected."),
            445: ("SMB", "SMB file-sharing service detected."),
            3268: ("Global Catalog LDAP", "Global Catalog service detected."),
            3269: ("Global Catalog LDAPS", "Secure Global Catalog service detected."),
        }

        findings = []

        for port, (service, description) in port_details.items():
            pattern = rf"\b{port}/tcp\s+open\b"
            if re.search(pattern, output, re.IGNORECASE):
                findings.append(
                    Finding(
                        title=f"Open {service} Port: {port}",
                        severity="INFO",
                        description=description,
                        evidence=f"{port}/tcp open",
                    )
                )

        if findings:
            summary = (
                f"Network discovery identified {len(findings)} open "
                "Active Directory-related service port(s)."
            )
            next_step = "Review the discovered services and proceed with authorized domain enumeration."
        else:
            summary = "No recognized open Active Directory service ports were identified in the scan output."
            next_step = "Review the scan output and verify that the target is reachable."

        return AnalysisResult(
            summary=summary,
            findings=findings,
            recommended_next_step=next_step,
        )

    def _analyze_domain_enum(self, result: ToolResult) -> AnalysisResult:
        """Extract domain and hostname information from SMB enumeration output."""

        output = result.output or ""
        findings = []

        domain_match = re.search(
            r"\(domain:([^)]+)\)",
            output,
            re.IGNORECASE,
        )
        hostname_match = re.search(
            r"\(name:([^)]+)\)",
            output,
            re.IGNORECASE,
        )

        if domain_match:
            domain = domain_match.group(1).strip()
            findings.append(
                Finding(
                    title=f"Active Directory Domain Identified: {domain}",
                    severity="INFO",
                    description=f"The target returned the domain name '{domain}'.",
                    evidence=domain_match.group(0),
                )
            )

        if hostname_match:
            hostname = hostname_match.group(1).strip()
            findings.append(
                Finding(
                    title=f"Domain Controller Hostname: {hostname}",
                    severity="INFO",
                    description=f"The target returned the hostname '{hostname}'.",
                    evidence=hostname_match.group(0),
                )
            )

        if findings:
            summary = "Domain enumeration returned domain or hostname information."
            next_step = "Continue with authorized Active Directory user enumeration."
        else:
            summary = "No domain or hostname information could be extracted from the enumeration output."
            next_step = "Review the SMB enumeration output and check target connectivity."

        return AnalysisResult(
            summary=summary,
            findings=findings,
            recommended_next_step=next_step,
        )

    def _analyze_ad_users(self, result: ToolResult) -> AnalysisResult:
        """Evaluate LDAP user records using the existing security rules."""

        try:
            records = json.loads(result.output or "[]")
        except (json.JSONDecodeError, TypeError):
            return AnalysisResult(
                summary="LDAP user enumeration returned data that could not be parsed as JSON.",
                findings=[],
                recommended_next_step="Review the LDAP tool output and its JSON format.",
            )

        if isinstance(records, dict):
            records = [records]

        if not isinstance(records, list):
            return AnalysisResult(
                summary="LDAP enumeration returned an unexpected data structure.",
                findings=[],
                recommended_next_step="Check the LDAP enumeration output format.",
            )

        findings = []

        for entry in records:
            if not isinstance(entry, dict):
                continue

            security_findings = [
                SecurityRuleEvaluator.evaluate_kerberoastable(entry),
                SecurityRuleEvaluator.evaluate_asrep_roastable(entry),
            ]

            for security_finding in security_findings:
                if security_finding is None:
                    continue

                findings.append(
                    Finding(
                        title=security_finding.technique_name,
                        severity=security_finding.severity.value,
                        description=(
                            f"{security_finding.explanation} "
                            f"Risk: {security_finding.risk_impact} "
                            f"Remediation: {security_finding.remediation}"
                        ),
                        evidence=json.dumps(
                            security_finding.evidence,
                            default=str,
                        ),
                    )
                )

        summary = (
            f"LDAP enumeration processed {len(records)} account record(s) "
            f"and identified {len(findings)} security finding(s)."
        )

        next_step = (
            "Review the identified account risks and remediation recommendations."
            if findings
            else "No Kerberoastable or AS-REP roastable accounts were identified in the returned records."
        )

        return AnalysisResult(
            summary=summary,
            findings=findings,
            recommended_next_step=next_step,
        )

    def _analyze_admin_access(self, result: ToolResult) -> AnalysisResult:
        """Interpret the result of an approved administrative access check."""

        try:
            data = json.loads(result.output or "{}")
        except (json.JSONDecodeError, TypeError):
            return AnalysisResult(
                summary="Administrative access output could not be parsed.",
                findings=[],
                recommended_next_step="Review the credential-check output.",
            )

        if not isinstance(data, dict):
            return AnalysisResult(
                summary="Administrative access returned an unexpected data structure.",
                findings=[],
                recommended_next_step="Review the tool output.",
            )

        is_admin = data.get("is_admin")
        evidence = json.dumps(data, default=str)

        if is_admin is True:
            findings = [
                Finding(
                    title="Administrative Access Confirmed",
                    severity="HIGH",
                    description=(
                        "The approved credential check reported administrative "
                        "access on the target system."
                    ),
                    evidence=evidence,
                )
            ]
            summary = "The approved credential check confirmed administrative access."
        elif is_admin is False:
            findings = []
            summary = "The credential check did not report administrative access."
        else:
            findings = []
            summary = "The credential check completed, but its administrative access status is unclear."

        return AnalysisResult(
            summary=summary,
            findings=findings,
            recommended_next_step="Review the access-check output and confirm that the test was authorized.",
        )

    def _analyze_smb_anonymous(self, result: ToolResult) -> AnalysisResult:
        """Analyze the results of an anonymous SMB access audit."""

        try:
            data = json.loads(result.output or "{}")
        except (json.JSONDecodeError, TypeError):
            return AnalysisResult(
                summary="SMB audit output could not be parsed as JSON.",
                findings=[],
                recommended_next_step="Review the SMB audit output format.",
            )

        if not isinstance(data, dict):
            return AnalysisResult(
                summary="SMB audit returned an unexpected data structure.",
                findings=[],
                recommended_next_step="Review the SMB audit output.",
            )

        status = str(data.get("status", "success")).lower()

        if status not in ("success", "completed"):
            return AnalysisResult(
                summary=f"SMB audit did not complete successfully: {data.get('error', status)}",
                findings=[],
                recommended_next_step="Check SMB audit configuration and target connectivity.",
            )

        shares = data.get("shares") or []

        if not isinstance(shares, list):
            shares = []

        findings = []

        if shares:
            findings.append(
                Finding(
                    title="Anonymous SMB Session Permitted",
                    severity="MEDIUM",
                    description=(
                        "The SMB audit returned accessible shares during "
                        "an anonymous access check."
                    ),
                    evidence=json.dumps(shares, default=str),
                )
            )

            for share in shares:
                if isinstance(share, dict):
                    share_name = str(share.get("name", ""))
                else:
                    share_name = str(share)

                if share_name.upper() in ("SYSVOL", "NETLOGON"):
                    findings.append(
                        Finding(
                            title=f"Sensitive SMB Share Accessible: {share_name}",
                            severity="HIGH",
                            description=(
                                f"The {share_name} share was returned by the "
                                "anonymous SMB audit. Review its actual permissions "
                                "and exposed contents."
                            ),
                            evidence=share_name,
                        )
                    )

            summary = f"The SMB audit returned {len(shares)} share(s) during anonymous access testing."
            next_step = "Review share permissions and verify whether sensitive data is exposed."
        else:
            summary = "The SMB audit did not identify any readable anonymous shares."
            next_step = "Review SMB access controls and continue with other authorized checks."

        return AnalysisResult(
            summary=summary,
            findings=findings,
            recommended_next_step=next_step,
        )
