# py_logger
[![PyPI Downloads](https://static.pepy.tech/badge/json-dev-logger)](https://pepy.tech/projects/json-dev-logger)  
[![Snyk Vulnerability Database report](https://snyk.io/advisor/images/snyk-poweredby.svg)](https://security.snyk.io/package/pip/json-dev-logger)  

Project homepage is https://github.com/Areso/py_logger

## Why?

I like to tinker things, and while I am writing the code, I am also the person who runs the code as well. This why I made this small library to gather enriched logs from my Python-powered projects. The enriched data includes name of the repo, branch, manually modified files (when debugging I could change something with my barehands right on a server, where my projects run)

## Installation through PyPi
`pip3 install json-dev-logger`  
in a project:  
```
from py_logger import setup_logger

logger = setup_logger()
logger.info("test")
```  

example of a record:  
```
{"level": "INFO", 
 "time": "2025-03-26 19:48:07,797", 
 "message": "test", 
 "name": "jsonLogger", 
 "filename": "1.py", 
 "lineno": 4, 
 "pathname": "/home/username/git/py_logger/1.py", 
 "hostname": "devserver-24",
 "reponame": "py_logger", 
 "branch": "master", 
 "modified_files": " M README.md"}
```
