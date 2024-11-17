import requests
import json
import base64

#Authentication application to spotify server
CLIENT_ID = "07c70ef841674ff4aebc0dbcbcfe42fe"
CLIENT_SECRET = "c599ef8cb7e144dea3192a600a8b90a9"

# Obtains an access token from the spotify API
def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token" #Endpoint for spotify API's

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"} # Indicates grant type 'client_credentials'
    result = requests.post(url, headers=headers,data=data) # Making a POST request
    json_result = json.loads(result.content)# Response is parsed as a JSON
    token = json_result["access_token"] #The access token is retrieved from JSON
    return token # Returns token 

def get_auth_token(token):
    return {"Authorization": "Bearer " + token}
    console.log(token)

token = get_token()