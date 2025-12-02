from collections import deque

def moving_average_queue(samples, window_size):
    """
    Calculate moving average using a queue and running sum.
    Each sample is enqueued once and dequeued once for O(n) time complexity.
    """
    q = deque()          # Queue holds samples currently in the window
    running_sum = 0      # Running sum avoids recalculating
    averages = []
    
    for sample in samples:
        # Enqueue a new sample in the window.
        q.append(sample)
        running_sum += sample
        
        # If the window is too big, dequeue the oldest sample.
        if len(q) > window_size:
            oldest = q.popleft()
            running_sum -= oldest
        
        # Calculate the average from running sum.
        averages.append(running_sum / len(q))
    
    return averages