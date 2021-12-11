
import random

'''
  Helper Functions
'''
def get_rand_bits(bits):
  return random.getrandbits(bits)


'''
  Random Prime Numbers
   1. Primality Test
     1.a. Euclidian GCD (m, n) == 1
     1.b. Primility Test for Jacobian and Euler Equation
'''
def euclid_gcd(m, n):
  #
  # @ref : Slide 15 CIT 620
  #
  # Assume the equation
  #  m_lst = div * quotient_lst + remainder_lst; m > n

  # Sanity check m > n
  if (n < m):
    temp = m
    m = n
    n = temp

  # Using arrays as a way to hold the division steps
  remainder_lst = []
  quotient_lst = []
  m_lst = []

  # For the first time the remainder_lst = n (second smaller number)
  m_lst.append(m)
  remainder_lst.append(m_lst[0] % n)
  quotient_lst.append(n)                          # In next rounds it will be remainder[i-1]
  div = m_lst[0] // quotient_lst[0]

  i = 0
  while (remainder_lst[i] != 0):                     # Continue until remainder = 0
    # Each round
    i = i+1
    # 1.a. Shift previous step remainder_lst into current step quotient_lst
    quotient_lst.append(remainder_lst[i-1])
    # 1.b. Shift previous step quotient_lst into current m_lst
    m_lst.append(quotient_lst[i-1])
    # 2. Calculate current div
    div = m_lst[i] // quotient_lst[i]
    # 3. Calculate current remainder_lst
    remainder_lst.append(m_lst[i] % quotient_lst[i])  
  return remainder_lst[i-1]

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

