# Simple starter Dockerfile for a Python project using uv

FROM ghcr.io/astral-sh/uv:python3.13-bookworm
WORKDIR /app
COPY pyproject.toml uv.lock README.md ./
RUN uv sync
CMD ["uv", "run", "src/main.py"]
