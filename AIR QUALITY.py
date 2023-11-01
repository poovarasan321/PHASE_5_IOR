import RPi.GPIO as GPIO

import time

# Define the GPIO pin where the analog output of the MQ-135 sensor is 

connected

MQ_PIN = 0

# Set the GPIO mode to BCM

GPIO.setmode(GPIO.BCM)
def read_mq():
try:
 while True:
 # Open a file to store the sensor values
 with open("air_quality_log.txt", "a") as log_file:
 # Initialize GPIO
 GPIO.setup(MQ_PIN, GPIO.IN)
 time.sleep(2) # Allow the sensor to warm up
 # Read the analog value from the sensor
 value = 0
 GPIO.setup(MQ_PIN, GPIO.OUT)
 GPIO.output(MQ_PIN, GPIO.LOW)
 time.sleep(0.1)
 while GPIO.input(MQ_PIN) == GPIO.LOW:
 continue
 start_time = time.time()
 while GPIO.input(MQ_PIN) == GPIO.HIGH:
 continue
 end_time = time.time()
 # Calculate sensor resistance and air quality index
 pulse_duration = end_time - start_time
ratio = pulse_duration / 2 / 30 # 30 is a typical value for clean 
air
 sensor_value = (1 - ratio) * 10000
 # Log the sensor value
 log_file.write(f"{time.ctime()}: Sensor Value: 
{sensor_value:.2f}\n")
 print(f"{time.ctime()}: Sensor Value: {sensor_value:.2f}")
 # Adjust this threshold according to your specific sensor and 
air quality standards
 if sensor_value > 300:
 print("Air quality is poor")
 else:
 print("Air quality is good")
 time.sleep(60) # Read the sensor every minute
 except KeyboardInterrupt:
 GPIO.cleanup()
if __name__ == "__main__":
read_mq()
