from gpiozero import LED

    def LED_ON(pin):
    led=LED(pin)
    led.on()
    
    return ('ON = PIN '+str(pin))
