# filepath: /Users/johnnycheng/projects/python_ms/README.md
# Python Microservice

A simple Python microservice that prints "hello Johnny".

## Getting Started

### Prerequisites
- Python 3.9+
- Docker (optional)

### Installation

1. Clone the repository
2. Install dependencies:
```
python -m pip install -r requirements.txt
```

### Running the service

Run directly with Python:
```
python app.py
```

Or with Gunicorn:
```
gunicorn --bind 0.0.0.0:5000 app:app
```

### Using Docker

Build the Docker image:
```
docker build -t python-ms .
```

Run the container:
```
docker run -p 5000:5000 python-ms
```

## API Endpoints

- `GET /`: Returns "hello Johnny" message
- `GET /health`: Health check endpoint