from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime

def generate_id():

    return str(uuid4())

def generate_date():

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return str(dt_string)

class Song(BaseModel):

    SongId: str = Field(default_factory=generate_id)
    SongTittle: str
    Artist: str
    SongGenre: str
    SongProductionDate: str = Field(default_factory=generate_date)

    LoaderId: str
    LoaderName: str

class DeleteSong(BaseModel):

    SongId: str
    LoaderId: str