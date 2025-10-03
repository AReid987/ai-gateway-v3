# Spec Requirements Document

> Spec: Deploy Helicone AI Gateway
> Created: 2025-09-21

## Overview

Deploy the Helicone AI Gateway as a single Docker container with a PostgreSQL database to act as the core entry point for all LLM traffic. This gateway will be structured as an application within a Turborepo monorepo.

## User Stories

### Deploy Helicone AI Gateway

As a developer, I want to deploy the Helicone AI Gateway as a single Docker container, so that it can act as the core entry point for all LLM traffic within a Turborepo monorepo.

## Spec Scope

1.  **Create `docker-compose.yml`** - Create a `docker-compose.yml` file in `apps/ai-gateway/infra` to define the Helicone Gateway and PostgreSQL database services.
2.  **Define Environment Variables** - Define all necessary environment variables for Helicone and the database connection in a `.env.example` file in `apps/ai-gateway/infra`.
3.  **Local Deployment** - Deploy the services locally using `docker-compose`.
4.  **Verification** - Verify that the Helicone Gateway and Dashboard are accessible.
5.  **Documentation** - Write a `README.md` in the `apps/ai-gateway/infra` directory documenting the deployment steps.

## Out of Scope

- Kubernetes deployment.
- Configuration of LLM providers.
- Advanced routing, caching, or security configurations.

## Expected Deliverable

1.  A running local instance of the Helicone AI Gateway and its dashboard, accessible via a web browser.
2.  A `docker-compose.yml` and `.env.example` file located in the `apps/ai-gateway/infra` directory.
3.  A `README.md` file in the `apps/ai-gateway/infra` directory with clear instructions on how to deploy and run the gateway locally.