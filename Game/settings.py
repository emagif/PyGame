class Settings: # a class that enables to create permanent settings instead of setting values in the main file
    
    def __init__(self): 

        self.screen_width = 1200 # declaration of screen width and height
        self.screen_height = 800
        self.background_color = (230, 230, 230) # declaration of background color
        self.ship_speed = 1.5 # setting the ships speed
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1.0
        self.fleet_direction = 1
