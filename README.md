# DevOps Capstone Project - Account Microservice

[![CI Build](https://github.com/shadabsayyad99-ops/capstone-final-project-devops-/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/shadabsayyad99-ops/capstone-final-project-devops-/actions/workflows/ci-build.yaml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

## Overview

This repository contains the completed Capstone Project for the **IBM DevOps and Software Engineering Professional Certificate**.

This project implements a production-ready **Account RESTful Microservice** developed using Test-Driven Development (TDD), Behavior-Driven Development (BDD), containerized using Docker, automated via GitHub Actions Continuous Integration (CI), deployed to Kubernetes, and delivered through an automated Tekton Continuous Delivery (CD) pipeline.

## Features

- **RESTful API**: Full CRUD operations (Create, Read, Update, Delete, List) for Customer Accounts.
- **TDD / Testing**: High code coverage (94%+) using `nosetests` and Python `coverage`.
- **Code Quality**: Strict linting and formatting compliance with `flake8` and `pylint`.
- **Security & Headers**: Secure HTTP headers implemented via `Flask-Talisman` and Cross-Origin Resource Sharing handled by `Flask-CORS`.
- **Continuous Integration**: Automated CI pipeline via GitHub Actions (`ci-build.yaml`).
- **Containerization**: Optimized non-root container image defined in `Dockerfile` served by Gunicorn.
- **Kubernetes Orchestration**: Deployment manifests, ReplicaSets, and NodePort services.
- **Continuous Delivery**: Automated cloud-native pipeline using Tekton (`pipelinerun`).

## Project Layout

```text
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── user-story.md       <- User Story Issue Template
│   └── workflows/
│       └── ci-build.yaml       <- GitHub Actions CI Workflow
├── service/                    <- Microservice package
│   ├── common/                 <- Common log & error handlers
│   ├── __init__.py             <- App factory, Talisman & CORS setup
│   ├── config.py               <- Flask configuration
│   ├── models.py               <- Persistent Account model
│   └── routes.py               <- REST API endpoints
├── Dockerfile                  <- Container configuration
├── requirements.txt            <- Python dependencies
├── setup.cfg                   <- Linting & testing configuration
└── tests/                      <- Unit and integration test suite
```

## Running the Application

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run tests**:
   ```bash
   nosetests
   ```
3. **Run service**:
   ```bash
   honcho start
   ```
   or
   ```bash
   gunicorn --bind 0.0.0.0:8080 service:app
   ```

## Author

- **Shahadab Sayyad** ([@shadabsayyad99-ops](https://github.com/shadabsayyad99-ops))
