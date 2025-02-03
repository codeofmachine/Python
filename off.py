import urllib.request
import urllib.parse
import time
status = "off"
params = urllib.parse.urlencode({status})
pars = urllib.request.urlopen("https://forums.sketchup.com/", params)
cont = time.sleep(3.18)
pars + cont * 2300

