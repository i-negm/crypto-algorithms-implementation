# Adding the current path for the PATH variable to be able to import external files/modules
import sys, os
path = os.getcwd()
abspath = os.path.abspath(path) 
sys.path.append(abspath)

# Imports
import rsa
from rsa import Primality

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
  # Larger numbers
  assert rsa.fast_exp_mod(457, 87457, 7987) == 5042

def test__fermat_test():
  prime_nums_lst = [838815654613746928755205315544445789313427350147837793096447, 6143, 51539607551, 108086391056891903, 108086391056891903, 227344844511754081845528645625545486374491 ]
  for num in prime_nums_lst:
    assert rsa.fermat_test(num) == Primality.ProbablyPrime

def test__fermat_test():
  prime_nums_lst = [838815654613746928755205315544445789313427350147837793096447, 6143, 51539607551, 108086391056891903, 108086391056891903, 227344844511754081845528645625545486374491 ]
  for num in prime_nums_lst:
    assert rsa.is_prime(num) == True

# def test__jacobian_euler_test():
#   prime_nums_lst = [838815654613746928755205315544445789313427350147837793096447, 6143, 51539607551, 108086391056891903, 108086391056891903, 227344844511754081845528645625545486374491 ]
#   for num in prime_nums_lst:
#     print(rsa.jacobian_euler_test(num))

def test__generate_large_primes():
  p, q = rsa.generate_primes(512)
  assert (rsa.is_prime(p) == True and rsa.is_prime(q) == True)
  print(p,q)

def test_calc_n__it_generates_n__equals_pq():
  p, q = rsa.generate_primes(1024)
  assert rsa.calc_n(p, q) == p * q

def test__calc_phi_n__and__calc_e():
  p, q = rsa.generate_primes(1024)
  phi_n = rsa.calc_phi_n(p, q)
  e = rsa.calc_e(phi_n)
  assert phi_n == (p - 1) * (q - 1)
  assert rsa.gcd_euclidean(phi_n, e) == 1 , "Should be coprimes"

def test__encryption_small():
  msg = 123
  print("msg", msg)
  p, q = rsa.generate_primes(10)
  print("p", p)
  print("q", q)
  phi_n = rsa.calc_phi_n(p, q)
  print("phi_n", phi_n)
  n = rsa.calc_n(p,q)
  print("n", n)
  e = rsa.calc_e(phi_n)
  print("e", e)
  c = rsa.encrypt(msg, (e, n))
  print("c", c)
  d = rsa.calc_d(e, phi_n)
  print("d", d)
  m = rsa.decrypt(c, (d, n))
  print("m", m)
  assert m == msg

def test__encryption_big():
  msg = 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
  print("msg", msg)
  p, q = rsa.generate_primes(512)
  print("p", p)
  print("q", q)
  phi_n = rsa.calc_phi_n(p, q)
  print("phi_n", phi_n)
  n = rsa.calc_n(p,q)
  print("n", n)
  e = rsa.calc_e(phi_n)
  print("e", e)
  c = rsa.encrypt(msg, (e, n))
  print("c", c)
  d = rsa.calc_d(e, phi_n)
  print("d", d)
  m = rsa.decrypt(c, (d, n))
  print("m", m)
  assert m == msg