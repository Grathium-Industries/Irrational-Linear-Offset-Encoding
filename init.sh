#!/bin/bash

rm ./src/includes/InfInt.h;
wget https://raw.githubusercontent.com/sercantutar/infint/master/InfInt.h;
mv ./InfInt.h ./src/includes/InfInt.h;
