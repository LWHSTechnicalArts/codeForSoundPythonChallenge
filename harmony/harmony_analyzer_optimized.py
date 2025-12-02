def active_pitch_classes_optimized(key_numbers, window_size):
    result = []
    window = deque()  # stores notes in window order
    pitch_class_count = {}     # hash table (pitch_class: count in window)
    
    for key_number in key_numbers:
        pitch_class = key_number % 12
        
        # enqueue new key_number in window and increment its pitch class count
        window.append(key_number)
        pitch_class_count[pitch_class] = pitch_class_count.get(pitch_class, 0) + 1
        
        # Dequeue oldest key_number if window exceeds size window_size and decrement pitch class count
        if len(window) > window_size:
            old_key_number = window.popleft()
            old_pitch_class = old_key_number % 12
            pitch_class_count[old_pitch_class] -= 1
            if pitch_class_count[old_pitch_class] == 0: # Remove from active set if count == 0
                del pitch_class_count[old_pitch_class]  
        
        # The keys in the window dictionary are the active pitch classes.
        result.append(set(pitch_class_count.keys()))
    
    return result