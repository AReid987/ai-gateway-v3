---
type: Page
title: 'Story 7.1: Implement Automated Trade Logging'
description: null
icon: null
createdAt: '2025-09-19T12:20:53.570Z'
creationDate: 2025-09-19 07:20
modificationDate: 2025-09-19 07:21
tags: []
coverImage: null
---

## Epic 7: Trading Journal & Telegram Integration

**Goal:** To provide tools for performance tracking, reflection, and on-the-go awareness.

### **Story 7.1: Implement Automated Trade Logging**

- **As a trader,** I want a journal where all my trades (manual and automated) are automatically logged with key details (entry/exit price, size, P&L),

- **so that** I have a complete record of my activity.

- **Acceptance Criteria:**

    1. A "Journal" page is created in the application.

    2. Every trade confirmed by the `ExecutionAgent` is automatically saved as an entry in the database.

    3. The log must include essential data: Symbol, Side (Buy/Sell), Quantity, Entry/Exit Prices, P&L, and Timestamp.

    4. The Journal page displays a chronological table of all automatically logged trades.

