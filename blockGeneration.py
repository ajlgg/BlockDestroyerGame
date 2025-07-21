import pygame as p
import random


class BlockGenerator:
    def __init__(self, numBlocks, randColors, screen_width):
        self.numBlocks = numBlocks
        self.randColors = randColors
        self.blocksize = 50
        self.screen_width = screen_width
        self.blocks = []  # Store block data here

    def randomBlockColor(self):
        return (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )

    def randomNumberBlocks(self):
        self.numBlocks = random.randint(10, 30)

    def generateBlock(self, screen):
        self.randomNumberBlocks()
        self.blocks = []  # Clear previous blocks

        screen_height = screen.get_height() 

        for _ in range(self.numBlocks):
            color = self.randomBlockColor()

            placed = False
            while not placed:
                x = random.randint(0, self.screen_width - self.blocksize)
                y = random.randint(0, (screen_height // 2) - self.blocksize)
                new_rect = p.Rect(x, y, self.blocksize, self.blocksize)

                collision = False
                for block in self.blocks:
                    if new_rect.colliderect(block['rect']):
                        collision = True
                        break

                if not collision:
                    # Create a surface for the block
                    block_surface = p.Surface((self.blocksize, self.blocksize), p.SRCALPHA)
                    block_surface.fill(color)

                    # Create the mask
                    block_mask = p.mask.from_surface(block_surface)

                    # Store block data
                    self.blocks.append({
                        'rect': new_rect,
                        'surface': block_surface,
                        'mask': block_mask,
                        'color': color
                    })

                    screen.blit(block_surface, (new_rect.x, new_rect.y))
                    placed = True

    def draw_Blocks(self, screen):
        for block in self.blocks:
            screen.blit(block['surface'], (block['rect'].x, block['rect'].y))


        

                

        

