from fastapi import APIRouter
from database.song import create_song, get_song, get_songs
from models.song import Song
from models.song import DeleteSong
from database.song import *

routes_song = APIRouter()

@routes_song.post("/create", response_model=Song)
def create(song: Song):

    return create_song(song.dict())

@routes_song.get("/get/{id}")
def get_songId(id: str):

    return get_song(id)

@routes_song.get("/all")
def get_all_song():

    return get_songs()

@routes_song.delete("/delete")
def delete(song: DeleteSong):

    return delete_song(song.dict())

@routes_song.put("/update")
def update(song: Song):

    return update_song(song.dict())