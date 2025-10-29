FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY templates ./templates
COPY config ./config
COPY backend/server.py ./server.py
ENV FLASK_APP=server.py
EXPOSE 5000
CMD ["python", "server.py"]
