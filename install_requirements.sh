#/bin/bash

# install gmp for large number
rm ./gmp-6.2.1.tar.xz;

wget https://gmplib.org/download/gmp/gmp-6.2.1.tar.xz;
tar xvf ./gmp-6.2.1.tar.xz;
cd ./gmp-6.2.1;
sudo ./configure;
sudo make;
sudo make install;

cd ..;
sudo rm -r ./gmp-6.2.1;
