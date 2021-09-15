from starlette.config import Config

# config = Config(".env")

# DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")

DATABASE_URL="postgresql://postgres:postgres@localhost:5432/employment_exchange"
