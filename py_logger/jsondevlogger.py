import logging
import json
import subprocess

def execute_command(command, timeout=10):
    try:
        # Execute the command
        result = subprocess.run(command,
                                shell=True,
                                capture_output=True,
                                text=True,
                                timeout=timeout)        
        # Get output and return code
        output = result.stdout
        error  = result.stderr
        rc     = result.returncode
        return output, error, rc
    except subprocess.TimeoutExpired as e:
        return None, f"Command timed out after {timeout} seconds", -1
    except Exception as e:
        return None, str(e), -1

def get_reponame():
    command = "basename -s .git `git config --get remote.origin.url`"
    output, err, rc = execute_command(command)
    if rc==0:
        return output
    else:
        return "cannot get a git repo name"

def get_branch():
    command = "git branch"
    output, err, rc = execute_command(command)
    if rc==0:
        return output
    else:
        return "cannot get a git repo branch"

def get_modified_files():
    command = "git status -s | grep M"
    output, err, rc = execute_command(command)
    if rc==0:
        return output
    else:
        return "NONE"

class JSONFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()
        self.branch         = get_branch()
        self.modified_files = get_modified_files()
        self.reponame       = get_reponame()
    def format(self, record):
        # Create a dictionary for log record attributes
        log_record = {
            'level':    record.levelname,
            'time':     self.formatTime(record),
            'message':  record.getMessage(),
            'name':     record.name,
            'filename': record.filename,
            'lineno':   record.lineno,
            'pathname': record.pathname,
            'reponame': self.reponame,
            'branch':   self.branch,#get_branch(),
            'modified_files': self.modified_files # get_modified_files()
        }
        # Add additional info if needed (e.g., exception info)
        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)        
        return json.dumps(log_record)
    

# Setup the logger
def setup_logger():
    logger_c = logging.getLogger('jsonLogger')
    if not logger_c.hasHandlers():  # Avoid adding handlers multiple times
        stream_handler = logging.StreamHandler()
        file_handler   = logging.FileHandler('json.log.json', mode='a') 
        stream_handler.setFormatter(JSONFormatter())
        file_handler.setFormatter(JSONFormatter())
        logger_c.addHandler(stream_handler)
        logger_c.addHandler(file_handler)
        logger_c.setLevel(logging.DEBUG)
    return logger_c