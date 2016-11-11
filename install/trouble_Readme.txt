Esse script tem como finalidade apresentar a configuração de software do pionner-AT.

Sensores:

Sick_tim551-2050001
  ch robotics um6
  gps ultimate breakout v3 adafruit
  Raspberry 2-b
  Pionner AT
  Adaptador wifi tp-link wn722n


Distancia em relação ao centro do pionner-AT(metros):
  Sick_tim551-2050001 -> [-0.03 -0.11 0.41]
  ch robotics um6 -> [-0.03 0 0.41]
  gps ultimate breakout v3 adafruit -> [-0.03 0.11 0.41]

Pré-instalação raspberry:
  ubuntu 14.04.LTS trusty (https://wiki.ubuntu.com/ARM/RaspberryPi)
  interface gráfica lubuntu (lubuntu-desktop)
  atualize o sistema

Arquivos auxiliares:
  trouble.rules -> mapeia as portas usb, utilizando id_Vendor, id_Product e Serial dos sensores. Esse está configurado com os produtos que utilizamos, ou seja, precisa ser configurado se for usado com outros produtos.

  trouble -> cria uma rede wifi própria com o nome de trouble.
  
  trouble.launch -> launcher do trouble
  
  comandos_trouble.py -> possui alguns comandos pré-fixados para o pionner via mqtt.

Se os ajustes acima forem feitos, aí executamos o script que ele fará a instalação criando a pasta catkin_t. Onde terão os dados da pioner. Então é só executar o launch:

roslaunch launchers trouble.launch