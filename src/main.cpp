#include <iostream>

#include "./includes/main.h"
#include "./includes/InfInt.h"

#include "numbers.cpp"

int main(int argc, char **argv) {
    InfInt base = findPi("643897589");

    std::cout << base << std::endl;
    return 0;
}
