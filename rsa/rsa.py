
import random
from enum import Enum
from numpy import random as rnd

'''
  User Defined Types
'''
class Primality(Enum):
  Composite = 0
  ProbablyPrime = 1
  Prime = 2

'''
  Helper Functions
'''
def get_rand_bits(bits):
  return random.getrandbits(bits)


def fast_exp_mod(base, exp, mod):
  '''
  Problem 15.3.4: Fast exponentiation given certain powers
  https://mathstats.uncg.edu/sites/pauli/112/HTML/secfastexp.html#exfastexp47
  '''
  a = 1               # Accumelator of the value (Final value will be in it)
  c = base
  n = exp
  while (n != 0):
    r = n % 2               # Check if the current digit is 1 or 0 (2 base)
    if (r == 1):
      a = (a * c) % mod     # Accumelate the value
    n = n // 2              # For the next digit (in binary)
    c = (c * c) % mod       # Calculate the square to be used in next step
  return a

def gcd_euclidean(a, b):
  '''
    Section 4.3: Euclidean Algorithm 
    https://mathstats.uncg.edu/sites/pauli/112/HTML/seceuclid.html#seceuclid
  '''
  # Arrange the elements (for usability)
  if (b > a):
    temp = a
    a = b
    b = temp

  # Special cases
  if (b == 0): return a

  r = 1 # init r to be used in condition (to any value, will be overwritten)
  while (r != 0):
    # Calculate the remainder in each step
    r = a % b
    # Shift the numbers
    a = b
    b = r
  return a

def fermat_test(n, r_lst):
  '''
    Probabilistic Algorithm i.e. returns either composite or propably prime
  '''
  # All even numbers are composites
  if (n % 2 == 0):
    return Primality.Composite
  
  # fermat condition (b)
  for r in r_lst:
    b = fast_exp_mod(r, n-1, n)
    if (b != 1):
      return Primality.Composite
  # After finishing testing against all the random generated integers
  return Primality.ProbablyPrime


def is_prime(num):
  # Generate uniformly distributed number over the range [2, n-2]
  r_lst = [int(x) for x in (rnd.uniform(low=2, high=num-2, size=10))]

  # The random numbers and the number under test should be coprimes
  for r in r_lst:
    if (gcd_euclidean(num, r) != 1):
      return False
  
  # Run the fermat test also
  if (fermat_test(num, r_lst) == Primality.Composite):
    return False
  
  return True # Survived 10 tests -> propably prime

def get_rand_large_prime(key_size = 512):
  while (True):
    # Get a random number between 2^(keysize-1) : 2^(keysize)
    num = random.randrange(2 ** (key_size - 1), 2 ** (key_size))
    # Check if this num is prime
    if (is_prime(num)):
      return num

def generate_primes(key_size = 512):
  p = get_rand_large_prime(key_size)
  q = get_rand_large_prime(key_size)
  return (p, q)

def calc_n(p, q):
  return p*q

def calc_phi_n(p, q):
  return (p - 1) * (q - 1)

def calc_e(phi_n):
  while (True):
    r = random.randrange(phi_n // 2, phi_n - 1)
    if (gcd_euclidean(phi_n, r) == 1): # Found the co-prime with phi_n
      return r

def encrypt(m, key):
  e, n = key
  c = fast_exp_mod(m, e, n)
  return c

def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
    # Make x positive
    if (x < 0):
        x = x + m0
    return x

def calc_d(e, phi):
  d = modInverse(e, phi)
  return d

def decrypt(c, private_key):
  d, phi = private_key
  m = fast_exp_mod(c, d, phi)
  return m