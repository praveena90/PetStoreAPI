import jsonpath as jsonpath
import requests
import json
from Utils.config import URL
from Utils.config import PETID
from Utils.config import PETNAME
from assertpy import assert_that

def test_update_petById():

    url = URL+str(PETID)

    reponse = requests.post(url,data={'petId': PETID,'name':PETNAME})

    #ssert reponse.status_code == 200

    assert_that(reponse.status_code,200)

    print(reponse.text)
