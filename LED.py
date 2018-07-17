from flask import Flask,request,render_template,jsonify
from gpiozero import LED

#from led_on import LED_ON
#from led_off import LED_OFF

app = Flask(__name__)
led=LED(18)

@app.route('/',methods=['GET'])
def index():
        return render_template('index.html')

@app.route('/pin_on', methods=['GET', 'POST'])
def pin_on():
    if request.method == 'POST':
        body=request.get_json()
        led.on()
        return jsonify({'status' : 'LED_ON(body[])'})
    else:
        return jsonify({'status: unavailable'})
@app.route('/pin_off', methods=['GET', 'POST'])
def pin_off():
    if request.method == 'POST':
        body=request.get_json()
        led.off()
        return jsonify({'status' : 'LED_OFF(body[])'})
    else:
        return jsonify({'status: unavailable'})

if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)

