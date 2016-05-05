import time

import RPi.GPIO as GPIO
import spidev

from Main import NRF24


class Transceiver():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]
        
        self.radio = NRF24(GPIO, spidev.SpiDev())
        self.radio.begin(0, 17)
        
        self.radio.setPayloadSize(32)
        self.radio.setChannel(0x76)
        self.radio.setDataRate(NRF24.BR_1MBPS)
        self.radio.setPALevel(NRF24.PA_MIN)
        
        self.radio.setAutoAck(True)
        self.radio.enableDynamicPayloads()
        self.radio.enableAckPayload()
        
        self.radio.openWritingPipe(pipes[0])
        self.radio.openReadingPipe(1, pipes[1])
        
    def __send__(self, message):
        m = list(message)

        while len(m) < 32:
            m.append(0)

        return self.radio.write(m)

    def __read__(self):
        start = time.time()
        self.radio.startListening()

        while not self.radio.available(0):
            time.sleep(0.01)
            if time.time() - start > 2:
                print("Timed out.")
                break

        receivedMessage = []

        self.radio.read(receivedMessage, self.radio.getDynamicPayloadSize())
        if receivedMessage is not 0:
            print("Received: {}".format(receivedMessage))
            self.radio.stopListening()
