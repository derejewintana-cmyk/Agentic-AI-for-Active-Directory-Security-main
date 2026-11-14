# Agentic AI for Active Directory Security

An agentic AI system designed to investigate Active Directory environments, identify potential security weaknesses, and explain possible attack paths. The project combines AI-powered analysis, security enumeration tools, and human-in-the-loop approval to support security investigations in authorized lab environments.

## 1. Project Overview

### Purpose

Active Directory environments can contain security misconfigurations, excessive permissions, and relationships between accounts that may create opportunities for privilege escalation.

This project aims to simplify Active Directory security investigations by using an AI agent to collect information, analyze evidence, identify potential weaknesses, and explain possible attack paths.

### Key Features

- **Active Directory Investigation:** Allows users to provide domain and target information through the frontend.
- **Security Enumeration:** Uses available security tools to collect information from the target environment.
- **AI-Powered Analysis:** Analyzes collected evidence to identify potential security weaknesses.
- **Attack Path Identification:** Helps explain possible privilege escalation paths.
- **Human-in-the-Loop Approval:** Requires human approval before actions that need authorization.
- **Investigation Results:** Provides investigation findings and explanations to the frontend.
- **GOAD Lab Integration:** Supports testing in the Game of Active Directory (GOAD) environment.

## 2. Project Workflow

1. **Input:** The user enters Active Directory domain and target information through the frontend.
2. **Validation:** The backend validates the investigation request and checks the authorized scope.
3. **Investigation:** The agent uses available security tools to collect information.
4. **Analysis:** The system analyzes collected evidence to identify potential weaknesses and attack paths.
5. **Approval:** Actions requiring authorization are submitted for human approval.
6. **Results:** Investigation findings and explanations are returned to the frontend.

## 3. Technology Stack

- **Frontend:** Web-based user interface.
- **Backend:** Python and FastAPI for API development and investigation services.
- **AI Model:** Ollama with a locally hosted language model.
- **Database:** SQLite and PostgreSQL for investigation-related data.
- **Knowledge Graph:** Neo4j for representing relationships and potential attack paths.
- **Security Testing Environment:** Game of Active Directory (GOAD).
- **Containerization:** Docker and Docker Compose.

## 4. Individual Contribution — Wintana Dereje

**Assigned Role: Backend and Database**

As a member of the six-person development team, my assigned role focused on the backend and database components of the project.

### Assigned Responsibilities

My responsibilities included:

- FastAPI backend development.
- API design and backend communication.
- Database development and PostgreSQL integration.
- Investigation session management.
- Storage of investigation findings.
- Tool execution records.
- Approval records.
- Communication between the frontend and the AI agent.

### Individual Work and Implementation

My individual work included:

- Setting up the local Python development environment.
- Creating and configuring the project's virtual environment.
- Installing the required project dependencies.
- Working on the `agent/analyzer.py` component.
- Resolving an indentation error and addressing a missing analyzer implementation.
- Checking the analyzer code using Python syntax compilation.
- Running the FastAPI backend successfully.
- Verifying the API health endpoint.
- Accessing and reviewing the Swagger API documentation.

These activities contributed to the backend setup, analyzer functionality, and API verification of the project.

## 5. Individual Video Demonstration

**Individual Project Walkthrough — Wintana Dereje**

[Watch the Individual Project Demonstration](https://drive.google.com/file/d/1DWR5myv7h9OYKGvorkqb1TMFOZdljy6c/view?usp=sharing)

The video demonstrates the project structure, relevant backend and agent components, and the FastAPI application through its API documentation and health endpoint.

## 6. GitHub Repositories

**Individual Submission — Wintana Dereje**

[View Individual GitHub Repository](https://github.com/derejewintana-cmyk/Agentic-AI-for-Active-Directory-Security-main)

**Original Group Repository**

[View Original Group Repository](https://github.com/Hermela-code/Agentic-AI-for-Active-Directory-Security)

## 7. Team Members

The project was developed collaboratively by the following six team members.

| No. | Full Name        | CTC ID      |
| --- | ---------------- | ----------- |
| 1   | Hermela Girma    | CTC-5848-26 |
| 2   | Feben Solomon    | CTC-1718-26 |
| 3   | Meseret Telke    | CTC-3934-26 |
| 4   | Wintana Dereje   | CTC-4911-26 |
| 5   | Lidiya Alemayehu | CTC-204-26  |
| 6   | Yosef Walelign   | CTC-2969-26 |

## 8. Project Status and Verification

The project is designed to support AI-assisted Active Directory security investigations in an authorized lab environment.

The backend implementation includes API endpoints for:

- Investigation creation and retrieval.
- Investigation findings.
- Tool execution records.
- Approval management.
- Backend health monitoring.

The local backend verification confirmed that the FastAPI application started successfully, the health endpoint returned a healthy status, and the Swagger API documentation was accessible.

The project also incorporates AI-assisted analysis, database support, and a human-in-the-loop approval process as part of its overall architecture.

## 9. Responsible Use

This project is intended for educational purposes and authorized Active Directory security assessments. All investigations should be conducted only within approved environments and authorized scopes. Actions requiring authorization should follow the project's human-in-the-loop approval process.

---

**Project Title:** Agentic AI for Active Directory Security\
**Individual Submission:** Wintana Dereje\
**Assigned Role:** Backend and Database\
**Development:** Collaborative team project

**After pasting:** Click **Commit changes** on GitHub so the updated README appears in your individual repository. Then check that the video link opens without requesting access.
