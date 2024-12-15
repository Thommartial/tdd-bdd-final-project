"""
Global Configuration for Application
"""
# ALTER USER postgres PASSWORD 'Postres2024#';
# export DATABASE_URI="postgresql://postgres:Postres2024#@localhost:5432/postgres"


import os
import logging

# Get configuration from environment
DATABASE_URI = os.getenv(
    "DATABASE_URI",
    "postgresql://postgres:Postres2024#@localhost:5432/postgres"
)

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_POOL_SIZE = 2

# Secret for session management
SECRET_KEY = os.getenv("SECRET_KEY", "sup3r-s3cr3t")
LOGGING_LEVEL = logging.INFO


# import os
# import logging

# # Get configuration from environment
# DATABASE_URI = os.getenv(
#     "DATABASE_URI",
#     "postgresql://postgres:postgres@localhost:5432/postgres"
# )

# # Configure SQLAlchemy
# SQLALCHEMY_DATABASE_URI = DATABASE_URI
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# # SQLALCHEMY_POOL_SIZE = 2

# # Secret for session management
# SECRET_KEY = os.getenv("SECRET_KEY", "sup3r-s3cr3t")
# LOGGING_LEVEL = logging.INFO
