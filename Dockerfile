# app/Dockerfile

FROM python:3.9-slim
WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt
RUN python -m pip install prophet
RUN pip install db-dtypes
RUN pip install --upgrade db-dtypes
EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]