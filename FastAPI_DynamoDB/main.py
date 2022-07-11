import uvicorn
from fastapi import FastAPI
from database.db import create_tables
from routes.song import routes_song
from pathlib import Path
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)

app.include_router(routes_song, prefix="/song")

create_tables()

if __name__ == "__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000, debug=True, env_file=".env")