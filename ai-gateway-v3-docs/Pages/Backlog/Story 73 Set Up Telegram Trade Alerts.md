---
type: Page
title: 'Story 7.3: Set Up Telegram Trade Alerts'
description: null
icon: null
createdAt: '2025-09-19T12:22:36.944Z'
creationDate: 2025-09-19 07:22
modificationDate: 2025-09-19 07:22
tags: []
coverImage: null
---

### **Story 7.3: Set Up Telegram Trade Alerts**

- **As a trader,** I want to receive a notification on Telegram whenever a trade is executed on my behalf,

- **so that** I am always aware of my account activity.

- **Acceptance Criteria:**

    1. The "Settings" page allows the user to securely connect their Telegram account.

    2. The backend contains a notification service that listens for filled trade events from the `ExecutionAgent`.

    3. Upon a filled trade, the service sends a formatted, non-interactive message to the user's Telegram.

    4. The message contains the essential details of the trade (e.g., "EXECUTED: BUY 1 BTC/USD at $50,000.00").

