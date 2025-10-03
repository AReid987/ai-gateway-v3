---
type: Page
title: '5. Story 1.2: Configure LLM Providers'
description: null
icon: null
createdAt: '2025-09-18T12:35:28.793Z'
creationDate: 2025-09-18 07:35
modificationDate: 2025-09-18 07:37
tags: []
coverImage: null
---

### 5. Story 1.2: Configure LLM Providers

# Story 1.2: Configure LLM Providers

## Status: Draft

## Story

- As a **developer**,

- I want to **configure at least two LLM providers (e.g., OpenAI, Anthropic) within Helicone**,

- so that **the gateway can route requests to them**.

## Acceptance Criteria (ACs)

1. The Helicone Gateway is configured to use at least two LLM providers (e.g., OpenAI, Anthropic).

2. Requests sent through the gateway are successfully routed to the specified providers.

3. The Helicone Dashboard displays usage and metrics for both configured providers.

4. Local testability: A `curl` command or a simple script can be used to send test requests that demonstrate successful routing to both providers.

## Tasks / Subtasks

- [ ] Obtain API keys for at least two LLM providers.

- [ ] Add the API keys to Helicone's environment variables.

- [ ] Modify the `docker-compose.yml` or Kubernetes manifests to pass the environment variables to the Helicone container.

- [ ] Send a test request to the gateway specifying the OpenAI provider.

- [ ] Send a test request to the gateway specifying the Anthropic provider.

- [ ] Verify that both requests are routed correctly and that metrics appear in the Helicone Dashboard.

- [ ] Document how to configure new providers in the `infra/` directory's `README.md`.

## Dev Technical Guidance

This story verifies the core routing functionality of Helicone, ensuring it can successfully abstract the underlying LLM providers.

- **Dependencies:** This story **depends on Story 1.1: Deploy Helicone AI Gateway**.

- **Technology Stack:** Helicone AI Gateway.

- **Security:** Ensure API keys are handled securely via environment variables and never hardcoded.

- **References:**

    - Helicone AI Gateway Documentation: [https://docs.helicone.ai/gateway/provider-routing](https://docs.helicone.ai/gateway/provider-routing)

## Story Progress Notes

### Agent Model Used: Fiona "Flux" Rivera (SM Agent)

### Completion Notes List

{To be filled by Developer Agent upon completion}

### Change Log

- Initial Draft | 2025-09-18 | Fiona "Flux" Rivera (SM Agent)

