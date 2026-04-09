from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def Hello_world():
    return 'Flask Hello world!!'

@app.route('/abobaail')
def test():
    return 'meya mesa on aboubasil'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000),
