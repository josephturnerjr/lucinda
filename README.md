A little toy application I built. It's a MongoDB-backed, generic REST
server. CRUD for any REST endpoint!

## Example:

    import requests
    import json


    r = requests.post("http://0.0.0.0:5000/apple", data={"data":
    json.dumps({'test': 1})}).json()
    print r
    r = requests.get("http://0.0.0.0:5000/apple").json()
    print r
    query = r["data"][0]["_id"]["$oid"]
    r = requests.get("http://0.0.0.0:5000/apple/%s" % query).json()
    print r
    r = requests.put("http://0.0.0.0:5000/apple/%s" % query,
    data={"data":json.dumps({'moar': 2})}).json()
    print r
    r = requests.get("http://0.0.0.0:5000/apple/%s" % query).json()
    print r
    r = requests.delete("http://0.0.0.0:5000/apple/%s" % query).json()
    print r
    r = requests.get("http://0.0.0.0:5000/apple/%s" % query).json()
    print r

Of course, it doesn't have to be apple. It can be anything! I'm not
entirely sure I see a value in this yet (categorical data collection?
testing out frontend ideas?), but I thought it seemed cool.
