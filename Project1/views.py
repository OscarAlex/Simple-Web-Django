from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Person():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

#Each function is a view
#Request as argument
def welcome(request):
    person= Person('Claire', 'Willow')
    #name= 'John'
    #last_name= 'Anderson'
    date= datetime.datetime.now()
    subjects= []#['Languages', 'Math', 'Biology']

    #Doc path
    ext_doc= open('C:/Users/Oscar/Desktop/FirstDjango/Project1/Project1/templates/welcome.html')
    #Read template
    temp= Template(ext_doc.read())
    ext_doc.close()

    #Context
    context= Context({
        'name':person.name,
        'last_name': person.last_name,
        'date': date,
        'subjects': subjects
    })

    doc= temp.render(context)
    return HttpResponse(doc)

def farewell(request):
    return HttpResponse("Goodbye")

def getDate(request):
    actual_date= datetime.datetime.now()
    return HttpResponse(actual_date)

def calculateAge(request, age, year):
    period= year-2021
    future_age= age+period
    return HttpResponse("On the year {0} you will be {1} years old".format(year, future_age))