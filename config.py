import os


class Config:
    # DB_NAME: str = 'db_name'
    # DB_USER: str = 'db_user'
    # DB_PASSWORD: str = 'db_password'
    # DB_HOST: str = 'db'
    DB_NAME: str = os.getenv('DB_NAME')
    DB_USER: str = os.getenv('DB_USER')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: int = 5432

    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
