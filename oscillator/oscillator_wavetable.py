import math

def wavetable_oscillator(num_samples, frequency=1.0, sample_rate=44100, table_size=1024):
    """Look up sample values in a pre-computed wavetable and apply linear interpolation"""
    # Create one cycle - frequency argument determines playback speed through table, not table contents
    table = [math.sin(2 * math.pi * i / table_size) for i in range(table_size)]
    
    output = []
    phase = 0.0
    phase_increment = frequency / sample_rate
    
    for _ in range(num_samples):
        # Find exact position in table
        exact_table_position = phase * table_size # might be fractional
        index_before = int(exact_table_position) # rewinds to integer index
        index_after = (index_before + 1) % table_size # fast-forward to next index, wrap around
        blend_amount = exact_table_position - index_before # fractional part for interpolation
        
        # Interpolate between two nearest samples
        sample_before = table[index_before]
        sample_after = table[index_after]
        output_value = sample_before + blend_amount * (sample_after - sample_before) # linear interpolation
        
        output.append(output_value)
        
        # Advance phase
        phase += phase_increment
        if phase >= 1.0:
            phase -= 1.0
    
    return output