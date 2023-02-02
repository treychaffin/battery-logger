import time 
import os
import csv
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#initialize ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
ads.gain = 1

#set channel A0
chan = AnalogIn(ads, ADS.P0)

r1 = 47000
r2 = 10000
vcal = 0.994423

def volt_divider():
    return round(chan.voltage*vcal*(r1+r2)/r2,2)

#get the current date and time
curr_time = time.strftime("%Y-%m-%d-%H-%M-%S")

#get current date
curr_date = time.strftime("%Y-%m-%d")

#construct filename
filename = curr_date + ".csv"

#get the voltage from the channel
voltage = volt_divider()

#check if file exists, if not create it
if os.path.isfile(filename) != True:
    open(filename, "w")

#append the voltage and time to a csv file
with open(filename, 'a') as csvfile:
    csvfile = csv.writer(csvfile, delimiter=',')
    csvfile.writerow({curr_time,voltage})
