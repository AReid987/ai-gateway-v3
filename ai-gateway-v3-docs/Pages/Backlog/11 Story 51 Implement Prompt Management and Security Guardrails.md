---
type: Page
title: '11. Story 5.1: Implement Prompt Management and Security Guardrails'
description: null
icon: null
createdAt: '2025-09-18T12:39:19.392Z'
creationDate: 2025-09-18 07:39
modificationDate: 2025-09-18 07:39
tags: []
coverImage: null
---

---

### 11. Story 5.1: Implement Prompt Management and Security Guardrails

# Story 5.1: Implement Prompt Management and Security Guardrails

## Status: Draft

## Story

- As a **developer**,

- I want to **configure prompt templates and enable security guardrails in Helicone**,

- so that **I can standardize LLM interactions and protect the gateway from malicious inputs**.

## Acceptance Criteria (ACs)

1. A prompt template with dynamic variables is created in the Helicone dashboard.

2. A test request uses the `prompt_id` and `inputs` to successfully apply the template.

3. Helicone's security guardrails feature is enabled via a request header.

4. A test request containing a malicious or insecure prompt is blocked by the gateway.

5. A log of the blocked request and the reason for blocking is visible in the Helicone dashboard.

## Tasks / Subtasks

- [ ] Research Helicone's prompt management and security guardrail features.

- [ ] Navigate to the Helicone dashboard and create a new prompt template with at least one variable (e.g., `{{hc:user_input:string}}`).

- [ ] Obtain the `prompt_id` from the dashboard.

- [ ] Modify a test script to send a request to the gateway using the `prompt_id` and the `inputs` variable.

- [ ] Enable Helicone's LLM security guardrails via the `Helicone-LLM-Security-Enabled: true` header.

- [ ] Create a test prompt designed to trigger a security alert (e.g., a prompt injection attempt).

- [ ] Send the malicious request through the gateway and verify that it is blocked.

- [ ] Confirm that the blocked request is logged in the Helicone dashboard.

- [ ] Document how to use prompt management and enable security guardrails in the main `README.md`.

## Dev Technical Guidance

This story finalizes the core feature set of the gateway, providing a robust, out-of-the-box solution for managing prompts and securing LLM interactions without writing custom code.

- **Dependencies:** This story **depends on Story 1.1: Deploy Helicone AI Gateway**.

- **Technology Stack:** Helicone AI Gateway. We will interact with its dashboard for configuration.

- **Security:** This is a high-security story. The goal is to test Helicone's native guardrails against malicious prompts.

- **Testing:** The primary test for this story is a negative test, where a request is intentionally crafted to be blocked.

- **References:**

    - [Helicone Prompts](https://www.youtube.com/watch?v=pJAn6hoQJDc)

This video provides a practical guide on how to create and manage prompts using the Helicone dashboard.
[http://googleusercontent.com/youtube_content/0](http://googleusercontent.com/youtube_content/0)

