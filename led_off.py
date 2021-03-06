from flask import Flask, request, jsonify, render_template, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

def onLED(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
	return 'LED no: {} ON'.format(str(pin))

def offLED(pin):
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	return 'LED no: {} OFF'.format(str(pin))


# Route "/" -> GET -> templates/led.html => Display Button for on-off & ask for pin number from the user. 
# Route "/on" -> POST => Get the pin and on or off led using RPI.
# Route "/off" -> POST => Get the pin and on or off led using RPI.
@app.route("/", methods=["GET"])
def led():
	if request.method == 'GET':
		return render_template('led.html')

@app.route("/pin_on", methods=["POST"])
def led_on():
	if request.method == 'POST':
		body = request.get_json()
		return jsonify({"status": onLED(body.get('pin'))})

@app.route("/pin_off", methods=["POST"])
def led_off():
	if request.method == 'POST':
		body = request.get_json()
		return jsonify({"status": offLED(body.get('pin'))})


# @app.route("/cleanup", methods=["POST"])
# def cleanup():
# 	if request.method == 'POST':
# 		GPIO.cleanup()
# 		return jsonify({"status": "Done cleaning the house!"})

# Route "/pwm" -> GET -> templates/pwm.html => Display Button for on-off & ask for pin number & duty cycle from the user. 
# Route "/pwm" -> POST => Get the pin & duty cycle, on or off led using RPI and then change the intensity of light.

@app.route("/pwm", methods=["GET"])
def pwm():
	if request.method == 'GET':
		return render_template('pwm.html')

@app.route("/pwmon", methods=["POST"])
def pwmon():
	if request.method == 'POST':
		body = request.get_json()
		p=GPIO.PWM(pin,50)
		p.start(0)
		try:
			while True:
				for i in range(100):
					p.ChangeDutyCycle(i)
            		time.sleep(0.02)
        		for i in range(100):
        			p.ChangeDutyCycle(100-i)
           			time.sleep(0.02)
           	except keyboardInterrupt:
				pass 

		p.stop()

	return jsonify({"status": onLED(body.get('pin'))})

if __name__ =='__main__':
    app.run(host='0.0.0.0', debug=True)