# PBE
Course at UPC 

## Puzzle 1
First puzzle consists on reading the UID of an RFID card using the module "NXP PN532 NFC RFID" and protocol UART on a Raspberry Pi 3b+

### Pin out:

<table style="width:100%" align="center">
    <tr>
        <th>Pin Out connections</th>
        <th>Esquematic</th>
    </tr>
    <tr>
        <td>
            <table>
                <tr>
                    <th>PN532 Module PIN</th>
                    <th>RPI GPIO</th>
                </tr>
                <tr>
                    <td>VCC</td>
                    <td>4</td>
                </tr>
                <tr>
                    <td>GND</td>
                    <td>6</td>
                </tr>
                <tr>
                    <td>RXD</td>
                    <td>8</td>
                </tr>
                <tr>
                    <td>TXD</td>
                    <td>10</td>
                </tr>
            </table>
        </td>
        <td><img src="https://user-images.githubusercontent.com/67743899/157332390-9396b52a-21bc-4ea1-b055-397795b00e75.png" width=300px></td>
    </tr>
</table>



### Requirements:
    pip3 install adafruit-circuitpython-pn532

### Run code:
    python3 puzzle1.py

## Puzzle 2
Second puzzle consists on create a simple GUI for the first puzzle. We are working with PyGObject library for python

### Out put
<p align="center">
    <img width="318" alt="waiting-read" src="https://user-images.githubusercontent.com/67743899/161647377-e33f21e5-17d6-463b-b94f-ff0104aef136.png" width=300px>
    <img width="318" alt="read" src="https://user-images.githubusercontent.com/67743899/161647391-d040e554-0b83-4050-aa54-9a73c669352a.png" width=300px>
</p>

### Requirements:
    pip3 install PyGObject

### Run code:
    python3 puzzle2.py
