
import requests


OWM_Endpoit = "api.openweathermap.org/data/2.5/forecast"

weaterparmns = {
    "lat" = 51.507351,
    "lon" =  -0.127667,
    "appid"= api_key
}
api_key ="c60f743a5123edd76b664362f0a878cf"

response = requests.get(OWM_Endpoit, params=weatherparmns)


print (response.status_code)
print (response.text)      
