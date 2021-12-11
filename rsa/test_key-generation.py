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

def test__calc_jacobian():
  # Arrange
  expected = -1
  r = 1001
  p = 9907
  # Act
  actual = rsa.calc_jacobian(r, p)
  # Assert
  assert actual == expected

def test__gcd_euclidean():
  assert rsa.gcd_euclidean(612, 56)        == 4
  assert rsa.gcd_euclidean(56, 612)        == 4
  assert rsa.gcd_euclidean(120, 30)        == 30
  assert rsa.gcd_euclidean(238, 237)       == 1
  assert rsa.gcd_euclidean(132, 84)        == 12
  assert rsa.gcd_euclidean(177855, 177856) == 1
  assert rsa.gcd_euclidean(105, 165)       == 15
  assert rsa.gcd_euclidean(939764, 1)      == 1
  assert rsa.gcd_euclidean(950218, 0)      == 950218
  assert rsa.gcd_euclidean(9653, 9653)     == 9653

def test__fast_exp_mod():
  assert rsa.fast_exp_mod(3, 18, 29)       == 6
  assert rsa.fast_exp_mod(7, 66, 101)      == 30
  assert rsa.fast_exp_mod(4, 25, 53)       == 40

