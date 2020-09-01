import os
from flask import Flask, json

ids = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)


@api.route('/ids', methods=['GET'])
def get_ids():
    return json.dumps(ids)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    api.run(host='0.0.0.0', port=int(port))
