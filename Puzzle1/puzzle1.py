###########################################################################
###########################################################################
#### This example shows connecting to the PN532 with I2C.              ####
#### We are using the adafruit library.                                ####
#### This program will read an rfid card and show it's uid on console. ####
###########################################################################
###########################################################################

import board
import busio
from time import sleep

from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

# Get the chip firmware version
ic, ver, rev, support = pn532.firmware_version
print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))

# Configure PN532 to communicate with MiFare cards
pn532.SAM_configuration()
print("Waiting for RFID/NFC card...")

while True:
    # Check if a card is available to read
    uid = pn532.read_passive_target(timeout=0.5)
    # Try again if no card is available.
    if uid is None:
        continue
    # Print the UID number on console
    print("Found card with UID:", int.from_bytes(uid, "big"))
    # Wait one second to make the next reading
    sleep(1)