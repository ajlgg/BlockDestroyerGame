import pygame as p


class Cannon:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cannonWidth = 100
        self.cannonHeight = 100
        self.cannonXpos = 350
        self.cannonYpos = 650
        self.cannon_img = None
        self.resize_cannon_img = None
        self.load_cannon_image()

        self.ballWidth = 30
        self.ballHeight = 30
        self.ballXpos = 385
        self.ballYpos = 630
        self.ball_img = None
        self.resize_ball_img = None
        self.bullet_in_motion = None
        self.bullet_mask = None
        self.bullet_speed = 5
        self.load_ball_image()
        

    def load_cannon_image(self):
        try:
            self.cannon_img = p.image.load("cannonBOOM.png")
            self.resize_cannon_img = p.transform.scale(
                self.cannon_img, (self.cannonWidth, self.cannonHeight)
            )
        except Exception as e:
            print(f"Error loading cannon image: {e}")

    def make_cannon(self, screen):
        if self.resize_cannon_img:
            screen.blit(self.resize_cannon_img, (self.cannonXpos, self.cannonYpos))

    def draw_cannon(self, screen):
        if self.resize_cannon_img:
            screen.blit(self.resize_cannon_img, (self.cannonXpos, self.cannonYpos))

    def cannon_movement_and_border(self, keys):
        speed = 5
        if keys[p.K_a] and self.cannonXpos > 0:
                self.cannonXpos -= speed
                self.ballXpos -= speed
        if keys[p.K_d] and self.cannonXpos < self.screen_width - self.cannonWidth:
                self.cannonXpos += speed
                self.ballXpos += speed

    def load_ball_image(self):
            try:
                self.ball_img = p.image.load("BALLS.png").convert_alpha()
                self.resize_ball_img = p.transform.scale(
                    self.ball_img, (self.ballWidth, self.ballHeight)
                )
                self.bullet_mask = p.mask.from_surface(self.resize_ball_img)
            except Exception as e:
                print(f"Error loading ball image: {e}")

    def draw_bullets(self, screen):
        if self.resize_ball_img:
            screen.blit(self.resize_ball_img, (self.ballXpos, self.ballYpos))

    def fire_bullet(self):
        if not self.bullet_in_motion:
            self.ballXpos = self.cannonXpos + (self.cannonWidth // 2) - (self.ballWidth // 2)
            self.ballYpos = self.cannonYpos
            self.bullet_in_motion = True

    def reset_bullet(self):
         self.ballXpos = self.cannonXpos + (self.cannonWidth // 2) - (self.ballWidth // 2)
         self.ballYpos = self.cannonYpos
         self.bullet_in_motion = False

    def update_bullet(self):
        if self.bullet_in_motion:
             self.ballYpos -= self.bullet_speed
             if self.ballYpos <= 0:
                  self.reset_bullet()
    
    




    
        
        
        
            



        
