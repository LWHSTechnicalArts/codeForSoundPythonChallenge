# ==================== BRUTE FORCE POLYPHONY HANDLER ====================

class BruteForcePolyphonyHandler:
    """A brute-force polyphony handler that tracks active keys."""
    
    def __init__(self, list_of_command_lists):
        self.list_of_command_lists = list_of_command_lists
        self.active_notes = []
    
    def process_command(self, command):
        """Process a single command to update active notes."""
        key_number = command[0]
        velocity = command[1]
        
        if velocity > 0:  # Note ON
            if key_number not in self.active_notes:  # O(n) search
                self.active_notes.append(key_number)
        else:  # Note OFF (velocity == 0)
            if key_number in self.active_notes:  # O(n) search
                self.active_notes.remove(key_number)  # O(n) removal
    
    def process_command_list(self, command_list):
        for command in command_list:
            self.process_command(command)
        return self.active_notes.copy()

# ==================== TEST CASES ====================

test_cases = [
    {
        "name": "Test 1: Simple Chord",
        "input": [
            [[60, 100], [64, 100], [67, 100]],
            [[60, 0], [64, 0], [67, 0]]
        ],
        "expected": [
            [60, 64, 67],
            []
        ]
    },
    {
        "name": "Test 2: Overlapping Notes",
        "input": [
            [[60, 100]],
            [[62, 100]],
            [[60, 0]],
            [[62, 0]]
        ],
        "expected": [
            [60],
            [60, 62],
            [62],
            []
        ]
    },
    {
        "name": "Test 3: Dense Polyphony",
        "input": [
            [[60, 100], [62, 100], [64, 100], [65, 100], [67, 100]],
            [[60, 0], [62, 0]],
            [[64, 0], [65, 0], [67, 0]]
        ],
        "expected": [
            [60, 62, 64, 65, 67],
            [64, 65, 67],
            []
        ]
    }
]


# ==================== RUN TESTS ====================

for test in test_cases:
    print(test["name"])
    handler = BruteForcePolyphonyHandler(test["input"])
    
    for i, command_list in enumerate(test["input"]):
            result = handler.process_command_list(command_list)
            expected = test["expected"][i]
            match = "✓" if result == expected else "✗"
            print(f"  After list {i+1}: {result} {match}")
    print()