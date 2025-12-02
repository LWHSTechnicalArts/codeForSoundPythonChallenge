def moving_average_brute(samples, window_size):
    """
    Calculate moving average using brute force.
    For each position, sum all samples in the window and divide.
    """
    averages = []
    
    for i in range(len(samples)):
        # Window starts at max(0, i - window_size + 1) and ends at i
        window_start = max(0, i - window_size + 1)
        
        # Sum all samples in the window
        window_sum = 0
        for j in range(window_start, i + 1):
            window_sum += samples[j]
        
        # Calculate average
        window_length = i - window_start + 1
        averages.append(window_sum / window_length)
    
    return averages