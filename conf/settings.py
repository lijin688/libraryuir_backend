import os
import sys
import datetime
from dotenv import load_dotenv

# load_dotenv('/data/webapps/appenv')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
CONFIG_NAME = 'test'

DATABASE_CONFIG = {
            "drivername": "mysql",
            "username": "root",
            "password": "xxx",
            "host": "localhost",
            "port": "3306",
            "database": "libraryuir"
        }

SQLALCHEMY_ECHO = False

# log
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s %(name)s %(module)s %(lineno)d : %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s [%(pathname)s:line:%(lineno)d] %(message)s'
        },
        'elk': {
            'format': '%(asctime)s [%(name)s] [%(threadName)s] %(levelname)s [%(pathname)s:line:%(lineno)d] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'verbose',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'uir.log'),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 8,
            'formatter': 'elk',
        },

    },
    'loggers': {
        'tamias': {
            'handlers': ['file', 'console', 'error'],
            'level': 'DEBUG',
        },
    }
}

