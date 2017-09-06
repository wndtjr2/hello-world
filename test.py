import requests

class url_request():

    print("hello world")
    req = urllib.request.Request("http://www.daum.net")
    data = urllib.request.urlopen(req).read()
    print(data)
