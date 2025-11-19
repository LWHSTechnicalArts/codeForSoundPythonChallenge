# ==================== EFFICIENT POLYPHONY HANDLER ====================

class EfficientPolyphonyHandler:
    """An efficient polyphony handler using a set."""
    
    def __init__(self, list_of_command_lists):
        self.list_of_command_lists = list_of_command_lists
        self.active_notes = set()
        self.current_list_index = 0
    
    def process_command(self, command):
        """Process a single command to update active notes."""
        key_number = command[0]
        velocity = command[1]
        
        if velocity > 0:  # Note ON
            self.active_notes.add(key_number)  # O(1)
        else:  # Note OFF
            self.active_notes.discard(key_number)  # O(1)
    
    def process_all_lists(self):
        """Process all command lists."""
        for command_list in self.list_of_command_lists:
            for command in command_list:
                self.process_command(command)
        return sorted(self.active_notes)