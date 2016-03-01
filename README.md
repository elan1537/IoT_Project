# IoT_Project in Home

집에서 웹페이지를 통해 손쉽게 **전등을 끄고 킬 수** 있는 사물인터넷 프로젝트
라즈베리파이와 아두이노를 사용하여 간단하게 제어가능하게 만들기


## 사용된 도구
1. 릴레이 스위치
2. Touch Sensor
3. nRF24L01 Transceiver * 2

## Board
1. Raspberry Pi2
2. Arduino Nano(호환보드)

## 사용언어
1. Python 3.4
2. Arduino C++

##NRF24L01 Pin Number


| 종류  | VCC | GND | CSN | CE | MOSI | MISO | SCLK |
|------|----|-----|-----|-----|-----|------|-------|
| 아두이노 | 3V3 | GND | D10 | D9 | D11 | D12 | D13 |
| 라즈베리 | 1 | 6 | 24 | 11 | 19 | 21 | 23 | 

-


###참고
> NRF24L01로 라즈베라피이 아두이노 양방향 통신하기 <https://www.youtube.com/watch?v=_68f-yp63ds>

