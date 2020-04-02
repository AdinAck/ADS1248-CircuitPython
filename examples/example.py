import board
import digitalio
import busio
from ADS1248 import ADS1248

# Initialize SPI
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
while not spi.try_lock():
    pass
spi.configure(baudrate=2000000, phase=1, polarity=0)

# ADS1248
adc = ADS1248(board.D31, board.D37) # Define ADC objects first
# Declare more ADC's (if applicable) here
ADS1248.init(spi, board.D33, board.D35) # Initialize ADC group

# Send commands to individual ADC
adc.wakeup()
adc.wreg(2,[0x30,0x00]) # Write register 2 with 0x30 (configure vref) and register 3 with 0x00 (conversion rate)
adc.rreg(0,16) # Read all registers

ADS1248.verbose = True

# Read inputs A0 and A2 in relation to A0 and convert to voltage from all ADC objects
print([2.048/(2**23)*i+2.048 for i in ADS1248.fetchAll(0,[0,2])])
