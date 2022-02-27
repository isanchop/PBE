# PBE
Course at UPC 

## Puzzle 1
First puzzle consists on reading the UID of an RFID card using the module "NXP PN532 NFC RFID" on a Raspberry Pi 3b+

### Esquematic

    | PN532 Module PIN | RPI GPIO  |
    | :---------------:|:---------:|
    | GND              | 6         |
    | VCC              | 4         |
    | SDA              | 3         |
    | SCL              | 5         |

### Requirements 
    pip3 install adafruit-circuitpython-pn532

### Run code
    python3 puzzle1.py