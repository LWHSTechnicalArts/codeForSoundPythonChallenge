# ==================== EFFICIENT DURATION CALCULATOR ====================

def calculate_durations_fast(midi_events):
    """
    Track active notes in a dictionary for O(1) lookups.
    Uses a stack per pitch to handle repeated notes correctly.
    Returns: List of (keyNumber, duration_in_seconds) tuples,
    unsorted by start time.

    Time: O(n) - single pass through input events
    """
    active_notes = {}
    durations = []
    
    for event in midi_events:
        pitch = event['pitch']
        
        if event['type'] == 'on':
            if pitch not in active_notes:
                active_notes[pitch] = []
            active_notes[pitch].append(event['time'])
        
        elif event['type'] == 'off':
            if pitch in active_notes and active_notes[pitch]:
                note_on_time = active_notes[pitch].pop()
                duration = event['time'] - note_on_time
                durations.append((pitch, duration))
    
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
    },
]

# ==================== RUN TESTS ====================

print("Running Duration Calculator Tests (Efficient O(n))")
print("=" * 60)

for test in test_cases:
    print(f"\n{test['name']}")
    print("-" * 40)
    
    # Run the function and get duration list
    duration_list = calculate_durations_fast(test["input"])
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
    print(f"Complexity: {n} events → exactly {n} operations (O(n))")

print("\n" + "=" * 60)
print("All tests completed")
