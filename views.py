from flask import Flask
from flask.ext.pymongo import PyMongo
from flask import (Blueprint,
                   request,
                   json,
                   Response,
                   )
from bson import json_util

app = Flask(__name__)
mongo = PyMongo(app)


def json_response(status=200, message="OK.", data=None):
    response_data = {
        "status": status,
        "message": message,
    }
    if data:
        response_data["data"] = data
    resp = Response(
        json_util.dumps(response_data),
        status=message,
        mimetype='application/json')
    resp.status_code = status
    return resp


@app.route('/<string:collection_name>', methods=['GET', 'POST'])
def collection(collection_name):
    if request.method == "GET":
        return json_response(data=[d for d in getattr(mongo.db, collection_name).find()])
    else:
        getattr(mongo.db, collection_name).insert(json.loads(request.form.get("data")))
        return json_response()


@app.route('/<string:collection_name>/<ObjectId:obj_id>', methods=['GET', 'PUT', 'DELETE'])
def document(collection_name, obj_id):
    if request.method == "GET":
        doc = getattr(mongo.db, collection_name).find_one({"_id": obj_id})
        if not doc:
            return json_response(404, "No such %s" % collection_name)
        return json_response(data=doc)
    if request.method == "DELETE":
        getattr(mongo.db, collection_name).remove(obj_id)
        return json_response()
    else:
        getattr(mongo.db, collection_name).update(
            {"_id": obj_id},
            json.loads(request.form.get("data")))
        return json_response()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
