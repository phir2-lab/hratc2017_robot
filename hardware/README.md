# Hardware Spec

This is a list of used resources:

- [Pionner P3-AT](http://www.mobilerobots.com/ResearchRobots/P3AT.aspx)
- [IMU ch robotics um6](http://www.chrobotics.com/shop/orientation-sensor-um6)
- [GPS ultimate breakout v3 adafruit](https://www.adafruit.com/product/746)
- [Raspberry 2-b](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/)
- [Adaptador wifi tp-link wn722n](http://www.tp-link.com/en/download/TL-WN722N.html)
- [Laser Sick_tim551-2050001](https://www.sick.com/us/en/detection-and-ranging-solutions/2d-laser-scanners/tim5xx/tim551-2050001/p/p343045). Top laser.
- [Laser Hokuyo URG-04LX-UG01](https://www.hokuyo-aut.jp/02sensor/07scanner/urg_04lx_ug01.html). Bottom laser, facing downwards.
- [Metal detector](https://github.com/ras-sight/metal_detector_msgs)

And these are the power and interface resources:
- [USB 2.0 powered hub](https://www.adafruit.com/products/961)
- [voltage converter]()
- [FTDI adapter]()


The software running on the Raspberry Pi is described in the install directory.

# Sensor Position

The sensor are placed on top of the support described in the model directory.
The following images show the position of each sensor.

**Renato, pegar screenshots do cavalete e colocar as dimensoes em relacao ao centro do robo
e outras dimensoes relavantes na imagem**

# Communication Ports
  # These are the ports mapping the sensors in the CPU:
  - Sick laser: recognized automatically
  - GPS: /dev/gps
  - IMU: /dev/imu
  - Metal detector: recognized automatically
  - Robot base: /dev/rosaria

# Power Distribution

 # from robot:
 - Sick laser: 12v
 - GPS:  5v
 - IMU:  5v
 - Metal detector: 12v
 - Robot base: 12v
 - USB hub: 5v
 - wifi: 5v

 # from own battery(Power 4200mah 12v):
 - Raspberry PI: 5v

# Simplified Schematics

**renato, colocar um esquemático simplificado. Pode ser fritizing**


