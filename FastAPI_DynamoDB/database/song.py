from .db import dynamodb
from botocore.exceptions import ClientError
from fastapi.responses import JSONResponse
from boto3.dynamodb.conditions import Key

table = dynamodb.Table("Song")

def create_song(song: dict):

    try:
        table.put_item(Item=song)

        return song

    except ClientError as e:

        return JSONResponse(content=e.response["error"], status_code=500)


def get_song(id: str):

    try:
        response = table.query(
            KeyConditionExpression=Key("LoaderId").eq(id)
        )

        return response["Items"]

    except ClientError as e:

        return JSONResponse(content=e.response["error"], status_code=500)


def get_songs():

    try:
        response = table.scan(
            Limit=200,
            AttributesToGet=["SongId", "SongTittle", "Artist", "SongGenre", "SongProductionDate", "LoaderId", "LoaderName"]
        )

        return response["Items"]

    except ClientError as e:

        return JSONResponse(content=e.response["error"], status_code=500)


def delete_song(song: dict):

    try:
        response = table.delete_item(
            Key={
                "LoaderId": song["LoaderId"],
                "SongId": song["SongId"]
            }
        )

        return response

    except ClientError as e:

        return JSONResponse(content=e.response["error"], status_code=500)


def update_song(song: dict):

    try:
        response = table.update_item(
            Key={
                "LoaderId": song["LoaderId"],
                "SongId": song["SongId"]
            },
            UpdateExpression="SET SongTittle = :SongTittle, Artist = :Artist, SongGenre = :SongGenre, SongProductionDate = :SongProductionDate",
            ExpressionAttributeValues={
                ":Artist": song["Artist"],
                ":SongGenre": song["SongGenre"],
                ":SongProductionDate": song["SongProductionDate"],
                ":SongTittle": song["SongTittle"]
            }
        )

        return response

    except ClientError as e:

        return JSONResponse(content=e.response["error"], status_code=500)
