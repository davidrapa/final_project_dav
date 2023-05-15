import os

# Database
DB_USERNAME = 'daviddb'
DB_PASSWORD = 'cAkLkSNCgT8nyLwVV1Ggd5LFZARkTgJX'
DB_HOST = 'dpg-ch9tcd6si8uqs8mo7nh0-a.oregon-postgres.render.com'
DB_NAME = 'daviddb'

# Secret Key
SECRET_KEY = '1234'

# Database URIflas
DB_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

# Flask
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', DB_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False
