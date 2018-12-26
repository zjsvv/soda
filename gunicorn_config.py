# Specifying this configuration while starting gunicorn
# gunicorn -c gunicorn_config.py soda.wsgi 

# The socket to bind.
bind = '0.0.0.0:8000'

# The granularity of Error log outputs.
# Valid level names are: debug, info, warning, error, critical 
loglevel = 'debug'

# The Error log file to write to.
# Using '-' for FILE makes gunicorn log to stderr.
errorlog = '-'

# The Access log file to write to.
# '-' means log to stdout.
accesslog = '-'

# The suggested number of workers is (2*CPU)+1
workers = 2

# Load application code before the worker processes are forked.
preload = True

# Restart workers when code changes.
# This setting is intended for development. 
# It will cause workers to be restarted whenever application code changes.
reload = True

# async type worker, so the app can handle a stream of requests in parallel
worker_class = 'gevent'  
