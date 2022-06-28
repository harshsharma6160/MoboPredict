from flask import Flask, render_template, request, jsonify

import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/getPrice', methods=['POST'])
def getPrice():
    res = request.values.to_dict()
    model = pickle.load(open('D:\Flask\FlaskMarket\market\model.sav', 'rb'))
    data = list(res.values())
    prediction = model.predict([data])
    print(prediction)
    return jsonify({'price': prediction[0]})


if __name__ == '__main__':
    app.run()
