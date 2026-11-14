# Agentic AI for Active Directory Security

An agentic AI system designed to investigate Active Directory environments, identify potential security weaknesses, and explain possible attack paths. The project combines AI-powered analysis with human approval to support security investigations in an authorized lab environment.

## 1. Project Overview

### Purpose

Active Directory environments can contain misconfigurations, excessive permissions, and relationships between accounts that create potential paths to higher privileges.

This project aims to simplify Active Directory security investigations by using an AI agent to collect information, analyze findings, and explain potential attack paths.

### Key Features

- **Active Directory Investigation:** Users can provide domain and target information through the frontend.
- **Security Enumeration:** Collects information using available security tools.
- **AI-Powered Analysis:** Analyzes collected evidence to identify potential security weaknesses.
- **Attack Path Identification:** Explains possible privilege escalation paths.
- **Human-in-the-Loop Approval:** Requires approval before actions that need authorization.
- **Investigation Results:** Returns findings and explanations to the frontend.
- **GOAD Lab Integration:** Uses Game of Active Directory (GOAD) as a controlled testing environment.

## 2. Project Workflow

1. **Input:** The user enters Active Directory domain and target information through the frontend.
2. **Validation:** The backend validates the request and checks the authorized scope.
3. **Investigation:** The AI agent uses available tools to collect information.
4. **Analysis:** The system analyzes collected evidence to identify potential weaknesses and attack paths.
5. **Approval:** Actions requiring authorization are submitted for human approval.
6. **Results:** Investigation findings and explanations are returned to the frontend.

## 3. Technology Stack

- **Frontend:** Web-based user interface.
- **Backend:** Python API and investigation services using FastAPI.
- **AI Model:** Ollama with a locally hosted language model.
- **Database:** SQLite for investigation-related data.
- **Planned Supporting Services:** PostgreSQL and Neo4j.
- **Security Testing Environment:** Game of Active Directory (GOAD).
- **Containerization:** Docker and Docker Compose.

## 4. Individual Contribution — Wintana Dereje

As a member of the six-person development team, my individual contribution focused on backend setup, analyzer implementation, and API verification.

My work included:

- Setting up the Python development environment.
- Installing the required project dependencies.
- Working on the backend analyzer component.
- Resolving an indentation and implementation issue in `agent/analyzer.py`.
- Checking the analyzer code using Python syntax compilation.
- Starting the FastAPI backend successfully.
- Verifying the API health endpoint.
- Accessing and reviewing the Swagger API documentation.

## 5. Individual Video Demonstration

**Five-Minute Project Demonstration**

[Insert individual video presentation link here]

## 6. GitHub Repositories

**Individual Submission — Wintana Dereje**

https://github.com/derejewintana-cmyk/Agentic-AI-for-Active-Directory-Security-main

**Original Group Repository**

https://github.com/Hermela-code/Agentic-AI-for-Active-Directory-Security

## 7. Team Members

The project was developed collaboratively by the following six team members.

| No. | Full Name | CTC ID |
|---|---|---|
| 1 | Hermela Girma | CTC-5848-26 |
| 2 | Feben Solomon | CTC-1718-26 |
| 3 | Meseret Telke | CTC-3934-26 |
| 4 | Wintana Dereje | CTC-4911-26 |
| 5 | Lidiya Alemayehu | CTC-204-26 |
| 6 | Yosef Walelign | CTC-2969-26 |

## 8. Project Status and Verification

The project is intended to support AI-assisted Active Directory security investigations in an authorized lab environment.

During my individual backend verification:

- The FastAPI backend started successfully.
- The API health endpoint returned a healthy status.
- The Swagger API documentation was accessible.
- The Ollama service was offline during this verification, so the complete AI-powered workflow was not independently verified.

## 9. Responsible Use

This project is intended for educational purposes and authorized Active Directory security assessments. All investigations should remain within approved environments and authorized scopes. Actions requiring authorization should follow the project's human approval process.

---

**Project Title:** Agentic AI for Active Directory Security  
**Individual Submission:** Wintana Dereje  
**Development:** Collaborative team project
