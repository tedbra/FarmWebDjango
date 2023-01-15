from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import json 

# Create your views here.

def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data

def read_json(path):   
    return json.loads(read_file(path))

#This function reads the language parameter and 
#chooses the corresponding parameter dictionary to that language
def choose_language(param):
    parametreLanguage = read_json('lang.JSON')    
    if param=="EN":
        return parametreLanguage.get("parameterEnglish")
    else :
        return parametreLanguage.get("parameterFrench")

#This function merges two dictionaries and brings them on the same level
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res        

