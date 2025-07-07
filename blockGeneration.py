import pygame as p
import random

class BlockGenerator:
    def __init__(self, numBlocks, randColors, screen_width):
        self.numBlocks = numBlocks
        self.randColors = randColors
        self.blocksize = 50
        self.screen_width = screen_width

    def randomBlockColor(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    def randomNumberBlocks(self):
        self.numBlocks = random.randint(1, 5)

    def generateBlock(self, screen):
        self.randomNumberBlocks()
        placed_blocks = []

        screen_height = screen.get_height() 

        for _ in range(self.numBlocks):
            color = self.randomBlockColor()

            placed = False
            while not placed:
                
                x = random.randint(0, self.screen_width - self.blocksize)
               
                y = random.randint(0, (screen_height // 2) - self.blocksize)
                new_rect = p.Rect(x, y, self.blocksize, self.blocksize)

                # there is no collision detection taking place so just set that to false

                collision = False
                # now we want to set a variable block and loop that into the list placed_blocks
                for block in placed_blocks:
                    # we want to use new_rect now to check if any of the rects in placed_blocks are touching or colliding
                    if new_rect.colliderect(block):
                        # if this is true then break the program
                        collision = True
                        break
                # otherwise check if there is no collision then append the new_rect to the list and then draw it on the screen
                if not collision:
                    placed_blocks.append(new_rect)
                    p.draw.rect(screen, color, new_rect)
                    placed = True
        

                

        

