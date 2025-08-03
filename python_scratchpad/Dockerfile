# Simple starter Dockerfile for a Python project using uv

FROM python:3.13-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv
RUN uv sync
CMD ["uv", "run", "src/main.py"]
