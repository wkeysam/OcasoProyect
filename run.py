import os
from app import create_app

env = os.getenv("APP_ENV", "development")   # dev por defecto
app = create_app(env)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
