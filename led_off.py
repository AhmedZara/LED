from gpiozero import LED
def LED_OFF(pin):
    led=LED(18)
    led.off()
    return ('OFF = PIN ' +str(pin))
