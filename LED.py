from flask import Flask,request,render_template,jsonify
from gpiozero import LED
import time
#from led_on import LED_ON
#from led_off import LED_OFF

app = Flask(__name__)
led1=LED(14)
led2=LED(15)
led3=LED(18)
led4=LED(2)
led5=LED(3)
led6=LED(4)

@app.route('/',methods=['GET'])
def index():
        return render_template('index.html')

@app.route('/pin_on', methods=['GET', 'POST'])
def pin_on():
    if request.method == 'POST':
        body=request.get_json()
        for i in range (0,5)
        led1.on()
        time.sleep(1)
        led2.on()
        time.sleep(1)
        led1.off()
        led2.off()

        led3.on()
        time.sleep(1)
        led4.on()
        time.sleep(1)
        led3.off()
        led4.off()

        led5.on()
        time.sleep(1)
        led6.on()
        time.sleep(1)
        led5.off()
        led6.off()

        led1.on()
        led3.on()
        led5.on()
        time.sleep(1)
        led1.off() 
        led3.off()
        led5.off()

        led2.on()
        led4.on()
        led6.on()
        time.sleep(1)
        led2.off()
        led4.off()
        led6.off()

        return jsonify({'status' : 'LED_ON(body[])'})
    else:
        return jsonify({'status: unavailable'})


if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)

