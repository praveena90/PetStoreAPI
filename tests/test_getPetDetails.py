import jsonpath as jsonpath
import requests
import json
from Utils.config import URL
from Utils.config import INVALID_PETID

def test_get_pet_details():

    pet_id  = 11
    url = URL+str(pet_id)

    response = requests.get(url)

    print(response.text)

    #Convert reponse to jason format
    response_json = json.loads(response.text)

    #Get pet name and print
    pet_name = response_json['name']
    #print(pet_name)
    assert pet_name == 'teroSr'

def test_get_invalidPet():

    url = URL+str(INVALID_PETID)

    response = requests.get(url)

    assert response.status_code == 404

    #Convert reponse to jason format
    response_json = json.loads(response.text)

    #Get pet name and print
    error_message = response_json['message']

    assert error_message == 'Pet not found'