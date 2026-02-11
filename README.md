# FinPilot

FinPilot is a financial analysis agent powered by Retrieval-Augmented Generation (RAG) and specialized sub-agents. It provides an API to ingest financial documents, extract structured data, and perform complex queries using a supervisor agent that coordinates between semantic retrieval and SQL database operations.

## Features

- **Document Ingestion:** Automated pipeline to parse financial documents, extracting text and tables.
- **Financial Fact Extraction:** Identifies and extracts key financial facts and metrics from unstructured text.
- **Hybrid Retrieval:** Combines vector-based semantic search with SQL-based structured data querying.
- **Supervisor Agent:** A high-level orchestration agent that delegates queries to the most appropriate sub-agent.
- **REST API:** Built with FastAPI for easy integration.

## Architecture

The system is built using:
- **LangGraph:** For stateful, multi-agent workflows (Ingestion, Retrieval, Supervisor).
- **FastAPI:** For the web server and API endpoints.
- **PostgreSQL:** For structured data storage.
- **Chroma:** For vector embeddings and semantic search.

## Prerequisites

- Python 3.13+
- PostgreSQL
- `uv` for dependency management.

## Installation

1. Clone the repository.

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your specific configuration. See `.env.example` for the required variables:
   - **LangSmith Configuration** (`LANGSMITH_TRACING`, `LANGSMITH_ENDPOINT`, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT`)
   - **Google API** (`GOOGLE_API_KEY`, `USER_AGENT`)
   - **LLM Provider** (`GROQ_API_KEY`)
   - **Database** (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`)

## Usage

### Development Server (FastAPI)

Start the FastAPI development server:

```bash
uv run fastapi dev
```

The API will be available at `http://localhost:8000`.
Interactive documentation: `http://localhost:8000/docs`.

### LangGraph Studio



Launch the LangGraph development studio for visual workflow debugging:



```bash

uv run langgraph dev

```



## Docker Support



You can run the application using Docker:



1. Build the image:

   ```bash

   docker build -t finpilot .

   ```



2. Run the container:

   ```bash

   docker run --env-file .env -p 8000:8000 finpilot

   ```
