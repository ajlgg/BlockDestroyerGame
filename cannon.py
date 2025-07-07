import pygame as p
import blockGeneration 

class Cannon:
    def __init__(self, screen_width):
        self.cannon_img = None
        self.cannonXpos = 400
        self.cannonYpos = 650
        self.resize_cannon_img = None 
        self.cannonWidth = 100
        self.cannonHeight = 100
        self.screen_width = screen_width
        self.ball_img = None
        self.resize_ball_img = None
        self.ballWidth = 30
        self.ballHeight = 30
        self.ballXpos = 400
        self.ballYpos = 500


    def make_cannon(self, screen):
        try:
            self.cannon_img = p.image.load("cannonBOOM.png")
            self.resize_cannon_img = p.transform.scale(self.cannon_img, (self.cannonWidth, self.cannonHeight))
        except Exception as e:
            print(f"Error loading image: {e}")
            return

        screen.blit(self.resize_cannon_img, (self.cannonXpos, self.cannonYpos))

    def draw_cannon(self, screen):
        screen.blit(self.resize_cannon_img, (self.cannonXpos, self.cannonYpos))

    def cannon_movement_and_border(self, keys):
        x = 5
        if keys[p.K_a]:
            if self.cannonXpos > 0:
                self.cannonXpos -= x
        if keys[p.K_d]:
            if self.cannonXpos < self.screen_width - self.cannonWidth:
                self.cannonXpos += x

    def cannon_bullets(self, screen):
        try:
            self.ball_img = p.image.load("BALLS.png")
            self.resize_ball_img = p.transform.scale(self.ball_img, (self.ballWidth, self.ballHeight))
        except Exception as e:
            print(f"Error loading image: {e}")
            return
        screen.blit(self.resize_ball_img, (self.ballXpos, self.ballYpos))

    def draw_bullets(self, screen):
        screen.blit(self.resize_ball_img, (self.ballXpos, self.ballYpos))

    def cannon_ball_fire(self):
        pass
        # for the cannon ball fire we want to make sure that the cannon ball image starts at a certain location
        # this location would be behind the cannon or inside the cannon on the screen
        # then we want to have the ball move upward when we press the space bar key 
        