# Example file for Programming Foundations: Algorithms by Joe Marini
# Find the greatest common denominator of two numbers
# using Euclid's algorithm

# Logic: 
# 1. For two integers a and b, where a > b, divide a by b
# 2. If the remainder, r, is 0 then stop: GCD is b. 
# 3. Otherwise, set a to b, b to r, and repeat at step 1 until r is 0.

def gcd(a, b):
    while(b != 0): # gcd of 20 and 8 is 4
        t = a # store the value of a in a temporary variable
        print("t=",t)
        a = b # set a equal to b (in case there is another loop)
        print("a=",a)
        b = t % b # recalculate b to be the remainder of a divided by b
        print("b=",b)
        # if b is now zero, the loop will stop
        # otherwise, a becomes b, and b becomes the remainder for the next loop
    return a


# try out the function with a few examples
print(gcd(60, 96))  # should be 12
print(gcd(20, 8))   # should be 4
