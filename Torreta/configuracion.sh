sudo apt update
sudo apt upgrade
Y
sudo apt-get purge python3:i386
sudo apt autoremove
sudo apt update
Y
sudo apt install git
Y
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
tar -xf Python-3.8.0.tgz
cd Python-3.8.0
./configure --enable-optimizations
make -j 8
sudo make altinstall
cd ..
sudo apt install python3-pip
pip install --upgrade "pip < 21.0"
pip3 install numpy scipy matplotlib ipython pandas sumpy nose
pip3 install libiio
git clone https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
sudo python3 setup.py install
