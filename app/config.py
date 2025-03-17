class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://mac:1234@postgres_db:5432/AirQualityMonitorDB'
    JWT_SECRET_KEY = 'secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
