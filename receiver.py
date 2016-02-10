"""
    Physical

    1. GND => 9
    2. 3V3 => 1
    3. CE => 26
    4. CSN => 28
    5. SCKL => 23
    6. MOSI => 19
    7. MISO => 21
    8. IRQ => none

    아두이노로 부터 JSON형식으로 된 데이터를 받아옴

"""
from lib_nrf24 import NRF24
import RPi.GPIO as GPIO
import time
import spidev

pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

GPIO.setmode(GPIO.BCM)

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(1, 7)
radio.setPayloadSize(32)
radio.setChannel(0x60)

radio.setDataRate(NRF24.BR_2MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe(1, pipes[1])
radio.printDetails()

radio.startListening()

while True:
    ackPL = [1]

    while not radio.available(1):
        time.sleep(100)

    receivedMessage = []
    radio.read(receivedMessage, radio.getDynamicPayloadSize())
    print("Received {}".format(receivedMessage))

    print("Translating the receivedMessage into unicode characters...")
    string = ""

    for i in receivedMessage:
        if 32 <= i <= 126:
            string += chr(i)
    print(string)

    radio.writeAckPayload(1, ackPL, len(ackPL))
    print("Loaded payload reply of {}".format(ackPL))
