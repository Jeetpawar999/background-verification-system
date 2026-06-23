# Background Verification System

## Project Overview

This project is an AI-powered Background Verification System built using FastAPI and Python.

The system performs Identity, Criminal, and Financial background verification using independent verification agents executed through a centralized orchestration layer.

The application supports:

* Identity Verification
* Criminal Background Verification
* Financial Verification
* Audit Logging
* State Management
* File Upload Support
* Docker Deployment

---

# Key Features

## Identity Verification

* Name Validation Agent
* DOB Verification Agent
* Address Verification Agent

## Criminal Background Verification

* Federal Criminal Check Agent
* State Criminal Check Agent
* County Records Check Agent

## Financial Verification

* Credit Verification Agent
* Fraud Detection Agent
* PEP Screening Agent

## Orchestration Layer

* Executes verification agents in parallel using AsyncIO
* Aggregates verification results
* Generates final verification response

## State Management

* Maintains verification state
* Stores execution results
* Tracks execution status
* Supports cached/fresh execution tracking

## Audit Trail

* Records verification events
* Stores execution timestamps
* Maintains execution history

## REST APIs

* POST /verify
* GET /audit
* GET /

---

# Project Structure

```text
background-verification-system/

├── app/
│
├── agents/
│   ├── identity/
│   ├── criminal/
│   └── financial/
│
├── api/
├── audit/
├── models/
├── orchestration/
├── state/
│
├── uploads/
├── tests/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Installation

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

Application URL

```text
http://127.0.0.1:8000
```

Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check

```http
GET /
```

Response

```json
{
  "status": "ok"
}
```

---

## Verify Candidate

```http
POST /verify
```

### Form Parameters

| Parameter     | Type   |
| ------------- | ------ |
| full_name     | String |
| dob           | String |
| address       | String |
| government_id | String |
| aadhaar_image | File   |

### Example Input

```text
full_name = Jeet Pawar
dob = 1995-11-19
address = Pune
government_id = ABC123456
aadhaar_image = aadhaar.jpg
```

### Example Response

```json
{
  "run_id": "12345678",
  "status": "completed",
  "cache_status": {
    "identity": "fresh",
    "criminal": "fresh",
    "financial": "fresh"
  }
}
```

---

## Audit Logs

```http
GET /audit
```

### Example Response

```json
[
  {
    "agent": "verification",
    "status": "started"
  },
  {
    "agent": "identity_verification",
    "status": "completed"
  },
  {
    "agent": "criminal_verification",
    "status": "completed"
  },
  {
    "agent": "financial_verification",
    "status": "completed"
  }
]
```

---

# System Architecture

```text
Client Request
      |
      v
FastAPI API Layer
      |
      v
Orchestrator
      |
      +--> Name Validation Agent
      +--> DOB Verification Agent
      +--> Address Verification Agent
      |
      +--> Federal Criminal Check Agent
      +--> State Criminal Check Agent
      +--> County Records Check Agent
      |
      +--> Credit Verification Agent
      +--> Fraud Detection Agent
      +--> PEP Screening Agent
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

---

# Execution Flow

1. User submits candidate information through POST /verify
2. FastAPI validates incoming request
3. Orchestrator starts verification workflow
4. Identity agents execute
5. Criminal agents execute
6. Financial agents execute
7. Results are aggregated
8. State Manager stores execution results
9. Audit Logger records execution history
10. Final verification response is returned

---

# State Management

The system maintains:

* Run ID
* Verification Status
* Verification Results
* Cache Status
* Execution History
* Audit Logs

---

# Execution States

| State     | Description                           |
| --------- | ------------------------------------- |
| Running   | Verification currently executing      |
| Completed | Verification completed successfully   |
| Failed    | Verification execution failed         |
| Fresh     | Result generated from new execution   |
| Cached    | Result reused from previous execution |

---

# Docker Setup

## Build Docker Image

```bash
docker build -t bgv-system .
```

## Run Docker Container

```bash
docker run -p 8000:8000 bgv-system
```

## Run Using Docker Compose

```bash
docker-compose up --build
```

---

# Technologies Used

* Python 3.11
* FastAPI
* Pydantic
* AsyncIO
* Uvicorn
* Docker
* Git
* GitHub

---



---


