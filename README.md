# MSD — Medical Sensor Data Platform (Parkinson’s Finger-Movement Monitoring)

MSD is a prototype platform for collecting, validating, and visualizing medical sensor measurements for Parkinson’s patients.  
It focuses on **standard-compliant data exchange (HL7 FHIR)** and **3D visualization** of finger-movement sensor data to support clinical workflows.

Repository: https://github.com/elalawani/MSD

---

## What the platform does

### 1) FHIR compliance validation (quality gate)
Before sensor data is shown in the 3D viewer, it is validated against **HL7 FHIR** requirements using an open-source FHIR server (HAPI FHIR).  
The system provides feedback when incoming data does not meet the required standard (e.g., missing fields, invalid structure).

### 2) 3D visualization for clinical interpretation
Sensor recordings (finger movement) are presented as a **3D view** to help clinicians evaluate movement characteristics relevant for Parkinson’s diagnosis and monitoring.

### 3) Patient-centered collaboration features
When a new patient is registered, the platform automatically creates a **patient-specific chat group** and assigns the responsible staff (doctors / nurses).

Inside the patient group:
- **To-Do workflow**: doctors can create patient-related tasks; nurses can “claim” a task with one click and manage it in their personal task list (status updates, completion, deletion).
- **Questionnaires**: example implementation for the **Barthel Index**; additional questionnaires are prepared as placeholders in the UI.
- **Vital signs & clinical measurements**: nurses can enter measurements such as blood pressure, temperature, respiration rate, heart rate, etc.

---

## Architecture (high level)

- **MSD/** — Backend services (Python) and integration logic (including FHIR validation workflow)
- **MSDV/** — Frontend (Vue) UI, including the 3D visualization view
- **docker-compose.yml** — Local development stack orchestration

> Naming: MSD = “Medical Sensor Data”; MSDV = “Medical Sensor Data View” (3D visualization UI)

---

## Tech stack

- Frontend: **Vue.js** (MSDV)
- Backend: **Python** (MSD)
- Standards / interoperability: **HL7 FHIR** via **HAPI FHIR server**
- Local orchestration: **Docker Compose**

---

## Getting started (local)

### Prerequisites
- Docker + Docker Compose installed

### Run
```bash
git clone https://github.com/elalawani/MSD.git
cd MSD
docker compose up --build
