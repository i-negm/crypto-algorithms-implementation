
import random

'''
  Helper Functions
'''
def get_rand_bits(bits):
  return random.getrandbits(bits)

'''
  Random Prime Numbers
'''
# 1. Primality Test
# 1.a. Euclidian GCD (m, n)

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
  

def calc_n(p, q):
  return p*q