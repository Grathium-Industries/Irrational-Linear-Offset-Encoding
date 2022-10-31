#include <iostream>
#include <gmp.h>
 
#include "./includes/main.h"
#include "numbers.cpp"

int main(int argc, char **argv) {
  const int scalar_value = 5;

  mpz_t value;
  mpz_t scalar;

  mpz_init(value);
  mpz_set_ui(value, irrationalNumberGenerator());

  mpz_init(scalar);
  mpz_set_ui(scalar, scalar_value);

  mpz_mul(value, value, scalar);

  std::cout << mpz_out_str(stdout,10,value) << std::endl;

  return 0;
}
