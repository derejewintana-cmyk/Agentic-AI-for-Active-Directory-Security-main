# Agentic AI for Active Directory Security

An agentic AI system designed to investigate Active Directory environments, identify potential security weaknesses, and explain possible attack paths. The project combines AI-powered analysis with human approval to support security investigations in an authorized lab environment.

## 1. Project Overview

### Purpose

Active Directory environments can contain misconfigurations, excessive permissions, and relationships between accounts that create potential paths to higher privileges.

This project aims to simplify Active Directory security investigations by using an AI agent to collect information, analyze findings, and explain potential attack paths.

### Key Features

- Active Directory investigation through a frontend and backend.
- Security enumeration using available security tools.
- AI-powered analysis of collected evidence.
- Identification and explanation of potential attack paths.
- Human-in-the-loop approval for actions requiring authorization.
- Investigation findings and explanations presented to users.
- GOAD (Game of Active Directory) lab integration for controlled testing.

## 2. How It Works

1. **Input:** The user provides Active Directory domain and target information through the frontend.
2. **Validation:** The backend processes the request and checks the authorized scope.
3. **Investigation:** The AI agent uses available tools to gather information.
4. **Analysis:** Collected evidence is analyzed to identify potential security weaknesses.
5. **Human Approval:** Actions requiring authorization are submitted for approval.
6. **Results:** Findings and explanations are returned for review.

## 3. Technology Stack

- **Frontend:** Web-based user interface.
- **Backend:** Python and FastAPI.
- **AI Model:** Ollama with a locally hosted language model.
- **Database:** SQLite for investigation-related data.
- **Supporting Services:** PostgreSQL and Neo4j as planned supporting technologies.
- **Security Testing Environment:** Game of Active Directory (GOAD).
- **Containerization:** Docker and Docker Compose.

## 4. Individual Contribution — Wintana Dereje

As a member of the project development team, my contribution focused on the backend component.

My work included:

- Setting up the Python development environment.
- Installing the required project dependencies.
- Working on the backend analyzer component.
- Resolving an indentation and implementation issue in `agent/analyzer.py`.
- Checking the analyzer's Python syntax.
- Starting the FastAPI backend successfully.
- Verifying the API health endpoint and Swagger documentation.

## 5. Video Presentation

**Individual Five-Minute Project Demonstration**

[Insert individual video presentation link here]

## 6. GitHub Repositories

**Individual Submission:**

https://github.com/derejewintana-cmyk/Agentic-AI-for-Active-Directory-Security

**Original Group Project:**

https://github.com/Hermela-code/Agentic-AI-for-Active-Directory-Security

## 7. Team Members

The project was developed collaboratively by six team members.

| No. | Full Name | CTC ID |
|---|---|---|
| 1 | Hermela Girma | CTC-5848-26 |
| 2 | Feben Solomon | CTC-1718-26 |
| 3 | Meseret Telke | CTC-3934-26 |
| 4 | Wintana Dereje | CTC-4911-26 |
| 5 | Lidiya Alemayehu | CTC-204-26 |
| 6 | Yosef Walelign | CTC-2969-26 |

## 8. Project Status

The project provides a framework for AI-assisted Active Directory security investigation. During my individual backend verification, the FastAPI server started successfully, the health endpoint responded successfully, and the Swagger API documentation was accessible. The Ollama service was offline during this verification, so the complete AI-powered workflow was not independently verified.

## 9. Responsible Use

This project is intended for educational purposes and authorized Active Directory security assessments. All investigations should remain within approved environments and scope, with appropriate authorization for security actions.

---

**Project:** Agentic AI for Active Directory Security  
**Individual Submission:** Wintana Dereje  
**Team Project:** Agentic AI for Active Directory Security
