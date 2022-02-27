###########################################################################
###########################################################################
#### This example shows connecting to the PN532 with I2C.              ####
#### We are using the adafruit library.                                ####
#### This program will read an rfid card and show it's uid on console. ####
###########################################################################
###########################################################################

import board
import busio
from adafruit_pn532.i2c import PN532_I2C
from time import sleep

class Rfid: 
    def __init__(self):
        # I2C connection:
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.pn532 = PN532_I2C(self.i2c, debug=False)
        # Configure PN532 to communicate with MiFare cards
        self.pn532.SAM_configuration()

    
    def read_uid(self):
        while True:
            # Check if a card is available to read
            uid = self.pn532.read_passive_target(timeout=0.5)
            # Try again until card is available.
            if uid:
                return uid.hex().upper()



if __name__ == "__main__":
    # Init Rfid
    rf = Rfid()
    print("Waiting for RFID/NFC card...")
    # Infinnte loop until a key is pressed
    try:
        while True:
            # Read the UID
            uid = rf.read_uid()
            # Print the UID number on console
            print("Found card with UID:", uid)
            # Wait one second to make the next reading
            sleep(1)
    except KeyboardInterrupt:
        pass 