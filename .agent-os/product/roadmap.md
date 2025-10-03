# Product Roadmap

## Phase 1: Helicone Gateway Deployment & Core Configuration

**Goal:** Deploy Helicone's AI Gateway and configure the core infrastructure.
**Success Criteria:** The Helicone Gateway is deployed, accessible, and configured to use at least two LLM providers.

### Features

- [ ] Deploy Helicone AI Gateway - Deploy the Helicone AI Gateway as a single Docker container or on Kubernetes. `[M]`
- [ ] Configure LLM Providers - Configure at least two LLM providers (e.g., OpenAI, Anthropic) within Helicone. `[S]`

### Dependencies

- None

## Phase 2: Intelligent Routing & Optimization

**Goal:** Implement dynamic model selection and optimization using Helicone's features.
**Success Criteria:** Requests are successfully routed to the optimal model based on the configured rules, and repeat requests are served from the cache.

### Features

- [ ] Implement Intelligent Routing - Configure intelligent routing rules in Helicone based on criteria like cost, latency, and model health. `[M]`
- [ ] Implement Caching - Enable and configure Helicone's caching feature. `[S]`

### Dependencies

- Phase 1

## Phase 3: Reliability and Fallback

**Goal:** Implement automatic retries and fallbacks for uninterrupted service.
**Success Criteria:** The gateway automatically retries failed requests and falls back to an alternative provider when necessary.

### Features

- [ ] Configure Automatic Retries and Fallbacks - Configure Helicone's built-in retry and fallback mechanisms. `[M]`

### Dependencies

- Phase 1

## Phase 4: Observability and Management

**Goal:** Utilize Helicone's built-in dashboard for monitoring and configuration.
**Success Criteria:** The dashboard displays real-time data, and virtual keys can be created and used.

### Features

- [ ] Access and Use the Observability Dashboard - Access the Helicone dashboard to view logs, metrics, and traces. `[S]`
- [ ] Configure Virtual Keys - Create and manage virtual keys in the Helicone dashboard. `[M]`

### Dependencies

- Phase 1

## Phase 5: Advanced Features

**Goal:** Implement LLM security and prompt management.
**Success Criteria:** A request made through the gateway applies a template and is checked by a security guardrail.

### Features

- [ ] Implement Prompt Management and Security Guardrails - Configure prompt templates and enable security guardrails for requests. `[M]`

### Dependencies

- Phase 1
