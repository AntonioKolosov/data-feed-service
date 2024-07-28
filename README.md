# Data feed service

```
A data feed is an ongoing stream of structured data that provides users   
with updates of current information from one or more sources.    
A data feed can stream continuously or be delivered on demand.    
Data feeds make it possible to have new content or updates delivered to    
a computer or mobile device as soon as it is published.    
The same technologies are also used to supply data to other software.  
   
A data feed is an online mechanism for sending up-to-date data or content   
to users, either automatically or in response to users' demands.    
This data is usually structured and sent from a server to a specific destination,   
such as a website or mobile phone app.   
```

## Project structure
``` bash
├── README.md
├── .gitignore
├── .github
│   └── workflows
│       └── publish.yaml
├── .pre-commit-config.yaml
├── src
│   ├── app.py
│   ├── config.py
│   ├── description.py
│   ├── loader.py
│   ├── notifier.py
│   └── router.py
├── static
│   ├── prompter
│   │    ├── chat.js
│   │    ├── dom-utils.js
│   │    ├── index.html
│   │    ├── selectors.js
│   │    ├── style.css
│   │    └── web-utils.js
│   └── viewer
│       ├── chat.js
│       ├── dom-utils.js
│       ├── index.html
│       ├── selectors.js
│       ├── style.css
│       └── web-utils.js
├── main.py
├── pytest.ini
├── requirements.txt
├── requirements_dev.txt
└── tests
    ├── __init__.py
    └── test_app.py
```

### Setup the project for the development
For this project will be installed:
* [fastapi](https://fastapi.tiangolo.com/) - popular framework for API's
* [flake8](https://flake8.pycqa.org/en/latest/) - for linting
* [httpx](https://www.python-httpx.org/) -  HTTP client for Python 3
* [pip](https://pypi.org/project/pip/) - for install packages
* [pipdeptree](https://pypi.org/project/pipdeptree/) - for sorting packages
* [pre-commit](https://pre-commit.com/) - Git hook scripts are useful for identifying simple issues before submission to code review.
* [pyngrok](https://pypi.org/project/pyngrok/) - a reverse proxy tool that opens secure tunnels from public URLs to localhost
* [pytest](https://docs.pytest.org/en/7.3.x/) - for unit tests
* [python-dotenv](https://pypi.org/project/python-dotenv/) - for reading .env files
* [uvicorn](https://www.uvicorn.org/) - an ASGI web server implementation for Python.

### Create virtual environment
```bash
python3 -m venv .dfsrvvenv
```

### Install dependencies
```bash
pip install -r requirements_dev.txt
```

### Run (localy)
```bash
python main.py [port]
```

### Check from browser
```bash
1. http://127.0.0.1:8005/
```
Hello I am your Bot
```

### Linting
```bash
flake8 -v --max-line-length=79 --max-doc-length=72 --ignore=E203,W503 ./src
```

### Unit testing
```bash
pytest
```

### Build the docker file 
```bash
docker build . --tag ghcr.io/antoniokolosov/data-feed-service-aarch64:1.0.0
```

### Publish to the Github registry
```bash
docker login -u <your-github-username> ghcr.io
docker push ghcr.io/antoniokolosov/data-feed-service-aarch64:1.0.0
``` 

### Build and publish to the Github registry the docker file for x64 architecture
```
from GitHub repository run the publish action
```
