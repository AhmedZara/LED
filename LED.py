from flask import Flask,request,render_template,jsonify

from led_on import LED_ON
from led_off import LED_OFF

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
        return render_template('index.html')

@app.route('/pin_on', methods=['GET', 'POST'])
def pin_on():
    if request.method == 'POST':
        body=request.get_json()
        return jsonify({'status' : LED_ON(body['pin'])})
    else:
        return jsonify({'status: unavailable'})
@app.route('/pin_off', methods=['GET', 'POST'])
def pin_off():
    if request.method == 'POST':
       body=request.get_json()
        return jsonify({'status' : LED_OFF(body['pin'])})
    else:
        return jsonify({'status: unavailable'})

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')
        

