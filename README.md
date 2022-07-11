![](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white) ![](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=for-the-badge&logo=Amazon%20DynamoDB&logoColor=white) ![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white) ![](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white) ![](https://img.shields.io/badge/Apache-D22128?style=for-the-badge&logo=Apache&logoColor=white) ![](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

# Building CRUD API with Lambda, FastAPI and DynamoDB

<div align="center">
    
![spotifysema](https://user-images.githubusercontent.com/54184905/178221555-2e2a94dc-88e4-482d-b670-68ce811584ad.png)
    
</div>

Hello, I'm Ahmet Furkan DEMİR, in this article/project I will show you how to create a CRUD API with Lambda, FastAPI and DynamoDB, we will make a platform like Spotify where we can upload our favorite songs while creating the API, have a good read.

**Stages**

├──  [What is Amazon DynamoDB](https://github.com/AhmetFurkanDEMIR/Building-CRUD-API-with-Lambda-FastAPI-and-DynamoDB#what-is-amazon-dynamodb)

├── [Create FastAPI](https://github.com/AhmetFurkanDEMIR/Building-CRUD-API-with-Lambda-FastAPI-and-DynamoDB#create-fastapi)

├── [Running FastAPI in AWS Lambda Function](https://github.com/AhmetFurkanDEMIR/Building-CRUD-API-with-Lambda-FastAPI-and-DynamoDB#running-fastapi-in-lambda-function)

├── [FastAPI connection with our Flask (Spotify) app](https://github.com/AhmetFurkanDEMIR/Building-CRUD-API-with-Lambda-FastAPI-and-DynamoDB#fastapi-connection-with-our-flask-spotify-app)

├── [Deploying our Flask (Spotify) application on Amazon EC2](https://github.com/AhmetFurkanDEMIR/Building-CRUD-API-with-Lambda-FastAPI-and-DynamoDB#deploying-our-flask-spotify-application-on-amazon-ec2)

└── [The Finish](https://github.com/AhmetFurkanDEMIR/Building-CRUD-API-with-Lambda-FastAPI-and-DynamoDB#the-finish)


### What is Amazon DynamoDB

<div align="center">
    
![images-removebg-preview](https://user-images.githubusercontent.com/54184905/178202112-64342ff7-8172-4c9e-a1d7-1173eb846f00.png)
    
</div>

[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is a fully managed proprietary NoSQL database service that supports key–value and document data structures and is offered by Amazon.com as part of the Amazon Web Services portfolio. DynamoDB exposes a similar data model to and derives its name from Dynamo, but has a different underlying implementation. Dynamo had a multi-leader design requiring the client to resolve version conflicts and DynamoDB uses synchronous replication across multiple data centers for high durability and availability. DynamoDB was announced by Amazon CTO Werner Vogels on January 18, 2012, and is presented as an evolution of Amazon SimpleDB.

I recommend this course on Coursera to learn Amazon DynamoDB. [Link](https://www.coursera.org/learn/dynamodb-nosql-database-driven-apps)

If you don't want to watch the course, you can refer to the notes and exercises in this course. [Link](https://github.com/AhmetFurkanDEMIR/Amazon-DynamoDB-Building-NoSQL-Database-Driven-Applications)

We will use the Amazon DynomoDB NoSQL database to store the songs uploaded to our Spotify application, we will be able to perform operations such as adding data, updating data, deleting data and reading data in this database. Now that we have completed this stage, we can move on to the next stage.


### Create FastAPI

<div align="center">
    
![FastAPI_logo](https://user-images.githubusercontent.com/54184905/178194766-50e33c0c-a7bf-4efc-a0d8-51e53c85ae4b.png)
    
</div>

FastAPI is a Web framework for developing RESTful APIs in Python. FastAPI is based on Pydantic and type hints to validate, serialize, and deserialize data, and automatically auto-generate OpenAPI documents.

It fully supports asynchronous programming and can run with Uvicorn and Gunicorn. To improve developer-friendliness, editor support was considered from the earliest days of the project.

With FastAPI, we will be able to add data to our table in our DynamoDB database, edit the data, delete the data and read the data. You can proceed to the FastAPI I created from the [/FastAPI_DynamoDB](/FastAPI_DynamoDB/) directory, do not forget to edit the [.env](/FastAPI_DynamoDB/.env) file under this directory according to your own AWS keys. If you do not make this edit, you will not be able to access DynamoDB in your AWS account and run the API.

```env
AWS_ACCES_KEY_ID=***********
AWS_SECRET_ACCESS_KEY=***********
REGION_NAME=us-east-1
```

Now that you have edited the .env file, we can deploy the API over localhost from port 8000 with the python3 main.py command.

You can go to http://127.0.0.1:8000/docs and see the HTTP Mothods available in our API.

<div align="center">
    
![Screenshot_2022-07-11_09-41-40](https://user-images.githubusercontent.com/54184905/178204099-68b7b0a4-f4f2-43ff-9f11-013856008090.png)
    
</div>

We will be able to perform operations on the data in our table with the Post, Get, Delete and Put methods above. Now that our FastAPI creation process is finished, we can now move on to the answer to the question of how we can deploy this API on AWS Lambda.

### Running FastAPI in Lambda Function

<div align="center">
    
![lambda_1_75](https://user-images.githubusercontent.com/54184905/178223560-b83d10c5-cf41-45c3-a6df-df21d88f2f0e.png)
    
</div>

AWS Lambda is an event-driven, serverless computing platform provided by Amazon as a part of Amazon Web Services. It is a computing service that runs code in response to events and automatically manages the computing resources required by that code. It was introduced in November 2014.

Node.js, Python, Java, Go, Ruby, and C# (through .NET) are all officially supported as of 2018. In late 2018, custom runtime support was added to AWS Lambda.

Scroll to the link to learn how to run Python FastAPI or any Python script on AWS Lambda. [Link](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)

Now that we have deployed our FastAPI on Lambda, we can connect with our interface and make the application work.


### FastAPI connection with our Flask (Spotify) app

<div align="center">
    
![Çalışma Yüzeyi 1](https://user-images.githubusercontent.com/54184905/178221791-4890b6d2-507f-47c5-b562-3832664b6a6b.png)
    
</div>

Follow the directory [/Flask_Website](/Flask_Website) to access the Frontend and Backend of our Spotify application. Edit the [.env](/Flask_Website/.env) file found here again according to the ip address or url address of your own FastAPI.


```env
URL=Your_Url_or_Ip
```

```python
global URl
URl = getenv("URL")
```

```python
#all songs
response = requests.get("{}/song/all".format(URl)).json()


# My songs
response = requests.get("{}/song/get/".format(URl)+str(session["LoaderId"])).json()


# Creating song
createSong = {
    "SongTittle": SongTittle,
    "Artist": Artist,
    "SongGenre": SongGenre,
    "LoaderId": session["LoaderId"],
    "LoaderName": session["LoaderName"]
}
response = requests.post("{}/song/create".format(URl), json = createSong)


# Song update
json={
    "SongId":SongId,
    "SongTittle":SongTittle,
    "Artist":Artist,
    "SongGenre":SongGenre,
    "SongProductionDate":SongProductionDate,
    "LoaderId": LoaderId, 
    "LoaderName":LoaderName
}
response = requests.put("{}/song/update/".format(URl), json=json)


# Song delte
json={
    "SongId": SongId, 
    "LoaderId":LoaderId
}
response = requests.delete("{}/song/delete/".format(URl), json=json)
```

With the python3 main.py command, you can deploy our Flask website and add your favorite songs to our Spotify application. Now that we have finished all our configuration and operations, we can deploy this Flask website via Amazon EC2.


### Deploying our Flask (Spotify) application on Amazon EC2

<div align="center">
    
![Çalışma Yüzeyi 1](https://user-images.githubusercontent.com/54184905/178222338-c96322f3-5077-4bbd-90c8-cfeffcd86441.png)
    
</div>

**Amazon EC2 :** Amazon Elastic Compute Cloud (EC2) is a part of Amazon.com's cloud-computing platform, Amazon Web Services (AWS), that allows users to rent virtual computers on which to run their own computer applications. EC2 encourages scalable deployment of applications by providing a web service through which a user can boot an Amazon Machine Image (AMI) to configure a virtual machine, which Amazon calls an "instance", containing any software desired. A user can create, launch, and terminate server-instances as needed, paying by the second for active servers – hence the term "elastic". EC2 provides users with control over the geographical location of instances that allows for latency optimization and high levels of redundancy. In November 2010, Amazon switched its own retail website platform to EC2 and AWS.

**Docker :** Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine. It was first started in 2013 and is developed by Docker, Inc.

**Apache :** The Apache HTTP Server is a free and open-source cross-platform web server software, released under the terms of Apache License 2.0. Apache is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation. The vast majority of Apache HTTP Server instances run on a Linux distribution, but current versions also run on Microsoft Windows, OpenVMS, and a wide variety of Unix-like systems. Past versions also ran on NetWare, OS/2 and other operating systems, including ports to mainframes.

Use the commands below to run the Flask (Spotify) app on your local computer with docker.

```bash
# Cleaning up Docker images
docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)

# Running all images (While in the project folder)
sudo docker-compose up -d
```

To deploy the Flask (Spotify) application on Amazon EC2 with Apache, proceed to the Medium article in the link. [Link](https://medium.com/@ahmetfurkandemir/deploy-the-python-flask-website-f43fcc5f2c80)


### The Finish

<div align="center">
    
![Screenshot_2022-07-11_11-11-15](https://user-images.githubusercontent.com/54184905/178218713-a3fadd19-73b4-4955-bec8-03361428456b.png)
    
</div>

After creating the architecture in the picture above, I opened a new Subdomain under the softforrange.com domain name and added a new dns record and directed this record to the machine running on EC2. So now the application I created via [spotify.softforrange.com](https://spotify.softforrange.com/) will be accessible.
