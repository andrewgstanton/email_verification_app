FROM python:3.10-slim
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Explicit permissions setup
RUN mkdir -p /app/data && chmod -R 777 /app/data

ENV FLASK_APP=app.py

EXPOSE 5000
CMD ["python", "-u", "app.py"]