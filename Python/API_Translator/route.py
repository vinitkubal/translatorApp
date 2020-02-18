from flask import Flask, request, jsonify,make_response
from flask_cors import CORS, cross_origin
import convert_lang

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'


cors = CORS(app, resources={r"/": {"origins": "http://localhost:8100/"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def index():
    req = request.get_json()
    print(req['body']['data'])
    result = convert_lang.convert(req['body']['data'] , req['body']['dest'])
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug = True)