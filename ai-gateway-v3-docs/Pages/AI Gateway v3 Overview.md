---
type: Page
title: AI Gateway v3 Overview
description: null
icon: null
createdAt: '2025-09-18T10:58:14.833Z'
creationDate: 2025-09-18 05:58
modificationDate: 2025-09-18 05:59
tags: []
coverImage: null
---

---

## Helicone as a Consolidated Solution

- **Unified API & Routing:** Helicone provides an OpenAI-compatible API that unifies access to over 100 LLM providers. Its built-in intelligent routing, which is both health-aware and rate-limit aware, directly replaces the primary functions of **Portkey**, **LiteLLM**, and **Not Diamond**.

- **Observability:** Helicone was initially designed as an observability platform. It offers native logging, metrics, tracing, and a comprehensive dashboard. This functionality fully replaces the need for the separate `Observability Service` and a custom Next.js dashboard, which would have been built to display data that Helicone already collects.

- **Deployment Simplicity:** Helicone is a single, high-performance Rust binary. This simplifies our deployment strategy significantly and eliminates the complex multi-service architecture that would have been required to integrate Kong, Portkey, LiteLLM, and a custom router and observability service.

---

Given this consolidation of functionality into a single component, the original plan is no longer valid. I will now proceed with a full system re-design to align with the new, simplified architecture. I will start by updating the core documentation, beginning with the Product Requirements Document (PRD).

---
