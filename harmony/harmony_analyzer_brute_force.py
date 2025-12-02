def active_pitch_classes_brute(key_numbers, window_size):
    '''
    Brute-force method to find active pitch classes in the last window_size key numbers.
    '''
    result = []
    for i in range(len(key_numbers)):
        # Get the lookback window ending at position i.
        start = max(0, i - window_size + 1)
        window = key_numbers[start:i+1]
        
        # Find the unique pitch classes in the window notes.
        pitch_classes = set()
        for key_number in window:
            pitch_class = key_number % 12
            pitch_classes.add(pitch_class)
        
        result.append(pitch_classes.copy())
    
    return result