import requests
import os

cookie = {
    'session':'53616c7465645f5f0dd6697f2a8fada40e904fd407fa090c6dd5c2c5c714b5d6bf83ed0b32ce816a06c146d380a41d7a306cb17275cb3ac94a914d902ef52690'
}

def loadfile(f, url):
    f = 'inputs/'+f
    if not os.path.isfile(f):
        response = requests.get(url,cookies=cookie)
        if response.status_code == 200:
            with open(f, 'wb') as file:
                file.write(response.content)
        else:
            raise Exception("Failed to get remote file")
        print("Successful retrieval of remote file.")
    with open(f,'r') as file:
        return [line.strip() for line in file.readlines()]

def preproc(data):
    return [d.strip() for d in data.strip().split('\n') if (d is not None) and (len(d.strip()) > 0)]
    