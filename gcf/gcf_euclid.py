def gcf_euclid(a, b):
    """Find GCF using Euclid's algorithm."""
    a, b = abs(a), abs(b)
    
    while b != 0:
        a, b = b, a % b
    return a