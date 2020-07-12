# ADS1248-CircuitPython
 A CircuitPython library for usage of the ADS1248.
 
## Dependencies
- Core CircuitPython modules.

## Usage
Example code can be found [here](https://github.com/AdinAck/ADS1248-CircuitPython/tree/master/examples).

Place [ADS1248.py](https://github.com/AdinAck/ADS1248-CircuitPython/blob/master/ADS1248.py) on your CircuitPython board next to your main script.

Import the ADS1248 library like so:
```
from ADS1248 import ADS1248
```

Create a four wire spi bus for the ADS1248(s) to use (hardware SPI pins are not required):
```
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
```

Configure the ADS1248 spi bus with ADS1248.setup():
```
ADS1248.setup(spi, board.D33, board.D35, freq=2000000)
```

Now you will create your individual ADC objects, each object will represent a seperate ADC. If you only have 1 ADC you still must create an ADC object:
```
adc = ADS1248(board.D31, board.D37, vref=2.048)
```

To communicate with a single ADC object, simply apply methods to the object:
```
adc.wakeup()
adc.wreg(2,[0x30,0x00]) # Write register 2 with 0x30 (configure vref) and register 3 with 0x00 (conversion rate)
print(adc.rreg(0,16)) # Read all registers
```


To communicate with all ADC objects, use the "All" methods and apply them to the ADS1248 class:
```
ADS1248.fetchAll(0,[0,2])
```
Refer to the wiki for a detailed list of all available methods.
