# ==================== BRUTE FORCE DURATION CALCULATOR ====================

def calculate_durations_slow(midi_events):
    """
    For each note-off, search backwards through ALL events
    to find the matching note-on.
    Returns: List of (keyNumber, duration_in_seconds) tuples
    Time: O(n²) - nested loops!
    """
    durations = []
    
    for i, event in enumerate(midi_events):
        if event['type'] == 'off':
            # Search backwards for the matching note-on
            for j in range(i - 1, -1, -1):
                prev_event = midi_events[j]
                
                # Found a matching note-on for this pitch?
                if (prev_event['type'] == 'on' and 
                    prev_event['pitch'] == event['pitch']):
                    
                    duration = round(event['time'] - prev_event['time'], 2)
                    durations.append((event['pitch'], duration))
                    break  # Stop searching
    
    return durations

# ==================== TEST CASES ====================

test_cases = [
    {
        "name": "Test 1: Basic Single Note",
        "input": [
            {'type': 'on',  'pitch': 60, 'time': 0.0},
            {'type': 'off', 'pitch': 60, 'time': 1.0}
        ],
        "expected": [(60, 1.0)]
    },
    {
        "name": "Test 2: Two Overlapping Notes",
        "input": [
            {'type': 'on',  'pitch': 60, 'time': 0.0},
            {'type': 'on',  'pitch': 64, 'time': 0.1},
            {'type': 'off', 'pitch': 60, 'time': 0.5},
            {'type': 'off', 'pitch': 64, 'time': 0.8}
        ],
        "expected": [(60, 0.5), (64, 0.7)]
    },
    {
        "name": "Test 3: Three Notes Mixed",
        "input": [
            {'type': 'on',  'pitch': 60, 'time': 0.0},
            {'type': 'on',  'pitch': 64, 'time': 0.1},
            {'type': 'off', 'pitch': 60, 'time': 0.5},
            {'type': 'on',  'pitch': 67, 'time': 0.6},
            {'type': 'off', 'pitch': 64, 'time': 0.8},
            {'type': 'off', 'pitch': 67, 'time': 1.2}
        ],
        "expected": [(60, 0.5), (64, 0.7), (67, 0.6)]
    },
    {
        "name": "Test 4: Same Pitch Repeated",
        "input": [
            {'type': 'on',  'pitch': 60, 'time': 0.0},
            {'type': 'off', 'pitch': 60, 'time': 0.5},
            {'type': 'on',  'pitch': 60, 'time': 0.6},
            {'type': 'off', 'pitch': 60, 'time': 1.0}
        ],
        "expected": [(60, 0.5), (60, 0.4)]
    },
    {
        "name": "Test 5: Complex Polyphony",
        "input": [
            {'type': 'on',  'pitch': 48, 'time': 0.0},   # Bass note
            {'type': 'on',  'pitch': 60, 'time': 0.0},   # C
            {'type': 'on',  'pitch': 64, 'time': 0.0},   # E
            {'type': 'on',  'pitch': 67, 'time': 0.0},   # G
            {'type': 'off', 'pitch': 64, 'time': 0.25},  # E off
            {'type': 'on',  'pitch': 65, 'time': 0.3},   # F
            {'type': 'off', 'pitch': 60, 'time': 0.5},   # C off
            {'type': 'off', 'pitch': 65, 'time': 0.6},   # F off
            {'type': 'off', 'pitch': 67, 'time': 0.75},  # G off
            {'type': 'off', 'pitch': 48, 'time': 1.0}    # Bass off
        ],
        "expected": [(64, 0.25), (60, 0.5), (65, 0.3), (67, 0.75), (48, 1.0)]
    }
]

# ==================== RUN TESTS ====================

print("Running Duration Calculator Tests (Brute Force O(n²))")
print("=" * 60)

for test in test_cases:
    print(f"\n{test['name']}")
    print("-" * 40)
    
    # Run the function and get duration list
    duration_list = calculate_durations_slow(test["input"])
    expected = test["expected"]
    
    # Log the calculated duration sequence
    print("Duration sequence (keyNumber, duration_in_seconds):")
    for key, duration in duration_list:
        print(f"  Note {key}: {duration:.2f} seconds")
    
    # Check if results match
    match = "✓ PASS" if duration_list == expected else "✗ FAIL"
    
    # Display comparison
    print(f"\nExpected: {expected}")
    print(f"Got:      {duration_list}")
    print(f"Result:   {match}")
    
    # Show timing complexity insight
    n = len(test["input"])
    print(f"Complexity: {n} events → up to {n*(n-1)//2} comparisons")

print("\n" + "=" * 60)
print("All tests completed")