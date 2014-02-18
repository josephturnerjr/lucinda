import requests
import json


def crud_example():
    r = requests.post("http://0.0.0.0:5000/apple", data={"data": json.dumps({'test': 1})}).json()
    print r
    r = requests.get("http://0.0.0.0:5000/apple").json()
    print r["data"]
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

if __name__ == "__main__":
    crud_example()
