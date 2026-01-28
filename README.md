# MSD — Medical Sensor Data Platform (Parkinson’s Finger-Movement Monitoring)

MSD is a hospital-staff platform for validating and visualizing medical sensor measurements for Parkinson’s patients. The core focus is **standard-compliant data exchange (HL7 FHIR)** and a **3D visualization** of finger-movement sensor data to support clinical workflows.

Repository: https://github.com/elalawani/MSD

---

## What the platform does

### 1) HL7 FHIR compliance validation (quality gate)
Before sensor data is shown in the 3D viewer, it is checked against HL7 FHIR requirements using an open-source FHIR server (**HAPI FHIR**). The platform provides feedback if the submitted data is not compliant (e.g., missing required elements or invalid structure).

### 2) 3D visualization for clinical interpretation
Finger-movement sensor data is displayed as a **3D view** to support clinical assessment relevant for Parkinson’s diagnosis and monitoring.

### 3) Patient-scoped collaboration workflows (hospital staff only)
This platform is intended for **hospital staff** (no patient login). When a new patient is registered, the platform creates a **patient-specific workspace (chat group)** and assigns the responsible staff (doctors/nurses).

Inside the patient workspace:
- **Chat group** for the patient’s care team.
- **To-Do workflow**: doctors can create To-Dos; nurses can claim a To-Do with one click and manage it in their personal To-Do list (with related information such as patient, time, place, goal). Nurses can mark tasks as done or delete them.
- **Questionnaires**: example implementation for **Barthel Index** with PDF export; other questionnaires exist as frontend placeholders.
- **Clinical measurements**: nurses can enter values such as blood pressure, temperature, respiration rate, heart rate, and more.

---

## Role-based profiles & access control (hospital staff only)

The platform uses **role-based profiles** to separate responsibilities and reduce the risk of unauthorized actions.

### Roles
- **Nurse**
  - Access assigned patient workspaces.
  - Claim and manage To-Dos in a personal task list.
  - Enter clinical measurements (e.g., blood pressure, temperature, respiration rate, heart rate).
  - Fill questionnaire responses (e.g., Barthel Index) and export as PDF.

- **Doctor**
  - Access assigned patient workspaces.
  - Create and track To-Dos for a patient workspace.
  - Review validated sensor data and use the 3D visualization view.

- **Admin (staff)**
  - Manage staff accounts and role assignment.
  - Register new patients and assign responsible staff.
  - Oversee operational configuration (deployment/runtime setup).

### Group-based access scope
When a new patient is registered, a **patient-specific workspace** is created and responsible staff are assigned. Access to chat, To-Dos, questionnaires, and measurements is scoped to that patient workspace.

---

## Accessibility (UI/UX)

The UI is intended for hospital environments. Accessibility goals include:
- Keyboard-friendly navigation for core workflows (navigation, forms, To-Dos).
- Semantic markup and clear labeling for interactive elements.
- Consistent validation and human-readable error messages (including FHIR validation feedback).
- Responsive layout for common workstation screen sizes.

> Note: 3D views can be challenging for assistive technologies; where possible, provide complementary text summaries (key values/metrics) alongside the visualization.

---

## Architecture (Docker Compose)

This repository is organized as a multi-service stack orchestrated via Docker Compose:

- **backend** (Django / Python) — runs on `0.0.0.0:8000`
- **frontend** (Vue / Vite) — runs on `0.0.0.0:5173`
- **fhir** (HAPI FHIR server) — exposed locally on `localhost:8081` (container port 8080)
- **postgres** (PostgreSQL database) — exposed locally on `localhost:5432`

---

## Repository structure

- `docker-compose.yml` — builds and runs all services (backend, frontend, fhir, postgres)
- `env/` — Python virtual environment for running Django without Docker (optional)
- `MSD/` — backend (Django/Python)
- `MSDV/` — frontend (Vue/Vite/Tailwind)

### MSD/ (Backend)
- `requirements.txt` — Python dependencies
- Dockerfile — backend image build instructions
- Django project setup — `manage.py`, settings, backend modules

### MSDV/ (Frontend)
- `package.json` — frontend dependencies
- Vite + Tailwind configuration
- Dockerfile — frontend image build instructions

---

## Tech stack

- **Frontend**: Vue.js (Vite), Tailwind CSS
- **Backend**: Python + Django
- **Database**: PostgreSQL
- **Interoperability standard**: HL7 FHIR
- **FHIR server**: HAPI FHIR (`hapiproject/hapi:latest`)
- **Local orchestration**: Docker Compose

---

## Getting started (Docker)

### Prerequisites
- Docker + Docker Compose installed

### 1) Build images
```bash
docker-compose build
