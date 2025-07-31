# physics_engine/player_movement.py
# This module handles player movement in a physics engine context.
class PlayerMovement:
    
#constants for gravity
    GRAVITY : float = -9.81  # m/s^2
    JUMP_VELOCITY : float = 5.0  # m/s
    GROUND : float = 0.0

    #constructor for player_movement class
    def __init__(self, position = None, speed = 5.0, direction = None):
        self.position : list = position if position else [1, 1] # Initial position of the player
        self.speed : float = speed if speed else 5.0 # Speed of the player
        self.direction : list = direction if direction else [1, 1] # Direction of movement
        self.grounded : bool = True  # Player starts grounded
        self.vertical_position : float = self.position[1]

    # Setters and getters for position, direction, and speed
    def set_position(self, x, y):
        self.position[0] = x
        self.position[1] = y

    def get_position(self):
        return self.position
    
    def set_direction(self, x, y):
        self.direction[0] = x
        self.direction[1] = y

    def get_direction(self):
        return self.direction

    def set_speed(self, speed):
        self.speed = speed

#moves the player based on direction and speed
    def move_player(self, delta_time):
        self.position[0] += self.direction[0] * self.speed * delta_time
        self.position[1] += self.direction[1] * self.speed * delta_time

#updates the vertical position of the player based on gravity
    def jump(self, delta_time):
        if self.grounded:
            self.vertical_position += self.JUMP_VELOCITY * delta_time + 0.5 * self.GRAVITY * delta_time**2
            if self.vertical_position <= self.GROUND:
                self.vertical_position = self.GROUND
                self.grounded = True
            else:
                self.grounded = False