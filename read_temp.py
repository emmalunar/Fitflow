# import smbus2 as smbus
# import time

# # Create an I2C bus object
# bus = smbus.SMBus(1)

# # HW-691 I2C address (check your sensor's datasheet for the correct address)
# HW691_ADDRESS = 0x48


# def read_temperature():
#     # Read 2 bytes of data from the sensor
#     data = bus.read_i2c_block_data(HW691_ADDRESS, 0, 2)  # Read 2 bytes
#     # Process the data (this will depend on the sensor's datasheet)
#     temperature = (data[0] << 8) | data[1]  # Combine the two bytes
#     return temperature


# try:
#     while True:
#         temp = read_temperature()
#         print(f"Temperature: {temp} °C")
#         time.sleep(1)   
#         break

# except KeyboardInterrupt:
#     print("Program stopped")



#  This is the code to run the MLX90614 Infrared Thermal Sensor
# You'll need to import the package "Adafruit Blinka"
# You'll need to import the package "adafruit-circuitpython-mlx90614/"
# You'll need to enable i2c on the pi https://pimylifeup.com/raspberry-pi-i2c/
# Reboot after enabling i2C
# Sensor is connected to 3.3V, GND and the i2C pins 3(SDA) and 5(SCL)

# import board
# import busio as io
# import adafruit_mlx90614

# from time import sleep

# i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
# mlx = adafruit_mlx90614.MLX90614(i2c)

# ambientTemp = "{:.2f}".format(mlx.ambient_temperature)
# targetTemp = "{:.2f}".format(mlx.object_temperature)

# sleep(1)

# print("Ambient Temperature:", ambientTemp, "°C")
# print("Target Temperature:", targetTemp,"°C")
  

# import smbus
# import time

# # Create an I2C bus object
# bus = smbus.SMBus(1)

# # HW-691 I2C address (check your sensor's datasheet for the correct address)
# HW691_ADDRESS = 0x48

# def read_temperature():
#     try:
#         # Read 2 bytes of data from the sensor
#         data = bus.read_i2c_block_data(HW691_ADDRESS, 0, 2)  # Read 2 bytes
#         # Process the data (this will depend on the sensor's datasheet)
#         temperature = (data[0] << 8) | data[1]  # Combine the two bytes
#         return temperature
#     except Exception as e:
#         print(f"Error reading temperature: {e}")
#         return None

# try:
#     while True:
#         temp = read_temperature()
#         if temp is not None:
#             print(f"Temperature: {temp} °C")
#         time.sleep(1)   
        
    
# except KeyboardInterrupt:
#     print("Program stopped")


# import board
# import busio
# from adafruit_mlx90614 import MLX90614

#    # Create I2C bus
# i2c = busio.I2C(board.SCL, board.SDA)

#    # Create sensor object
# sensor = MLX90614(i2c)

#    # Read ambient and object temperatures
# ambient_temp = sensor.ambient_temperature
# object_temp = sensor.object_temperature

# print(f"Ambient Temperature: {ambient_temp:.2f}°C")
# print(f"Object Temperature: {object_temp:.2f}°C")
    
import board
import busio
from adafruit_mlx90614 import MLX90614
import time

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor object
sensor = MLX90614(i2c)

try:
    while True:
        # Read ambient and object temperatures
        ambient_temp = sensor.ambient_temperature
        object_temp = sensor.object_temperature

        # Print the temperatures
        print(f"Ambient Temperature: {ambient_temp:.2f}°C")
        print(f"Object Temperature: {object_temp:.2f}°C")
        
        time.sleep(1)  # Sleep for 1 second before the next reading

except KeyboardInterrupt:
    print("Interrupted! Stopping the program.")
