def gcf_euclid_explainable(a, b):
    """
    Find GCF using Euclid's algorithm:
    Apply the observation that GCF(a, b) == GCF(b, a % b).
    """

    a, b = abs(a), abs(b) # handle negative input
    
    while b != 0: # while a is not a common factor of both a and b,
        remainder = a % b # store remainder of a / b (also divisible by GCF)
        a = b # replace a with b
        b = remainder # replace b with the stored remainder
    
    return a


def gcf_euclid_pythonic(a, b):
    """
    The Pythonic version of Euclid's algorithm to find GCF.
    """

    a, b = abs(a), abs(b) 
    
    while b != 0:
        a, b = b, a % b 
    return a


# And now let's apply this to 3 or more frequency components:

def gcf_multiple(numbers):
    """Find GCF of a sorted, ascending list of integers."""
    result = numbers[0] # starting with the first number,
    
    for i in range(1, len(numbers)):
        # result is GCF of result and next number in the list
        result = gcf_euclid(result, numbers[i]) 
    
    return result 