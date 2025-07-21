import pygame as p

class Lives: 
    def __init__(self, text="Lives", font_name="TimesNewRoman", font_size=30, font_color=(255, 222, 89), position=(20, 20)):
        p.font.init()
        self.text = text
        self.font = p.font.SysFont(font_name, font_size)
        self.color = font_color
        self.position = position

        self.rendered_text = self.font.render(self.text, True, self.color)

    def lives_draw(self, surface):
        surface.blit(self.rendered_text, self.position)

    def lives_text(self, lives_text):
        self.text = lives_text
        self.rendered_text = self.font.render(self.text, True, self.color)

class BlocksDestroyed:
    def __init__(self, text="Lives", font_name="TimesNewRoman", font_size=30, font_color=(255, 222, 89), position=(20, 50)):
        p.font.init()
        self.text = text
        self.font = p.font.SysFont(font_name, font_size)
        self.color = font_color
        self.position = position

        self.rendered_text = self.font.render(self.text, True, self.color)

    def blockD_draw(self, surface):
        surface.blit(self.rendered_text, self.position)

    def BlocksDestroyed_text(self, blockD_text):
        self.text = blockD_text
        self.rendered_text = self.font.render(self.text, True, self.color)

class Score:
    def __init__(self, text="Lives", font_name="TimesNewRoman", font_size=30, font_color=(255, 222, 89), position=(20, 80)):
        p.font.init()
        self.text = text
        self.font = p.font.SysFont(font_name, font_size)
        self.color = font_color
        self.position = position

        self.rendered_text = self.font.render(self.text, True, self.color)

    def score_draw(self, surface):
        surface.blit(self.rendered_text, self.position)
    

    def score_text(self, score_text):
        self.text = score_text
        self.rendered_text = self.font.render(self.text, True, self.color)