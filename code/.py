# type: ignore
import time 
import os 
import board
import busio
import adafruit_mpl3115a2
import displayio
import storage


displayio.release_displays() 
sda_pin = board.GP10
scl_pin = board.GP11
i2c = busio.I2C(scl_pin, sda_pin)  
write_pin = digitalio.DigitalInOut(board.GP0)
write_pin.direction = digitalio.Direction.INPUT
write_pin.pull = digitalio.Pull.UP


sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
#sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

# If write pin is connected to ground on start-up, CircuitPython can write to
CIRCUITPY filesystem.
if not write_pin.value:
 storage.remount("/", readonly=False)

sensor.sealevel_pressure = 102250

alt_pressure = []
alt_altitude =[]
alt_temperature =[]


while True:
    pressure = sensor.pressure
    alt_pressure.append()
    print("Pressure: {0:0.3f} pascals".format(pressure))
    altitude = sensor.altitude
    alt_altitude.append()
    print("Altitude: {0:0.3f} meters".format(altitude))
    temperature = sensor.temperature
    alt_temperature.append()
    print("Temperature: {0:0.3f} degrees Celsius".format(temperature))
    time.sleep(1.0)
    break 
 
Values=open(f"/data/{time.monotonic()}.csv","w")
for i in range(len(list_z)):
Values.write(f"{list_time[i]}{list_z[i]}\n")
Values.close
