#Hardware utilizados:
#Sick_tim551-2050001
#ch robotics um6
#gps ultimate breakout v3 adafruit
#Raspberry 2-b
#Pionner AT
#Adaptador wifi tp-link wn722n

#Arquivos necessários:
#trouble.rules para mapear as portas usb
#trouble para criar uma rede wifi
#trouble.launch que é o launcher do trouble
#comandos_trouble.py que possui os comandos utilizados via mqtt

#sources do mosquitto e do ros
sudo apt-add-repository -y ppa:mosquitto-dev/mosquitto-ppa

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116

#Programas/dependências
sudo apt-get update

sudo apt-get install -y git

sudo apt-get install -y openssl

sudo apt-get install -y ssh

#instalação do ros
sudo apt-get install -y ros-indigo-desktop

sudo rosdep init

rosdep update

echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc

source ~/.bashrc

#pacotes do mqtt, python e ros
sudo apt-get install -y mosquitto

sudo apt-get install -y mosquitto-clients

sudo apt-get install -y libmosquitto-dev

sudo apt-get install -y python-rosinstall

sudo apt-get install -y python-pip

sudo pip install paho-mqtt

sudo apt-get install -y libaria*

sudo apt-get install -y ros-indigo-geographic-info

sudo apt-get install -y ros-indigo-um6

sudo apt-get install -y ros-indigo-sick-tim

sudo apt-get install -y ros-indigo-nmea-*

#criação do catkin
mkdir -p ~/catkin_tb/src

cd ~/catkin_tb/src

git clone https://github.com/amor-ros-pkg/rosaria.git

git clone https://github.com/pengtang/rosaria_client.git

git clone https://github.com/cra-ros-pkg/robot_localization.git -b indigo-devel

catkin_create_pkg launchers rospy roscpp

cd launchers

mkdir launch

#TODO: renato, acho q está errado aqui. da onde vem este arquivo .launch 
# acho q vc esqueceu de dizer onde esta este repo hratc2017_robot
mv ~/trouble.launch ~/catkin_t/src/launcher/launch/trouble.launch

cd ~/catkin_t

catkin_make

# TODO: aqui vc está assumindo q o username eh trouble.
echo "source /home/trouble/catkin_tb/devel/setup.bash" >> ~/.bashrc

#configurações de internet, mapeamento usb e comandos via mqtt ao iniciar
cd ~

#TODO: ler do repo hratc2017_robot !
sudo mv ~/trouble etc/NetworkManager/system-connections/trouble

sudo mv ~/trouble.rules /etc/udev/rules.d/trouble.rules

sudo chmod 777 ~/comandos_trouble.py

sudo sh -c 'echo "sleep 10\n./home/trouble/comandos_trouble.py" > /etc/rc.local'
