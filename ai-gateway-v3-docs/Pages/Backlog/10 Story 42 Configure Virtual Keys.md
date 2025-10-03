---
type: Page
title: '10. Story 4.2: Configure Virtual Keys'
description: null
icon: null
createdAt: '2025-09-18T12:38:08.127Z'
creationDate: 2025-09-18 07:38
modificationDate: 2025-09-18 07:38
tags: []
coverImage: null
---

---

### 10. Story 4.2: Configure Virtual Keys

# Story 4.2: Configure Virtual Keys

## Status: Draft

## Story

- As a **developer**,

- I want to **create and manage virtual keys in the Helicone dashboard**,

- so that **I can abstract away raw LLM provider API keys and apply per-key configurations**.

## Acceptance Criteria (ACs)

1. A new virtual key is successfully created in the Helicone dashboard.

2. The virtual key is configured to map to an underlying LLM provider's API key.

3. The virtual key is associated with a specific configuration, such as a rate limit.

4. A test request using the new virtual key successfully routes to the correct provider and adheres to the configured rate limit.

5. Helicone's Dashboard metrics track usage and cost specifically by the virtual key.

## Tasks / Subtasks

- [ ] Research how to create virtual keys in the Helicone dashboard.

- [ ] Navigate to the Helicone dashboard and create a new virtual key.

- [ ] Configure the virtual key to use one of the LLM providers from Story 1.2.

- [ ] Apply a rate limit to the virtual key (e.g., 5 requests per minute).

- [ ] Modify a test script to use the new virtual key in the `Authorization` header instead of a raw provider key.

- [ ] Send multiple test requests to verify the rate limit is enforced.

- [ ] Confirm in the Helicone Dashboard that all requests are being tracked under the new virtual key.

- [ ] Document the process for creating and configuring virtual keys in the main `README.md`.

## Dev Technical Guidance

This story is crucial for enabling secure, fine-grained access control and cost management. Helicone's built-in virtual key management simplifies this process from a custom-coded service to a configuration task.

- **Dependencies:** This story **depends on Story 1.1: Deploy Helicone AI Gateway** and **Story 1.2: Configure LLM Providers**.

- **Technology Stack:** Helicone AI Gateway. We will interact with its dashboard for configuration.

- **Security:** This is a high-security story. The goal is to avoid distributing raw provider API keys.

- **Testing:** Test for both success and failure scenarios (e.g., a request that hits the rate limit).

- **References:**

    - Helicone AI Gateway Documentation: [https://docs.helicone.ai/features/advanced-usage/virtual-keys](https://www.google.com/search?q=https://docs.helicone.ai/features/advanced-usage/virtual-keys)

---
