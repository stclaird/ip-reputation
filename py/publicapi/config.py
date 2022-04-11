"""
Central Configuration
"""
import os

class General():
    """
    General Configuration
    """
    VERSION = 0.1
    DEBUG: bool = os.environ.get('DEBUG', True)
    SERVICE_NAME: str = "IP Reputation"
    ENV: str = os.environ.get('ENV', 'development')
    API_PREFIX = os.environ.get('API_PREFIX', '/v1')
    SERVER_ENVIRONMENT = os.environ.get('SERVER_ENVIRONMENT', 'localhost')

class Database():
    """
    DB Settings
    """
    DB_URL = os.environ.get('DB_URL', "localhost")
    DB_NAME = os.environ.get('DB_NAME', "ip_reputation")