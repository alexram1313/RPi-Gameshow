import RPi.GPIO as GPIO
import time

class BuzzerMatch:
    
    GPIO_BOARD = GPIO.BOARD
    GPIO_BCM   = GPIO.BCM
    
    def __init__(self, board_mode, p1_btn, p1_led, p2_btn, p2_led):
        self.__need_clean = False
        check = {p1_btn, p1_led, p2_btn, p2_led}
        if len(check) < 4:
            raise ValueError("Pins must be all different")
        
        self.__p1_btn = p1_btn
        self.__p1_led = p1_led
        
        self.__p2_btn = p2_btn
        self.__p2_led = p2_led

        GPIO.setmode(board_mode)

        self.__reset_callback = False

        GPIO.setup(self.__p1_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.__need_clean = True
        GPIO.setup(self.__p1_led, GPIO.OUT,initial=GPIO.LOW)
        
        GPIO.setup(self.__p2_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.__p2_led, GPIO.OUT,initial=GPIO.LOW)

    def __disable_check(self, pin):
        #print("callback", self.__results)
        if (self.__results == []):
            self.__results.append(pin)

    def play(self):
        self.reset()
        self.__results = []
        
        GPIO.add_event_detect(self.__p1_btn, GPIO.FALLING, callback=self.__disable_check, bouncetime=300)
        self.__reset_callback= True
        GPIO.add_event_detect(self.__p2_btn, GPIO.FALLING, callback=self.__disable_check, bouncetime=300)
        try:
            while (self.__results == []):
                time.sleep(0.3)
                
            if (self.__results[0] == self.__p1_btn):
                GPIO.output(self.__p1_led, 1)
                return False
            elif (self.__results[0]== self.__p2_btn):
                GPIO.output(self.__p2_led, 1)
                return True
            return None
        finally:
            #print("finally", self.__results)
            GPIO.remove_event_detect(self.__p1_btn)
            GPIO.remove_event_detect(self.__p2_btn)
    
    def reset(self):
        self.__results = [0];
        if (self.__reset_callback == True):
            GPIO.remove_event_detect(self.__p1_btn)
            GPIO.remove_event_detect(self.__p2_btn)
        self.__reset_callback= False
        GPIO.output(self.__p1_led, 0)
        GPIO.output(self.__p2_led, 0)
        
    def cleanup(self):
        if self.__need_clean:
            GPIO.cleanup()
        
    def __del__(self):
        self.cleanup()
        
