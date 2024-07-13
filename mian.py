import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

def generate_frequency(freq):
    if freq < 1 or freq > 80000:
        print("Frequency must be between 1 Hz and 80 kHz")
        return
    
    period = 1 / freq
    while True:
        try:
            GPIO.output(12, GPIO.HIGH)
            time.sleep(period / 2)
            GPIO.output(12, GPIO.LOW)
            time.sleep(period / 2)
        except KeyboardInterrupt:
            break

try:
    while True:
        user_input = input("Enter desired frequency (1-80000 Hz): ")
        try:
            freq = int(user_input)
            generate_frequency(freq)
        except ValueError:
            print("Please enter a valid whole number.")
except KeyboardInterrupt:
    print("\nProgram terminated.")
finally:
    GPIO.cleanup()
