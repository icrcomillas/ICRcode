sudo apt update
sudo apt upgrade
Y
sudo apt-get purge python3:i386
sudo apt autoremove
sudo apt update
Y
sudo apt install git
Y
sudo apt instasll python3.7
sudo apt install python3-pip
pip install --upgrade "pip < 21.0"
pip3 install numpy scipy matplotlib ipython pandas sumpy nose
sudo apt-get install git libxml2 libxml2-dev bison flex libcdk5-dev cmake python3-pip

git clone https://github.com/analogdevicesinc/libiio.git
cd libiio
cmake ./
make all -j4
sudo make install
sudo ldconfig
cd bindings/python/
sudo python3 setup.py.cmakein install
cd ..


git clone https://github.com/analogdevicesinc/libad9361-iio.git
cd libad9361-iio
cmake ./
make -j3
sudo make install
cd ..

git clone https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
sudo python3 setup.py install
