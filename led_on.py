from gpiozero import LED
def LED_ON(pin):
    led=LED(18)
    led.on()
    return ('ON = PIN '+str(pin))
