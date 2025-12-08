def gcf_brute_force(a, b):
    """Find GCF by checking all possible divisors."""
    a, b = abs(a), abs(b)  # handle negative inputs
    smaller = min(a, b)
    
    gcf = 1
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            gcf = i
    return gcf