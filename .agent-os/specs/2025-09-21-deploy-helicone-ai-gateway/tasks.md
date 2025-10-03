# Spec Tasks

## Tasks

- [x] 1. Create `apps/ai-gateway/infra/` directory and `docker-compose.yml`
    - [x] 1.1 Create the `apps/ai-gateway/infra/` directory.
    - [x] 1.2 Create the `docker-compose.yml` file in the `apps/ai-gateway/infra/` directory.
    - [x] 1.3 Define the `helicone-gateway` service in the `docker-compose.yml` file.
    - [x] 1.4 Define the `postgres` service in the `docker-compose.yml` file.

- [x] 2. Create `.env.example` and `README.md`
    - [x] 2.1 Create the `.env.example` file in the `apps/ai-gateway/infra/` directory.
    - [x] 2.2 Define the environment variables for the `helicone-gateway` and `postgres` services in the `.env.example` file.
    - [x] 2.3 Create the `README.md` file in the `apps/ai-gateway/infra/` directory.
    - [x] 2.4 Document the deployment steps in the `README.md` file.

- [x] 3. Deploy and verify
    - [x] 3.1 Run `docker-compose up` from the `apps/ai-gateway/infra` directory to deploy the services.
    - [x] 3.2 Verify that the `helicone-gateway` service is running.
    - [x] 3.3 Verify that the `postgres` service is running.
    - [x] 3.4 Verify that the Helicone dashboard is accessible in a web browser.
    - [x] 3.5 Verify that the gateway is accessible via `curl`.
