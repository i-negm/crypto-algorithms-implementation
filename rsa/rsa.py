
import random

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
  n = exp
  while (n != 0):
    r = n % 2     # Check if the current base is 1 or 0
    if (r == 1):
      a = (a * c) % mod     # Accumelate the value
    n = int(n / 2)          # For the next digit (in binary)
    c = (c * c) % mod       # Calculate the square to be used in next step
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

def is_prime(num):
  for i in range(0,9):
    temp_random = random.randrange(0, num)
    if (euclid_gcd(temp_random, num) != 1):
      return False
  return True # Survived 10 tests -> propably prime

def get_rand_large_prime(key_size = 1024):
  found_prime = False
  while (found_prime == False):
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
  print("r/p = ", r, "/", p)
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
  return (r ** ((p-1) / 2)) % p

'''
  Encryption
'''
def calc_n(p, q):
  return p*q

