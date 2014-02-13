A little toy application I built. It's a MongoDB-backed, generic REST
server. CRUD for any REST endpoint!

## Example:

    import requests
    import json


    r = requests.post("http://0.0.0.0:5000/apple", data={"data": json.dumps({'test': 1})}).json()
    print r
    r = requests.get("http://0.0.0.0:5000/apple").json()
    print r
    query = r["data"][0]["_id"]["$oid"]
    r = requests.get("http://0.0.0.0:5000/apple/%s" % query).json()
    print r
    r = requests.put("http://0.0.0.0:5000/apple/%s" % query, data={"data":json.dumps({'moar': 2})}).json()
    print r
    r = requests.get("http://0.0.0.0:5000/apple/%s" % query).json()
    print r
    r = requests.delete("http://0.0.0.0:5000/apple/%s" % query).json()
    print r
    r = requests.get("http://0.0.0.0:5000/apple/%s" % query).json()
    print r

Prints:

    {u'status': 200, u'message': u'OK.'}
    [{u'test': 1, u'_id': {u'$oid': u'52fc581344ac617b7962fd26'}}]
    {u'status': 200, u'message': u'OK.', u'data': {u'test': 1, u'_id':
    {u'$oid': u'52fc581344ac617b7962fd26'}}}
    {u'status': 200, u'message': u'OK.'}
    {u'status': 200, u'message': u'OK.', u'data': {u'_id': {u'$oid': u'52fc581344ac617b7962fd26'}, u'moar': 2}}
    {u'status': 200, u'message': u'OK.'}
    {u'status': 404, u'message': u'No such apple'}


Of course, it doesn't have to be apple. It can be anything! I'm not
entirely sure I see a value in this yet (categorical data collection?
testing out frontend ideas?), but I thought it seemed cool.
