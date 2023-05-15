import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgres://daviddb:cAkLkSNCgT8nyLwVV1Ggd5LFZARkTgJX@dpg-ch9tcd6si8uqs8mo7nh0-a.oregon-postgres.render.com/daviddb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
