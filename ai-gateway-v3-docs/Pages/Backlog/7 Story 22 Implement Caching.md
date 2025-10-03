---
type: Page
title: '7. Story 2.2: Implement Caching'
description: null
icon: null
createdAt: '2025-09-18T12:36:12.827Z'
creationDate: 2025-09-18 07:36
modificationDate: 2025-09-18 07:37
tags: []
coverImage: null
---

### 7. Story 2.2: Implement Caching

# Story 2.2: Implement Caching

## Status: Draft

## Story

- As a **developer**,

- I want to **enable and configure Helicone's caching feature**,

- so that **repeat requests are served from the cache, reducing cost and latency**.

## Acceptance Criteria (ACs)

1. Helicone's caching feature is enabled via an HTTP header.

2. A test request successfully misses the cache on the first attempt and hits the cache on the second, identical attempt.

3. The second request is served with significantly lower latency than the first.

4. Helicone's Dashboard metrics confirm a cache hit and the associated cost savings.

5. Caching is configured to use an external Redis instance for persistence.

## Tasks / Subtasks

- [ ] Modify the `docker-compose.yml` to include a Redis service and configure Helicone to connect to it.

- [ ] Add the `cache` section to the Helicone `config.yaml` to specify Redis as the storage backend.

- [ ] Add the `Helicone-Cache-Enabled: "true"` header to a test request.

- [ ] Send an LLM request through the gateway and note the response time.

- [ ] Send the exact same request again and verify that the response is returned from the cache with a lower latency.

- [ ] Check the Helicone Dashboard to confirm the cache hit and that no cost was incurred on the second request.

- [ ] Document the caching configuration and how to test it in the `infra/` directory's `README.md`.

## Dev Technical Guidance

This story implements a key cost-saving and performance-boosting feature. Helicone handles the caching logic internally; our job is to enable and configure it correctly.

- **Dependencies:** This story **depends on Story 1.1: Deploy Helicone AI Gateway**.

- **Technology Stack:** Helicone AI Gateway, Redis.

- **Configuration:** Caching is enabled via request headers and can be configured globally in `config.yaml` to use an external storage backend like Redis for long-term persistence.

- **Testing:** The primary test will involve two identical `curl` commands to demonstrate the cache hit.

- **References:**

    - Helicone AI Gateway Documentation: [https://docs.helicone.ai/features/advanced-usage/caching](https://docs.helicone.ai/features/advanced-usage/caching)

## Story Progress Notes

### Agent Model Used: Fiona "Flux" Rivera (SM Agent)

### Completion Notes List

{To be filled by Developer Agent upon completion}

### Change Log

- Initial Draft | 2025-09-19 | Fiona "Flux" Rivera (SM Agent)

