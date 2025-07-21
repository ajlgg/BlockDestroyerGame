import pygame as p
from blockGeneration import BlockGenerator
from cannon import Cannon
from scoreboard import Lives, BlocksDestroyed, Score
class GameState:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_surface = p.Surface((screen_width, screen_height))
        self.background_surface.fill((0, 0, 0))

        self.blocks = BlockGenerator(1, (0, 0, 0), screen_width)
        self.blocks.generateBlock(self.background_surface)

        self.cannon = Cannon(screen_width, screen_height)
        self.lives = Lives()
        self.blockD = BlocksDestroyed()
        self.score = Score()
        
        

        # track bullets in motion (for example)
        self.bullets = []

        # first_text = ScoreBoard(font_name='TimesNewRoman', font_size=50, font_color=(random.randint(255, 255)))

    def update(self, keys):
        # Cannon movement
        self.cannon.cannon_movement_and_border(keys)

        if keys[p.K_SPACE]:
            self.cannon.fire_bullet()

        self.cannon.update_bullet()
        self.lives.lives_text(f"Lives: ")
        self.blockD.BlocksDestroyed_text(f"Blocks Destroyed: ")
        self.score.score_text(f"Score: ")
        
        
        
        


        # Update bullet positions here if animated (placeholder logic)
        # Example: for bullet in self.bullets: bullet.move()

    def draw(self, screen):
        # draw background
        screen.blit(self.background_surface, (0, 0))

       
        self.cannon.draw_bullets(screen)
        self.cannon.draw_cannon(screen)
        self.blocks.draw_Blocks(screen)
        self.lives.lives_draw(screen)
        self.blockD.blockD_draw(screen)
        self.score.score_draw(screen)
       