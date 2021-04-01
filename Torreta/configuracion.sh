sudo apt update
sudo apt upgrade
Y
sudo apt install python3-pip
Y
sudo apt instasll python3.7
Y
python3.7 -m pip install pip
Y
python3.7 -m pip install numpy scipy matplotlib ipython pandas sumpy nose
sudo apt install git
Y

sudo apt-get install libxml2 libxml2-dev bison flex libcdk5-dev cmake

git clone https://github.com/analogdevicesinc/libiio.git
cd libiio
cmake ./
make all -j4
sudo make install
sudo ldconfig
cd bindings/python/
sudo python3.7 setup.py.cmakein install
cd ..


git clone https://github.com/analogdevicesinc/libad9361-iio.git
cd libad9361-iio
cmake ./
make -j3
sudo make install
cd ..

git clone https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
sudo python3.7 setup.py install
