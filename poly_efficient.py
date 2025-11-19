# ==================== EFFICIENT POLYPHONY HANDLER ====================

class EfficientPolyphonyHandler:
    """An efficient polyphony handler using a set."""
    
    def __init__(self, list_of_command_lists):
        self.list_of_command_lists = list_of_command_lists
        self.active_notes = set() # a set is a hash table with keys and no values
    
    def process_command(self, command):
        """Process a single command to update active notes."""
        key_number = command[0]
        velocity = command[1]
        
        if velocity > 0:  # Note ON
            self.active_notes.add(key_number)  # O(1)
        else:  # Note OFF
            self.active_notes.discard(key_number)  # O(1) 

    def process_command_list(self, command_list):
        for command in command_list:
            self.process_command(command)
        return self.active_notes.copy() 