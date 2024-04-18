# Precondition prediction API
Precondition prediction API written in Python

## Usage

### Docker Compose example

```yaml
version: '3'
services:
  app:
    restart: always
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 8787:8080
    volumes:
      - <FOLDER WHERE forestModel.joblib IS ACTIVE>:/models
    #   - ./src:/app # If you want to mount the source code for development
```

### Endpoints

- GET: `/predict` - Predict the probability of a precondition. Returns a JSON with the probability of the precondition.
```json
{
  "datetime": "2024-04-18 07:59:51", // Current time in UTC/Zulu
  "prediction": 0.0 //0.0 if airco should not be turned on, 1.0 if airco should be turned on
}
```