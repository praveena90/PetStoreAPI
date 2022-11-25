from uuid import uuid4

import jsonpath as jsonpath
import requests
import json
from Utils.config import URL
from Utils.config import PETID


def test_upload_pet_image():

    url = URL+str(PETID)+'/uploadImage'
    print(url)
    file= {'file': open('C:\\Projects\\API\\1.jpg', 'rb')}
     # Pass the request json to post method

    response = requests.post(url,files=file)

    # Assert status code
    assert response.status_code == 200

