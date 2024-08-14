import pyfirmata
 
comport = 'COM3'
board = pyfirmata.Arduino(comport)

# Define motor control pins
motor_speed = board.get_pin('d:10:p')  # PWM pin for motor speed

def moter_control(fingerUp):
    if fingerUp == [0, 0, 0, 0, 0]:
        motor_speed.write(0)  # Motor off

    elif fingerUp == [1, 0, 0, 0, 0]:
        motor_speed.write(0.3)  # Motor on at low speed

    elif fingerUp == [0, 1, 0, 0, 0]:
        motor_speed.write(0.6)  # Motor on at medium speed

    elif fingerUp == [1, 1, 1, 1, 1]:
        motor_speed.write(1)  # Motor on at high speed

fingerUp = [1, 0, 0, 0, 0]
moter_control(fingerUp)
