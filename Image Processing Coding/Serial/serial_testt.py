import serial

port =serial.Serial('/dev/tty.usbserial-110', 9600, timeout=1)
while True:
    data_input=input("Ledi yakmak için 'a' harfine basın söndürmek için 'b' harfine basın")
    if data_input== 'a':
        port.write(bytes('a','utf-8'))
    elif data_input== 'b':
        port.write(bytes('b','utf-8'))