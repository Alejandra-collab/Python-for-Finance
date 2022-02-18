from cgitb import html
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getInfo(url):
    try:
        html = urllib.request.urlopen(url)
    except HTTPError as e:
        return None # Return a null, break,... url.
    try: # If the tag we're trying to get in does not exis
        obj = BeautifulSoup(url.read())
        infoFrom = obj.body.div.a  class="btn btn-primary btn-sm view-data" href="/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data"
    except AttributeError as e:
        return None
    return infoFrom

infoFrom = getTitle("https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr")

if infoFrom == None:
    print("Title could not be found")  
    else:
        print(infoFrom)

    





