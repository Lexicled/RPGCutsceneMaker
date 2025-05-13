from PySide6.QtWidgets import *

class DragDrop:
    def __init__(self):
        self.held = None # Item being dragged
        self.cursor_state = None #TODO figure out how to change cursor images