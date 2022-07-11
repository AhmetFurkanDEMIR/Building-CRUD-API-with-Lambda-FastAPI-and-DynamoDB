from flask import Flask,render_template, session, redirect, url_for, request
from httpx import URL
import requests
from uuid import uuid4
from flask_recaptcha import ReCaptcha
from os import getenv

app = Flask(__name__) 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['RECAPTCHA_SITE_KEY'] = '6LffydYgAAAAAFYE9ZYRR31INacauICpvN4RsXZ0' # <-- Add your site key
app.config['RECAPTCHA_SECRET_KEY'] = '6LffydYgAAAAAHwuNObQB_yra8x4UGXtwld9C48d' # <-- Add your secret key
app.config['RECAPTCHA_THEME'] = "dark"
recaptcha = ReCaptcha(app)

global URl
URl = getenv("URL")

@app.route("/",methods = ["GET","POST"])
def main():

    login = 0

    try:

        session["LoaderId"]
        session["LoaderName"]
        login= 0


    except:

        login = 1        

    try:

        response = requests.get("{}/song/all".format(URl)).json() 

        songs = []
        for i in response:

            songs.append(i)

        return render_template("/index.html", songs=songs, login=login)

    except:

        return render_template("/index.html", login=login)

@app.route("/create",methods = ["GET","POST"])
def create():

    login = 0

    try:

        session["LoaderId"]
        session["LoaderName"]
        login= 0


    except:

        login = 1        

        return render_template("/create.html", login=login)

    if request.method == "POST":

        if recaptcha.verify()==False:

            session["Flag"] = 1
            session["Text"] = "Please verify that you are human."

            return redirect(url_for("create"))

        SongTittle = request.form['SongTittle']
        Artist = request.form['Artist']
        SongGenre = request.form['SongGenre']

        createSong = {
            "SongTittle": SongTittle,
            "Artist": Artist,
            "SongGenre": SongGenre,
            "LoaderId": session["LoaderId"],
            "LoaderName": session["LoaderName"]
            }

        response = requests.post("{}/song/create".format(URl), json = createSong)
        
        session["Flag"] = 2
        session["Text"] = "Song creation successful."

        return redirect(url_for("create"))

    else:

        try:

            if  session["Flag"]==1 or session["Flag"]==2:

                text = session["Text"]
                flag = session["Flag"]

                session["Flag"]=-1

                session["Text"]=""

                return render_template("/create.html", login=login, flag=flag, text=text)
            else:

                return render_template("/create.html", login=login, flag=-1)

        except:

            return render_template("/create.html", login=login, flag=-1)


@app.route("/mySongs",methods = ["GET","POST"])
def mySongs():

    login = 0

    try:

        session["LoaderId"]
        session["LoaderName"]
        login= 0

    except:

        login = 1        

        return render_template("/mySongs.html", login=login)


    response = requests.get("{}/song/get/".format(URl)+str(session["LoaderId"])).json()
    songs = []
    for i in response:

        songs.append(i)
        
    try:

        if session["Flag"]==1 or session["Flag"]==2:

            text = session["Text"]
            flag = session["Flag"]

            session["Flag"]=-1

            session["Text"]=""

            return render_template("/mySongs.html", login=login, songs=songs, flag=flag, text=text)
            
        else:

            return render_template("/mySongs.html", login=login, songs=songs, flag=-1)

    except:

        return render_template("/mySongs.html", login=login, songs=songs, flag=-1)



@app.route("/process",methods = ["GET","POST"])
def process():

    login = 0

    try:

        session["LoaderId"]
        session["LoaderName"]
        login= 0


    except:

        login = 1        

        return render_template("/mySongs.html", login=login)

    if request.method == "POST":

        processType = request.form['processType']

        if str(processType)=="0":

            SongId = request.form['SongId']
            LoaderId = session["LoaderId"]

            json={"SongId": SongId, 
                  "LoaderId":LoaderId}

            response = requests.delete("{}/song/delete/".format(URl), json=json)
            
            session["Flag"] = 2
            session["Text"] = "Song deletion successful."

        elif str(processType)=="1":

            LoaderId = session["LoaderId"]
            SongId = request.form['SongId']
            Artist = request.form['Artist']
            LoaderName = session["LoaderName"]
            SongGenre = request.form['SongGenre']
            SongProductionDate = request.form['SongProductionDate']
            SongTittle = request.form['SongTittle']

            json={"SongId":SongId,
                "SongTittle":SongTittle,
                "Artist":Artist,
                "SongGenre":SongGenre,
                "SongProductionDate":SongProductionDate,
                "LoaderId": LoaderId, 
                "LoaderName":LoaderName
                  }

            response = requests.put("{}/song/update/".format(URl), json=json)

            session["Flag"] = 2
            session["Text"] = "The song {} has been successfully updated.".format(SongTittle)           

        return redirect(url_for("mySongs"))

    else:

        return redirect(url_for("mySongs"))



@app.route("/login",methods = ["GET","POST"])
def login():

    if request.method == "POST":

        session["LoaderId"] = str(uuid4())
        session["LoaderName"] = request.form['name']

        return redirect(url_for("main"))


    else:

        return redirect(url_for("main"))

if __name__ == "__main__": 
	app.run(host='0.0.0.0', port=5000, debug=True)
