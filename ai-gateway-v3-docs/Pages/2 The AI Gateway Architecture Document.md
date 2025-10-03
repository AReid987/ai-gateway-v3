---
type: Page
title: 2. The AI Gateway Architecture Document
description: null
icon: null
createdAt: '2025-09-19T01:44:51.091Z'
creationDate: 2025-09-18 20:44
modificationDate: 2025-09-19 04:48
tags: []
coverImage: null
---

### 2. The AI Gateway Architecture Document

# AI Gateway Architecture Document

## Introduction / Preamble

This document outlines the project architecture for the AI Gateway, now simplified and centered around **Helicone's open-source AI Gateway**. Its primary goal is to serve as the guiding architectural blueprint for AI-driven development, ensuring consistency and adherence to the chosen technologies and a streamlined deployment model. The architecture is no longer a complex, multi-component system but a single, performant proxy with an integrated dashboard.

## Technical Summary

The AI Gateway will be a single, high-performance proxy for Large Language Models, utilizing **Helicone's Rust-based AI Gateway**. It will be deployed via containerization (Docker) and orchestrated (Kubernetes/Kuma). The architecture is designed to simplify deployment, enhance performance, and provide a unified, out-of-the-box observability dashboard. It natively handles intelligent routing, fallbacks, caching, and rate limiting, replacing the need for multiple disparate services. The system prioritizes high availability, ultra-low latency, and robust security.

## High-Level Overview

The architecture follows a transparent proxy pattern. The entire system is comprised of the Helicone Gateway and an optional, but highly recommended, data persistence layer for its built-in dashboard. Requests will flow from external applications through the Helicone proxy, which handles all routing, reliability, and optimization logic before forwarding the request to the appropriate LLM provider. All operational data is collected internally by Helicone and made available through its integrated dashboard.

```text
graph TD
    subgraph Client-Facing Layer
        U[User/Application] --> H[Helicone AI Gateway]
    end
    subgraph Helicone Core
        subgraph Helicone Services
            direction LR
            H --> R[Router]
            H --> L[LLM Security]
            H --> C[Caching]
        end
        R --> P[LLM Provider 1<br>(e.g., OpenAI)]
        R --> P2[LLM Provider 2<br>(e.g., Anthropic)]
        R --> P3[LLM Provider 3<br>(e.g., Groq)]
        subgraph Helicone Observability
            H -- Metrics/Logs/Traces --> O[Observability Engine]
            H -- Caching Data --> M[DB/Cache Layer<br>(PostgreSQL/Redis)]
            O --> D[Built-in Dashboard]
        end
    end
    style U fill:#F5E8D9,stroke:#AD7034,stroke-width:2px
    style H fill:#D9E8F5,stroke:#3470AD,stroke-width:2px
    style R fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style L fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style C fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style O fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style M fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style D fill:#E0F2F7,stroke:#2F8F9F,stroke-width:2px
    style P fill:#F5E8D9,stroke:#AD7034,stroke-width:2px
    style P2 fill:#F5E8D9,stroke:#AD7034,stroke-width:2px
    style P3 fill:#F5E8D9,stroke:#AD7034,stroke-width:2px
```

*Description: This diagram illustrates the simplified architecture centered on the Helicone AI Gateway. The User/Application interacts with the single Helicone proxy. Helicone internally handles routing, security, and caching before forwarding requests to the appropriate LLM providers. All request data is simultaneously sent to Helicone's internal Observability Engine for real-time monitoring and display on its built-in dashboard.*

## Architectural / Design Patterns Adopted

- **Transparent Proxy Pattern:** Helicone acts as a transparent proxy, requiring only a change to the API base URL in the client application.

- **Monolithic (single binary) / Modular (internally):** The system is a single binary for ease of deployment, but its internal design is modular, with distinct components for routing, caching, and observability.

- **Circuit Breaker/Retry Pattern:** Helicone's native fallback and retry mechanisms adhere to these patterns.

- **Load Balancing Pattern:** Built-in intelligent load balancing across providers is a core feature.

- **Observability Pattern:** Helicone provides a complete, out-of-the-box observability solution with native logging, metrics, and tracing.

## Component View

The system is now composed of a single primary component and its dependencies:

- **Helicone AI Gateway:**

    - **Responsibility:** The core of the system. It handles all external traffic, intelligent routing, load balancing, caching, rate limiting, and LLM-specific security. It also serves as the data collection point for observability.

    - **Key Capabilities:**

        - **LLM Router:** Dynamically selects the best LLM model based on configurable criteria.

        - **Caching Engine:** Handles request/response caching to reduce costs and latency.

        - **LLM Security:** Provides built-in prompt injection and security guardrails.

        - **Virtual Key Management:** Manages virtual keys and their associated configurations.

- **Helicone Built-in Dashboard:**

    - **Responsibility:** An integrated web UI for visualizing operational insights (logs, metrics, traces) and managing gateway configurations. This replaces the need for a separate Next.js application.

- **Data Persistence Layer (Optional):**

    - **Responsibility:** Helicone can be configured to use an external database (e.g., PostgreSQL) or an in-memory Redis cache for its observability and caching data, respectively. This provides long-term persistence and is highly recommended for production.

## Project Structure (Revised)

The project structure will be significantly simplified.

```text
{project-root}/
├── .github/                      # CI/CD workflows (GitHub Actions)
│   └── workflows/
│       └── main.yml
├── docs/                         # Project documentation
│   ├── prd.md                    # Product Requirements Document
│   ├── architecture.md           # This Architecture Document
│   └── ...
├── infra/                        # Infrastructure as Code (e.g., Docker, Kubernetes, Kuma)
│   ├── docker-compose.yml        # Docker Compose file for local dev
│   ├── kubernetes/               # Kubernetes manifests
│   └── helicone.env.example      # Example environment variables for Helicone
├── README.md                     # Project overview and setup instructions
└── .gitignore                    # Git ignore rules
```

## API Reference (Revised)

Helicone provides a unified API interface that is compatible with the OpenAI API format. This single interface replaces the need for separate APIs for each LLM provider.

### External APIs Consumed

The Helicone AI Gateway will consume APIs from various LLM Providers, as configured.

### Internal APIs Provided

Helicone provides its own internal API for configuration and its dashboard. The details are abstracted by the product itself.

## Data Models (Revised)

Helicone manages its own internal data models for requests, virtual keys, and prompts. We will not need to define or manage these schemas manually. The core entities we will interact with conceptually remain:

- **LLMRequest:** A request made to an LLM, now with all metadata (cost, tokens, latency) collected automatically by Helicone.

- **VirtualKey:** Represents an abstraction over raw LLM provider API keys, managed within the Helicone dashboard.

- **PromptTemplate / PromptPartial:** Reusable templates/segments, managed by Helicone's prompt management features.

## Core Workflow / Sequence Diagrams (Revised)

This diagram illustrates the new, simplified core request flow through the Helicone AI Gateway.

```text
sequenceDiagram
    actor A as User/Application
    participant H as Helicone AI Gateway
    participant P as LLM Provider
    participant D as Helicone Dashboard
    A->>H: LLM Request (using Helicone URL)
    H->>H: 1. Apply Virtual Key rules
    H->>H: 2. Check Cache
    alt Cache Hit
        H-->>A: Cached Response
        H->>D: Log Cache Hit
    else Cache Miss
        H->>H: 3. Select Best Model (Intelligent Router)
        H->>P: Forward Request to Provider
        P-->>H: LLM Response
        H->>H: 4. Log Metrics, Traces, Cost
        H-->>A: Final Response
    end
    H->>D: Real-time data sync
    Note over D: User views analytics in dashboard
```

*Description: This sequence diagram details the streamlined journey of an LLM request from the User/Application through the single Helicone proxy. It highlights the internal steps of virtual key application, caching, and intelligent routing. All request data is automatically sent to the Helicone Dashboard.*

## Definitive Tech Stack Selections (Revised)

This table outlines the new definitive technology choices for the project.

| Category           | Technology                                | Version / Details                                 | Description / Purpose                                                                                    |
| :----------------- | :---------------------------------------- | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------- |
| **Core Gateway**   | Helicone AI Gateway                       | Latest open-source release                        | The core engine, handling all routing, caching, and observability. Built with Rust for high performance. |
| **Languages**      | N/A                                       | We do not need to write code for the core gateway | The gateway is a single, self-contained binary.                                                          |
| **Databases**      | PostgreSQL / Redis                        | Latest stable                                     | Optional but recommended for Helicone's dashboard and caching data persistence.                          |
| **Cloud Platform** | AWS / GCP / Cloudflare / Fly.io / Railway | N/A                                               | Flexible deployment across all specified cloud providers.                                                |
| **Infrastructure** | Docker                                    | Latest stable                                     | Containerization for easy deployment.                                                                    |
|                    | Kubernetes / Kuma                         | Latest stable                                     | Orchestration for production scale.                                                                      |
|                    | Infrastructure as Code (IaC)              | (Tool to be selected)                             | Automated infrastructure provisioning.                                                                   |
| **UI**             | Helicone Built-in Dashboard               | N/A                                               | Provides all necessary analytics and configuration UI. This replaces the custom Next.js application.     |
| **Testing**        | Helicone's built-in tests                 | N/A                                               | We will rely on the comprehensive testing provided by the Helicone project itself.                       |
|                    | Manual E2E tests                          |                                                   | To verify our configuration and deployment.                                                              |
| **CI/CD**          | GitHub Actions                            | N/A                                               | For deploying our infrastructure and configurations.                                                     |

## Infrastructure and Deployment Overview (Revised)

- **Cloud Provider(s):** The architecture is designed for multi-cloud compatibility.

- **Infrastructure as Code (IaC):** A robust IaC tool will be used to define and manage all infrastructure components (Docker, Kubernetes manifests) for the Helicone Gateway and its database.

- **Deployment Strategy:** A fully automated CI/CD pipeline will support frequent deployments. The strategy will involve containerization (Docker) and orchestration (e.g., Kubernetes). Blue/Green or Canary deployments will be considered.

## Error Handling Strategy (Revised)

We will rely on Helicone's built-in error handling. Helicone's gateway handles transient failures with retries and fallbacks. All errors are automatically logged and available in the dashboard. Our strategy now focuses on configuring Helicone's robust features rather than building them from scratch.

## Coding Standards (Revised)

As the core gateway is a self-contained binary, we will not be writing any Python or TypeScript code for the core functionality. Our coding standards will now apply primarily to our IaC and any custom scripts we may need to write for deployment and testing.

## Overall Testing Strategy (Revised)

We will now rely on Helicone's internal testing for its core functionality. Our testing efforts will focus on:

- **Configuration Verification:** Ensuring our deployed Helicone instance is configured correctly and communicates properly with its database and LLM providers.

- **End-to-End (E2E) Tests:** Sending test requests through the deployed gateway to verify that intelligent routing, caching, and fallbacks work as expected.

## Security Best Practices (Revised)

We will rely on Helicone's security features, including its handling of API keys and built-in LLM security guardrails. Our focus will be on securely managing our environment variables and ensuring our IaC is configured correctly to align with our security policies.

## Key Reference Documents (Revised)

- [AI Gateway Project Brief](https://www.google.com/search?q=project-brief.md)

- [Helicone AI Gateway GitHub](https://github.com/Helicone/ai-gateway)

- [Helicone AI Gateway Documentation](https://docs.helicone.ai/gateway/overview)

