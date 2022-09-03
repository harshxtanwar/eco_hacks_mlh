from typing import Collection
from django.shortcuts import render
from django.http import HttpResponse
# from database.database import post_db
# Create your views here.

import pymongo 


def mongoConnection_collection():
    client = pymongo.MongoClient("mongodb://harshxtanwar:db12345@ac-zdnook2-shard-00-00.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-01.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-02.dvbpycz.mongodb.net:27017/?ssl=true&replicaSet=atlas-83le6q-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client["eco"]
    collection = db["event_details"]
    return collection



def post_db(request):
    # name = request.get("name")
    # instructions = request.get("")
    collection = mongoConnection_collection()
    collection.insert_one(request)


def get_db_browse(request):
    if request.method == "GET":

        collection = mongoConnection_collection()
        query = list(collection.find())

        listt = []
        for i in query:
            dic = {
                'event_name' : i.get('event_name'),
                'event_date' : i.get('event_date'),
                'event_time' : i.get('event_time'),
                'event_location' : i.get('event_location')
            }
            listt.append(dic)


        
        print ((listt))
    return listt















def homepage(request):
    he = {1 : "coming from backend"}
    ## NO backend code required here
    return render(request, 'home.html', {'hel':he})

def postEvent(request):
    ## DATABASE CONNECTION MONGODB
    # collection = mongoConnection_collection()
    if request.method == 'POST':
        print(request.POST.get('event_name'))
        post_db({
            'your_name':request.POST.get('your_name'),
            'email':request.POST.get('email'),
            'mobile_no':request.POST.get('mobile_no'),
            'event_name':request.POST.get('event_name'),
            'event_date':request.POST.get('event_date'),
            'event_time':request.POST.get('event_time'),
            'event_location':request.POST.get('event_location'),
            'event_detail':request.POST.get('event_detail')
        })
    ## POST
    return render( request, 'hosting.html')

def browseEvents(request):
    ## DATABASE CONNECTION MONGODB
    if request.method == "GET":

        query = get_db_browse(request)
    return render(request, 'browsing.html', {'query': query})

def registerButton(request):
    ## GET 
    ## MONGODB connection
    ## get data to register for the event
    return render(request, 'register.html')

def regDone(request):
    ## No Backend Code Needed 
    ## Button to redirect to the homepage
    ## get data to register for the event
    return render(request,'reg_done.html')

def hostDone(request):
    return render(request, 'host_done.html') 