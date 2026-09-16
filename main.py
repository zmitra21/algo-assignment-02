"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
Zack Mitra
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def quadratic_multiply(x, y):
    ### TODO
    if len(x.binary_vec) == 1 or len(y.binary_vec) == 1:
        return x.decimal_val * y.decimal_val
    x_bits = ''.join(x.binary_vec)
    y_bits = ''.join(y.binary_vec)
    n = max(len(x_bits), len(y_bits))
    x_bits = x_bits.zfill(n)
    y_bits = y_bits.zfill(n)

    if n % 2 != 0:
        n += 1
        x_bits = x_bits.zfill(n)
        y_bits = y_bits.zfill(n)
    mid = n // 2
    x_L = BinaryNumber(int(x_bits[:mid], 2))
    x_R = BinaryNumber(int(x_bits[mid:], 2))
    y_L = BinaryNumber(int(y_bits[:mid], 2))
    y_R = BinaryNumber(int(y_bits[mid:], 2))

    P1 = quadratic_multiply(x_L, y_L)
    P2 = quadratic_multiply(x_R, y_R)   
    P3 = quadratic_multiply(x_L, y_R)
    P4 = quadratic_multiply(x_R, y_L)

    return (2 ** n) * P1 + (2 ** mid) * (P3 + P4) + P2 # From formula

    pass
    ###

def subquadratic_multiply(x, y):
    ### TODO
    if len(x.binary_vec) == 1 or len(y.binary_vec) == 1:
        return x.decimal_val * y.decimal_val

    x_bits = ''.join(x.binary_vec)
    y_bits = ''.join(y.binary_vec)

    n = max(len(x_bits), len(y_bits))
    x_bits = x_bits.zfill(n)
    y_bits = y_bits.zfill(n)

    if n % 2 != 0:
        n += 1
        x_bits = x_bits.zfill(n)
        y_bits = y_bits.zfill(n)

    mid = n // 2

    x_L = BinaryNumber(int(x_bits[:mid], 2))
    x_R = BinaryNumber(int(x_bits[mid:], 2))
    y_L = BinaryNumber(int(y_bits[:mid], 2))
    y_R = BinaryNumber(int(y_bits[mid:], 2))
    P1 = subquadratic_multiply(x_L, y_L)
    P2 = subquadratic_multiply(BinaryNumber(x_L.decimal_val + x_R.decimal_val), BinaryNumber(y_L.decimal_val + y_R.decimal_val))
    P3 = subquadratic_multiply(x_R, y_R)
    middle = P2 - P1 - P3

    return (2 ** n) * P1 + (2 ** mid) * middle + P3


    pass
    ###

def time_multiply(x, y, f):
    start = time.time()
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    bit_sizes = [4, 8, 16, 32, 64, 128, 256]
    for n in bit_sizes:
        value = (2**n) - 1
        x = BinaryNumber(value)
        y = BinaryNumber(value)
        quadratic_time = time_multiply(x, y, quadratic_multiply)
        subquadratic_time = time_multiply(x, y, subquadratic_multiply)
        print("bits =", n, "quadratic =", quadratic_time, "ms", "subquadratic =", subquadratic_time, "ms")

    # compare the empirical runtimes of multiplication functions
    ### TODO - add test cases and measure runtime
    
    
compare_multiply()
