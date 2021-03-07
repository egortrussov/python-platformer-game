
class Inventory:
    def __init__(self, window):
        self.window = window 

        self.primary = None 
        self.primary_num = 0
        self.secondary = None 
        self.secondary_num = 0
    
    def draw(self):
        self.window.draw_rect(10, 80, 70, 70, [255, 0, 0]) 
        self.window.draw_rect(15, 85, 63, 63, [0, 0, 0]) 
    

        