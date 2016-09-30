#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/YouthMusic/")

from YouthMusic import app as application
application.secret_key = 'SET T0 4NY SECRET KEY L1KE RAND0M H4SH'
