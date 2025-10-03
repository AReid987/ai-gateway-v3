
# Spec: Add cz-git (czg) with AI-Powered Commit Messages

**Author:** Gemini
**Date:** 2025-10-01
**Status:** Draft

## 1. Background

To maintain a high-quality and consistent commit history, it is crucial to follow a standardized commit message format. The Conventional Commits specification is a widely accepted standard. `cz-git` (`czg`) is a tool that helps enforce this standard.

Furthermore, with the availability of powerful local Large Language Models (LLMs) through services like Ollama and Nexa, we can automate the process of writing commit messages. `cz-git` supports using AI to generate commit messages based on staged changes, which can significantly improve developer productivity and the quality of commit messages.

This spec details the plan to integrate `cz-git` into our development workflow and configure it to use a local AI model for generating commit messages.

## 2. Goals

- Integrate `commitizen` and the `cz-git` adapter into the project.
- Configure `cz-git` to enforce the Conventional Commits specification.
- Configure `cz-git` to use a local AI model (Ollama or Nexa) to automatically generate commit messages.
- Document the new commit workflow for all contributors.

## 3. Technical Plan

The implementation will involve installing the necessary npm packages, configuring `commitizen` and `cz-git`, and documenting the new workflow.

### 3.1. Installation

We will install `commitizen` and `cz-git` as development dependencies at the root of the monorepo.

```bash
pnpm add -D -w commitizen cz-git
```

### 3.2. Configuration

#### 3.2.1. `package.json`

We will add the following configuration to the root `package.json` to configure `commitizen` to use the `cz-git` adapter and to add a new `commit` script.

```json
{
  "scripts": {
    "commit": "czg"
  },
  "config": {
    "commitizen": {
      "path": "cz-git"
    }
  }
}
```

#### 3.2.2. `.czrc` Configuration File

We will create a `.czrc` file in the root of the project to configure `cz-git`. This file will contain the settings for AI-powered commit messages.

```json
{
  "use-ai": true,
  "ai-prompt": "Generate a commit message for the following changes:",
  "ai-source": "openai",
  "openai-api-key": "YOUR_API_KEY",
  "openai-endpoint": "http://localhost:11434/v1"
}
```

- **`use-ai`**: Enables the AI feature.
- **`ai-prompt`**: The prompt to be used for the AI.
- **`ai-source`**: We will use `"openai"` as the source, as local services like Ollama provide an OpenAI-compatible API.
- **`openai-api-key`**: For local models, this can often be a placeholder string like `"ollama"` or `"nexa"`. This needs to be verified based on the specific local AI provider.
- **`openai-endpoint`**: The endpoint for the local AI model's OpenAI-compatible API. The default for Ollama is `http://localhost:11434/v1`. This should be adjusted for Nexa or other providers if needed.

### 3.3. Model Selection

The configuration will default to using a model available via the Ollama endpoint. The user can specify the model to use when running the commit command or configure it in the `.czrc` file if `cz-git` supports it.

## 4. Task Breakdown

- [ ] Install `commitizen` and `cz-git` dependencies.
- [ ] Update `package.json` with `commitizen` configuration and `commit` script.
- [ ] Create and configure the `.czrc` file for AI-powered commits.
- [ ] Test the `pnpm commit` workflow to ensure it generates a commit message using the local AI model.
- [ ] Document the new commit workflow in the `CONTRIBUTING.md` or a similar guide.

## 5. Future Work

- **Liquid AI Edge Models:** Investigate the integration of `liquid-ai-edge-models` as another AI source. This might require a custom configuration or a feature request to `cz-git` if it's not directly compatible.
- **Model Selection:** Explore options for easily switching between different local models (e.g., via environment variables or command-line flags).
