FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim
WORKDIR /app/
COPY ./app /app
RUN RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
ENV PYTHONPATH=/app