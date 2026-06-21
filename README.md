# Background Verification System

## Project Overview

This project is an AI-powered Background Verification System built using FastAPI and Python.

The system verifies the following candidate information:

* Name
* Date of Birth (DOB)
* Address

Each verification task is handled by a dedicated agent.

---

## Key Features

### Verification Agents

* Name Verification Agent
* DOB Verification Agent
* Address Verification Agent

### Orchestration Layer

* Executes all verification agents
* Aggregates verification results
* Generates the final verification report

### State Management

* Maintains the current verification state
* Determines the final verification status (Verified/Failed)

### Audit Trail

* Records all verification events
* Stores logs with timestamps

### REST APIs

* POST /verify
* GET /audit

---

## Project Structure

```text
background-verification-system/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── models/
│   ├── orchestration/
│   ├── state/
│   ├── utils/
│   └── main.py
│
├── tests/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Installation

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Candidate Verification

### API Endpoint

```http
POST /verify
```

### Request Example

```json
{
  "name": "J",
  "dob": "1995-01-15",
  "address": "India"
}
```

### Response Example

```json
{
  "status": "completed",
  "results": {
    "name": {
      "verified": true
    },
    "dob": {
      "verified": true
    },
    "address": {
      "verified": true
    }
  }
}
```

---

## Audit Logs

### API Endpoint

```http
GET /audit
```

Returns the complete verification audit history and logs.

---

## Docker Setup

### Build Docker Image

```bash
docker build -t bgv-system .
```

### Run Docker Container

```bash
docker run -p 8000:8000 bgv-system
```

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Asyncio
* Docker

## System Architecture

```
Client Request
      |
      v
FastAPI API Layer
      |
      v
Orchestrator
      |
      +--> Name Verification Agent
      +--> DOB Verification Agent
      +--> Address Verification Agent
      |
      v
State Manager
      |
      v
Audit Logger
      |
      v
Final Verification Response
```

## Execution Flow

1. Client submits candidate data through POST /verify
2. Request is validated using Pydantic schemas
3. Orchestrator initializes the verification workflow
4. Verification agents execute independently
5. Results are aggregated and stored in the state manager
6. Audit logs are generated
7. Final verification report is returned

## State Management

The system maintains:

* run_id
* execution status
* verification results
* cache status
* audit history

State transitions:

```
Running -> Completed
Running -> Failed
Completed -> Cached
```

## Execution States

| State     | Description                                |
| --------- | ------------------------------------------ |
| Running   | Verification is currently executing        |
| Completed | Verification completed successfully        |
| Failed    | One or more verification checks failed     |
| Fresh     | Result generated from a new execution      |
| Cached    | Result retrieved from a previous execution |

## Selective Re-Execution Logic

The system supports selective re-execution to avoid unnecessary processing.

Rules:

* If candidate information changes, only affected agents are re-executed.
* Unchanged verification results are reused from cache.
* This reduces execution time and improves efficiency.

Example:

Initial Verification:

* Name: Jeet Pawar
* DOB: 1995-01-15
* Address: Pune

Updated Verification:

* Name: Jeet Pawar
* DOB: 1995-01-15
* Address: Pune

Outcome:

* Address Verification Agent executes again.
* Name Verification Agent uses cached result.
* DOB Verification Agent uses cached result.

---


