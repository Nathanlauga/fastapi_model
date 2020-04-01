FastAPI for Machine learning models
-----

by Nathan Lauga.

Inspired by [eightBEC's work](https://github.com/eightBEC/fastapi-ml-skeleton/tree/master/fastapi_skeleton/api).

# Code strucutre

```bash
.
├── api
│   ├── app
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   └── routes
│   │   │       ├── heartbeat.py
│   │   │       ├── __init__.py
│   │   │       ├── prediction.py
│   │   │       └── router.py
│   │   ├── core
│   │   │   ├── config.py
│   │   │   ├── event_handlers.py
│   │   │   ├── __init__.py
│   │   │   ├── messages.py
│   │   │   └── security.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── heartbeat.py
│   │   │   ├── __init__.py
│   │   │   ├── payload.py
│   │   │   ├── prediction.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── model.py
│   │   └── utils
│   │       ├── __init__.py
│   │       └── utils.py
│   └── src
│       └── model.pkl
├── data
│   └── adult.csv
├── docker
│   ├── fastapi
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── jupyter
│       ├── Dockerfile
│       └── requirements.txt
├── docker-compose.yml
├── notebooks
│   └── create_model.ipynb
└── README.md
```