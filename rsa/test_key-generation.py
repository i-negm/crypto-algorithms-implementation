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