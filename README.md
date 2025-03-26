# py_logger

## installation through PyPi
`pip3 install json-dev-logger`  
in a project:  
```
import py_logger

mylogger = py_logger.setup_logger()
mylogger.info("test")
```  

example of a record:  
```
{"level": "INFO", 
 "time": "2025-03-26 19:48:07,797", 
 "message": "test", 
 "name": "jsonLogger", 
 "filename": "1.py", 
 "lineno": 4, 
 "pathname": "/home/username/git/dbaas/py_logger/1.py", 
 "reponame": "py_logger\n", 
 "branch": "* master\n", 
 "modified_files": " M README.md\n"}
```

## locally:  
to add:  
```
git submodule add git@github.com:Areso/py_logger.git
git submodule update --init
```  

to update:  
```
git submodule update --remote
git commit -am "Upgraded dependency"
```
to downgrade:  
```
cd path/to/submodule_dir/within/the?repo
git reset --hard <commit_hash_or_tag>
cd ..
git commit -am "Downgraded dependency"
git push
```

on a remote:  
```
git submodule init
git submodule update --init
```

## to use inside your code
```
from py_logger.py_logger import setup_logger
...

logger_c = setup_logger()
logger_c.info("Program has started")
```
