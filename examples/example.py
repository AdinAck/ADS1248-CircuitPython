import board
import digitalio
import busio
from ADS1248 import ADS1248

# Initialize SPI
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# ADS1248
ADS1248.setup(spi, board.D33, board.D35, freq=2000000) # Set up spi, start pin, etc
adc = ADS1248(board.D31, board.D37) # Define ADC objects
# Declare more ADC's (if applicable) here
ADS1248.verbose = True

# Send commands to individual ADC
adc.wakeup()
adc.wreg(2,[0x30,0x00]) # Write register 2 with 0x30 (configure vref) and register 3 with 0x00 (conversion rate)
print(adc.rreg(0,16)) # Read all registers

# Read inputs A0 and A2 in relation to A0 and convert to voltage from all ADC objects
print(ADS1248.fetchAll(0,[0,2]))
