
import random
import sys
from enum import Enum
from numpy import random as rnd

import math

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
  a = 1               # Accumelator of the value
  c = base
  # print(mod)
  # print(sys.getsizeof(mod))
  # print(type(mod))
  n = exp
  while (n != 0):
    r = n % 2     # Check if the current base is 1 or 0
    # if(r == 1): print(f"a*c % mod = {(a * c) % mod}")
    if (r == 1):
      a = (a * c) % mod     # Accumelate the value
    n = n // 2              # For the next digit (in binary)
    c = (c * c) % mod       # Calculate the square to be used in next step
    # print(f"r = {r}, a = {a}, n = {n}, c = {c}")
  return a

def gcd_euclidean(a, b):
  '''
    Section 4.3: Euclidean Algorithm 
    https://mathstats.uncg.edu/sites/pauli/112/HTML/seceuclid.html#seceuclid
  '''
  if (b > a):
    temp = a
    a = b
    b = temp

  # Special cases
  if (b == 0): return a

  r = 1 # init r to be used in condition (to any value, will be overwritten)
  while (r != 0):
    r = a % b
    a = b
    b = r
  return a

def fermat_test(n):
  '''
    Probabilistic Algorithm i.e. returns either composite or propably prime
  '''
  # All even numbers are composites
  if (n % 2 == 0):
    return Primality.Composite
  # Generate uniformly distributed number over the range [2, n-2]
  r_lst = [int(x) for x in (rnd.uniform(low=2, high=n-2, size=10))]
  # fermat condition (b)
  for r in r_lst:
    # b = (a**(n-1)) % n # Takes forever !!!
    b = fast_exp_mod(r, n-1, n)
    # b = pow(r, n-1, n)
    # print(f"r = {r}, exp = {n - 1}, mod = {n} => result = {b}")
    if (b != 1):
      return Primality.Composite
  # After finishing testing against all the random generated integers
  return Primality.ProbablyPrime


def is_prime(num):
  # Generate uniformly distributed number over the range [2, n-2]
  r_lst = [int(x) for x in (rnd.uniform(low=2, high=num-2, size=10))]
  for r in r_lst:
    if (gcd_euclidean(num, r) != 1):
      return False
  # Run the fermat test also
  if (fermat_test(num) == Primality.Composite):
    return False
  return True # Survived 10 tests -> propably prime

def get_rand_large_prime(key_size = 1024):
  while (True):
    num = random.randrange(2 ** (key_size - 1), 2 ** (key_size))
    if (is_prime(num)):
      return num

def generate_primes(key_size = 1024):
  p = get_rand_large_prime(key_size)
  q = get_rand_large_prime(key_size)
  return (p, q)

def calc_jacobian(r, p):
  '''
    r = random number > p
    p = prime number
  '''
  # print("r/p = ", r, "/", p)
  if (r == 1):
    return 1
  elif (r % 2 == 0): # even
    return calc_jacobian(r/2, p) * (-1) ** (((p*p) - 1) / 8)
  else: # odd
    return calc_jacobian((p % r), r) * (-1) ** (((r - 1) * (p - 1)) / 4)

def calc_euler_criterion(r, p):
  '''
    @ref https://en.wikipedia.org/wiki/Euler%27s_criterion
    @ref Slide 10 CIT 620 RSA
  '''
  return pow(r, int((p-1)/2), p)

def jacobian_euler_test(num):
  # Generate uniformly distributed number over the range [2, n-2]
  r_lst = [int(x) for x in (rnd.uniform(low=2, high=num-2, size=10))]
  for r in r_lst:
    print(calc_jacobian(r, num))
    print(calc_euler_criterion(r, num))

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

def xgcd_iterative(a, b):
   """ Calculates the gcd and Bezout coefficients, 
   using the Extended Euclidean Algorithm (non-recursive).
   (Source: extendedeuclideanalgorithm.com/code) 
   """
   #Set default values for the quotient, remainder, 
   #s-variables and t-variables
   q = 0
   r = 1
   s1 = 1 
   s2 = 0
   s3 = 1 
   t1 = 0 
   t2 = 1
   t3 = 0
   
   '''
   In each iteration of the loop below, we
   calculate the new quotient, remainder, a, b,
   and the new s-variables and t-variables.
   r decreases, so we stop when r = 0
   '''
   while(r > 0):
      #The calculations
      q = math.floor(a/b)
      r = a - q * b
      s3 = s1 - q * s2
      t3 = t1 - q * t2
      
      '''
      The values for the next iteration, 
      (but only if there is a next iteration)
      '''
      if(r > 0):
         a = b
         b = r
         s1 = s2
         s2 = s3
         t1 = t2
         t2 = t3

   return abs(b), s2, t2

def multinv(b, n):
   """
   Calculates the multiplicative inverse of a number b mod n,
   using the Extended Euclidean Algorithm. If b does not have a
   multiplicative inverse mod n, then throw an exception.
   (Source: extendedeuclideanalgorithm.com/code)
   """
   
   #Get the gcd and the second Bezout coefficient (t)
   #from the Extended Euclidean Algorithm. (We don't need s)
   my_gcd, _, t = xgcd_iterative(n, b)
   
   #It only has a multiplicative inverse if the gcd is 1
   if(my_gcd == 1):
      return t % n
   else:
      raise ValueError('{} has no multiplicative inverse modulo {}'.format(b, n))

def calc_d(e, phi):
  d = modInverse(e, phi)
  # d = multinv(e, phi)
  # d = multinv(phi, e)
  return d

def decrypt(c, private_key):
  d, phi = private_key
  m = fast_exp_mod(c, d, phi)
  return m