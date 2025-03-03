from UI.simple_ui import simple_main
from UI.complex_ui import complex_main

class UserInterfaceHandler:
    def __init__(self, ui_type='simple'):
        # Initialize with a default UI type
        self.ui_type = ui_type

    def get_ui(self):
        """
        Returns the appropriate UI instance based on the ui_type.
        """
        if self.ui_type == 'simple':
            return simple_main
        elif self.ui_type == 'complex':
            return complex_main
        else:
            raise ValueError(f"Unsupported UI type: {self.ui_type}")

    def set_ui_type(self, ui_type):
        """
        Set the UI type dynamically. 
        """
        self.ui_type = ui_type
