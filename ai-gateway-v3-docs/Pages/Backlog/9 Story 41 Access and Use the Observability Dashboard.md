---
type: Page
title: '9. Story 4.1: Access and Use the Observability Dashboard'
description: null
icon: null
createdAt: '2025-09-18T12:34:31.379Z'
creationDate: 2025-09-18 07:34
modificationDate: 2025-09-18 07:34
tags: []
coverImage: null
---

### 9. Story 4.1: Access and Use the Observability Dashboard

## Status: Draft

## Story

- As a **developer**,

- I want to **access the Helicone dashboard to view logs, metrics, and traces**,

- so that **I can monitor system health, performance, and costs in real-time**.

## Acceptance Criteria (ACs)

1. The Helicone dashboard is accessible via a web browser (e.g., at `http://localhost:3000`).

2. The dashboard displays a live feed of requests made to the gateway.

3. Metrics such as latency, cost, and token usage are visible on the dashboard.

4. It is possible to drill down into a specific request to view its full trace, including request and response payloads.

5. Logs and metrics for requests made using different providers are correctly separated and visible.

## Tasks / Subtasks

- [ ] Verify that the Helicone Gateway deployment from Story 1.1 includes access to the dashboard.

- [ ] Ensure the `HELICONE_API_KEY` is set correctly to enable observability.

- [ ] Make several test requests to the gateway, varying models and providers.

- [ ] Access the Helicone dashboard in a web browser.

- [ ] Navigate the dashboard to find the Requests tab and confirm that the test requests appear.

- [ ] Verify that key metrics (cost, latency, tokens) are accurately reported on the dashboard.

- [ ] Click on a specific request to view its full trace, including request and response bodies.

- [ ] Document how to access the dashboard and interpret its key metrics in the project's main `README.md`.

## Dev Technical Guidance

This story is about validating Helicone's core value proposition: providing comprehensive observability out of the box. Our task is to confirm that the data we need for monitoring is being collected and displayed correctly.

- **Dependencies:** This story **depends on Story 1.1: Deploy Helicone AI Gateway** and **Story 1.2: Configure LLM Providers**.

- **Technology Stack:** Helicone AI Gateway. We do not need to build any custom UI components for this story.

- **Authentication:** The Helicone dashboard often requires a separate API key for access. This needs to be configured correctly in our environment variables.

- **Observability:** The dashboard is a direct result of the observability features of Helicone. We are simply verifying that our configuration enables and sends data to it.

- **References:**

    - Helicone AI Gateway Documentation: [https://docs.helicone.ai/ai-gateway/observability](https://docs.helicone.ai/ai-gateway/observability)

