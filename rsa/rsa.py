'''
  Random Prime Numbers
'''

# 1. Primality Test
# 1.a. Euclidian GCD

def euclid_gcd(m, n):
  #
  # @ref : https://djangocentral.com/gcd-using-euclid-algorithm-in-python/
  # 
  # Assuming m = n*q + r ; q: quotient and r: reminder
  #
  # Rearrange the m,n if n > m
  temp = 0
  if (n > m):
    temp = n
    n = m
    m = temp
  r = m % n
  while(r != 0):
      m = n
      n = r
      q = int(m / n)
      r = m % n
  return r

def calc_n(p, q):
  return p*q