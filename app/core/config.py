from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str = 'Social network'
    DB_TYPE: str
    DB_DRIVER: str
    DB_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    SECRET: str
    EMAIL_HUNTER_KEY: str

    class Config:
        env_file = '.env'

    @property
    def db_url(self):
        return (
            f'{self.DB_TYPE}+{self.DB_DRIVER}://'
            f'{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}'
            f'@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        )


settings = Settings()
