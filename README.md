# GitHub Actions Practice

This is a simple project to practice the basics of GitHub Actions.

## What's Included

A FastAPI application with a health check endpoint, plus several GitHub Actions workflows demonstrating different concepts:

- **CI Workflow** (`ci.yml`) - Runs health checks on the FastAPI server
- **Workflow Variables** (`workflow_variables.yml`) - Shows how to use variables at workflow, job, and step levels
- **Config Variables** (`config_variables.yml`) - Demonstrates using repository-level variables
- **Context Variables** (`context_varibales.yml`) - Examples of GitHub's built-in context variables
- **User Input** (`user_input.yml`) - Workflow that accepts manual inputs via `workflow_dispatch`

## Running Locally

```bash
uv sync
uv run python main.py
```

Visit `http://localhost:8000/health` to check if the server is running.
