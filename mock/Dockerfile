FROM python:3.12-slim
WORKDIR /srv
RUN pip install --no-cache-dir "fastapi>=0.115" "uvicorn>=0.30"
COPY erp.py .
EXPOSE 9000
CMD ["uvicorn", "erp:app", "--host", "0.0.0.0", "--port", "9000"]
