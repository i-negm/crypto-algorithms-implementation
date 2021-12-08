# Adding the current path for the PATH variable to be able to import external files/modules
import sys, os
path = os.getcwd()
abspath = os.path.abspath(path) 
sys.path.append(abspath)

# Imports
import rsa

def test_calc_n__it_generates_n__equals_pq():
  PRIME_1 = 61
  PRIME_2 = 53
  assert rsa.calc_n(PRIME_1, PRIME_2) == 3233

def test_get_rand_bits__it_generates_not_equal_numbers():
  # Arrange
  rand1 = rsa.get_rand_bits(1024)
  # Act
  rand2 = rsa.get_rand_bits(1024)
  # Assert
  assert rand1 != rand2

def test_euclid_gcd__it_finds_eculid_gcd():
  # Arrange
  expected = 17
  m = 323
  n = 238
  # Act
  actual = rsa.euclid_gcd(m,n)
  # Assert
  assert actual == expected

def test_euclid_gcd__it_finds_eculid_gcd_for_rearranged_parameters():
  # Arrange
  expected = 17
  m = 238
  n = 323
  # Act
  actual = rsa.euclid_gcd(m,n)
  # Assert
  assert actual == expected

