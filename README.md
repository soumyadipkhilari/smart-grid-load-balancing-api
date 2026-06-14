#  Smart Grid Load Balancing API

## Features
- Meter Data API
- Load Status API
- Docker Support

## Run Locally

pip install -r requirements.txt
uvicorn main:app --reload

## Run With Docker

docker build -t smart-grid-api .
docker run -d -p 8000:8000 smart-grid-api

## API Docs

http://localhost:8000/docs