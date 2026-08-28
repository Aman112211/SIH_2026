FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DEMO_MODE=true
EXPOSE 5000
CMD ["python", "run.py"]
