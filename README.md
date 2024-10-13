# py_logger

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
