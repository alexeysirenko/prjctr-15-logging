FROM python:3.9

RUN apt-get update
RUN apt-get install -y curl siege
RUN rm -rf /var/lib/apt/lists/*

COPY urls.txt /siege/urls.txt

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
