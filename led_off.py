from gpiozero import LED

    def LED_OFF(pin):
        led=LED(pin)
        led.off()
        return ('OFF = PIN ' +str(pin))
