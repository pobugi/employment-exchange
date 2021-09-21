from starlette.config import Config

# config = Config(".env")

# DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")

DATABASE_URL="postgresql://postgres:postgres@localhost:5432/employment_exchange"
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM = "HS256"
SECRET_KEY="fa78e009f4e9e7c01286badccbb4d77c96ae92d6fc6235d6df1aa427206123f8"