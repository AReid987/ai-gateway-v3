---
type: Page
title: '4. Story 1.1: Deploy Helicone AI Gateway'
description: null
icon: null
createdAt: '2025-09-18T12:35:03.251Z'
creationDate: 2025-09-18 07:35
modificationDate: 2025-09-18 07:37
tags: []
coverImage: null
---

### 4. Story 1.1: Deploy Helicone AI Gateway

# Story 1.1: Deploy Helicone AI Gateway

## Status: Draft

## Story

- As a **developer**,

- I want to **deploy the Helicone AI Gateway as a single Docker container or on Kubernetes**,

- so that **it can act as the core entry point for all LLM traffic**.

## Acceptance Criteria (ACs)

1. The Helicone Gateway Docker container is successfully deployed and accessible.

2. A local PostgreSQL database is configured and connected to the Helicone Gateway.

3. The Helicone Gateway and its associated database are deployed according to the monorepo structure, with configuration files placed in `infra/docker/` or `infra/kubernetes/`.

4. The Helicone Dashboard is accessible via a web browser.

5. Local testability: The deployed instance can be accessed via `curl` and the dashboard is functional in a local development environment.

## Tasks / Subtasks

- [ ] Create a `docker-compose.yml` file to define the Helicone Gateway and PostgreSQL database services.

- [ ] Define all necessary environment variables for Helicone and the database connection in a `.env.example` file.

- [ ] Run `docker-compose up` to deploy the services locally.

- [ ] Verify the Helicone Gateway is running and accessible.

- [ ] Verify the Helicone Dashboard is accessible and connected to the database.

- [ ] Write a `README.md` in the `infra/` directory documenting the deployment steps.

## Dev Technical Guidance

This story is foundational, replacing the complex multi-service deployment of our original plan with a single, streamlined process.

- **Technology Stack:** Helicone AI Gateway, Docker, PostgreSQL.

- **Infrastructure:** The deployment should align with the Infrastructure as Code (IaC) requirement and integrate with the monorepo's `infra/` directory.

- **Security:** Pay close attention to securing the database connection and managing environment variables.

- **References:**

    - Helicone AI Gateway Documentation: [https://docs.helicone.ai/gateway/self-hosting/docker](https://www.google.com/search?q=https://docs.helicone.ai/gateway/self-hosting/docker)

## Story Progress Notes

### Agent Model Used: Fiona "Flux" Rivera (SM Agent)

### Completion Notes List

{To be filled by Developer Agent upon completion}

### Change Log

- Initial Draft | 2025-09-18 | Fiona "Flux" Rivera (SM Agent)

