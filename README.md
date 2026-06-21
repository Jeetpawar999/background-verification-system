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
  "name": "Jeet",
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

---


