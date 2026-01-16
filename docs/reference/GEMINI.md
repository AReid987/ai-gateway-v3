# AI Gateway v3 Project

## Project Overview

This project is in the planning and documentation phase for building an **AI Gateway v3**. The core of the project is to use the open-source **Helicone AI Gateway** to create a single, resilient, and cost-effective entry point for interacting with a wide range of Large Language Models (LLMs). The project is structured as a Turborepo monorepo to support the long-term goal of creating reusable, standalone services.

The main goals of the project are:
*   **Cost Efficiency:** Reduce LLM API costs.
*   **Reliability:** Ensure high uptime and handle provider outages.
*   **Performance:** Achieve fast response times.
*   **Observability:** Provide a unified dashboard for monitoring and analytics.

The project is centered around deploying and configuring a Helicone instance, which will handle intelligent routing, caching, fallbacks, and security for LLM requests.

## Project Structure

This project is a Turborepo monorepo with the following structure:

-   `apps/`: Contains the individual applications.
    -   `ai-gateway/`: The Helicone AI Gateway application.
-   `packages/`: Contains shared code and configurations.

## Building and Running

The AI Gateway application is a Dockerized service. To run it locally, navigate to the `apps/ai-gateway/infra` directory and follow the instructions in the `README.md` file.

## Development Conventions

As the project is in a pre-implementation phase, there are no established coding conventions. The `2 The AI Gateway Architecture Document.md` states that when implementation begins, conventions will apply to:

*   **Infrastructure as Code (IaC):** For managing the deployment of Helicone.
*   **Custom Scripts:** For any deployment or testing scripts.

## Key Files

The most important files in this directory are the planning and documentation files found in `ai-gateway-v3-docs/Pages/`:

*   `1 The AI Gateway Project Brief.md`: Outlines the project's vision, problem statement, and success metrics.
*   `2 The AI Gateway Architecture Document.md`: Provides a detailed technical blueprint for the project, centered around the Helicone AI Gateway.
*   `AI Gateway Product Requirements Document (PRD).md`: Defines the functional and non-functional requirements for the AI Gateway.
*   `AI Gateway v3 Overview.md`: A summary of the project and the decision to use Helicone as the core component.