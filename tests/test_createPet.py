import jsonpath as jsonpath
import requests
import json
from Utils.config import URL
from pprint import pprint

file = open('C:\\Projects\\API\\createPet.json', 'r')

# Read Json file
json_iput = file.read()

def test_create_pet():

    # Convert file data into json
    request_json = json.loads(json_iput)

    #Pass the request json to post method
    #response = requests.post(url,json=request_json)
    response = requests.request("POST",URL, json=request_json)

    ind = 3
    pprint(response.text, indent=ind)
    #Assert status code
    assert response.status_code==200



def test_Verify_PetName():

    # Convert file data into json
    request_json = json.loads(json_iput)

    #Pass the request json to post method
    response = requests.post(URL,json=request_json)

    #Convert reponse to jason format
    response_json = json.loads(response.text)

    #Get pet name and print
    pet_name = response_json['tags'][0]['name']

    assert pet_name == 'bruno'


def test_Verify_Responseheader():

    # Convert file data into json
    request_json = json.loads(json_iput)

    #Pass the request json to post method
    response = requests.post(URL,json=request_json).headers

    #Get the header value
    print(response.get('Content-Type'))


def test_Verify_Status():

    # Convert file data into json
    request_json = json.loads(json_iput)

    #Pass the request json to post method
    response = requests.post(URL,json=request_json)

    #Convert reponse to jason format
    response_json = json.loads(response.text)

    #Get pet name and print
    status = jsonpath.jsonpath(response_json,'status')

    print(status)

    #Convert the response to pythod dictionry format
    response_text = response.json()

    print(response_text)
