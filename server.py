from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
import json
import util
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/', methods=['POST'])
@cross_origin()
def predict_heart_disease():
    event_data = json.loads(request.get_data().decode('utf-8'))
    print(event_data['data'])
    input=event_data['data']
    # predict_data=int(util.get_disease_output(input))
    predict_data=int(util.get_disease_result(input))
    print(predict_data)
    print(type(predict_data))
    response=jsonify({
        'predict':predict_data
    })
    return response

if __name__=="__main__":
    print("Flask server is running ")
app.run()
