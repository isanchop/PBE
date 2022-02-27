import board
import busio
from time import sleep

from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

ic, ver, rev, support = pn532.firmware_version

print("Found PN532 with firmware version: {0}.{1}".format(ver, rev))
pn532.SAM_configuration()
print("Waiting for RFID/NFC card...")
while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is None:
        continue
    print("Found card with UID:", int.from_bytes(uid, "big"))
    sleep(1)