import urllib.request
import urllib.parse
def login():
    params = urllib.parse.urlencode({"luizdb":"97531Abc&$@"})
    resp = urllib.request.urlopen("https://twitter.com/i/flow/login", params)
    return()
def send_to_twitter(msg):
    cons = urllib.request.urlopen("https://twitter.com/compose/post", msg)       
msg = input("Do you want see the gm?")
if msg == "y":
    send_to_twitter("Every day better")
else:
    send_to_twitter("United eoooh")