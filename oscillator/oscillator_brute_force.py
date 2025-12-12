import math

def direct_sin_lfo(num_samples, frequency=1.0, sample_rate=44100):
    """Generate LFO by calculating sin() each time"""
    output = []
    phase = 0.0
    phase_increment = frequency / sample_rate
    
    for _ in range(num_samples):
        # Calculate sin directly
        output_value = math.sin(2 * math.pi * phase)
        output.append(output_value)
        
        # Advance phase
        phase += phase_increment
        if phase >= 1.0:
            phase -= 1.0
    
    return output