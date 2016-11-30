import sys, os
import requests
import json
from thetaPythonTest import startSession, takePicture



def request(url_request):
    url_base = "http://192.168.1.1/osc/"
    url = url_base + url_request
    return url

def state():
    url = request("state")
    req = requests.post(url)
    response = req.json()
    return response

def latestFileUri():
    state_data = state()["state"]
    latestFileUri = state_data["_latestFileUri"]
    return latestFileUri

def getImage(fileUri,photoName):
    url = request("commands/execute")
    body = json.dumps({"name": "camera.getImage",
         "parameters": {
            "fileUri": fileUri,
#            "_type": "thumb"
            "_type": "image"
         }
         })
    with open(photoName, 'wb') as handle:
        response = requests.post(url, data=body, stream=True)
        print response.iter_content(1024)
        for block in response.iter_content(1024):
            handle.write(block)
            print("More")
    handle.close()
    
    
def takeTheta(fname):
    retVal = ""
    #sid = startSession()
    #takePicture(sid) # how do we know it succeeded?
    #getImage(latestFileUri())
    #print("Photo complete")
    print "From takeTheta: ", fname
    ofile = open(fname,'wb')
    ofile.write(fname)
    ofile.close()
    retVal = ("\nPhoto taken: " + fname)
    return(retVal)
    
