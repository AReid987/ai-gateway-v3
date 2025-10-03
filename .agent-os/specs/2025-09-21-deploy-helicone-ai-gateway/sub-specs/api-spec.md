# API Specification

This is the API specification for the spec detailed in @.agent-os/specs/2025-09-21-deploy-helicone-ai-gateway/spec.md

## Endpoints

The Helicone AI Gateway exposes an OpenAI-compatible API endpoint. The exact path of the endpoint will depend on the port mapping defined in the `docker-compose.yml` file.

### `POST /`

**Purpose:** This is the main endpoint for making requests to the LLMs. The gateway will route the request to the appropriate LLM provider based on the request body and the gateway's configuration.

**Request Body:** The request body should be compatible with the OpenAI API format.

**Response:** The response will be the response from the underlying LLM provider.

**Errors:** The gateway will return appropriate error codes if it is unable to process the request or if the underlying LLM provider returns an error.
