
# Incident Management System (IMS)

## Architecture
Producer -> FastAPI -> In-memory store -> UI

## Features
- Debouncing logic
- Async-ready structure
- RCA enforcement
- MTTR calculation
- Prometheus metrics ready

## Run
docker-compose up --build

## GitHub Link
(Add your repo link here)

## Screenshots
(Add UI + logs screenshots)

## Explanation

### Debouncing
Single work item per component

### Async Processing
FastAPI supports async endpoints

### RCA Enforcement
Cannot close without RCA

### MTTR
Calculated automatically
