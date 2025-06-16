import pigpio
import time

# Create a pigpio object
pi = pigpio.pi()

# Check if pigpio is running
if not pi.connected:
    exit()

SERVO_GPIO = 18  # Change this to your GPIO pin

# Set pulse width in microseconds (e.g., 1000 - 2000 us for standard servo)
# 1500 us is typically center
try:
    while True:
        print("Moving to 0°")
        pi.set_servo_pulsewidth(SERVO_GPIO, 1000)  # 0 degrees
        time.sleep(1)

        print("Moving to 90°")
        pi.set_servo_pulsewidth(SERVO_GPIO, 1500)  # 90 degrees (center)
        time.sleep(1)

        print("Moving to 180°")
        pi.set_servo_pulsewidth(SERVO_GPIO, 2000)  # 180 degrees
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Turn off servo
pi.set_servo_pulsewidth(SERVO_GPIO, 0)

# Disconnect
pi.stop()
