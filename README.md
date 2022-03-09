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

