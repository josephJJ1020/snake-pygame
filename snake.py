import pygame
import random


pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

w = 1000
h = 600
dis = pygame.display.set_mode((w, h))

pygame.display.set_caption('Snake Game2')

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 10

font_style = pygame.font.SysFont("harlowsolid", 25)
score_font = pygame.font.SysFont("harlowsolid", 35)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [w / x, h / y])


run = True


def gameloop():
    game_over = False
    game_close = False
    snake_speed = 10

    x1 = w / 2
    y1 = h / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, w - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, h - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close:
            dis.fill(black)
            message("You Lost!", yellow, 2.4, 3)
            message("Press Return to Restart the game.", yellow, 3.2, 2)
            message("Press Escape to Quit the game", yellow, 3, 1.5)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= w or x1 < 0 or y1 >= h or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(black)

        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, w - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, h - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            snake_speed += 2
        clock.tick(snake_speed)

    pygame.quit()
    quit()


def game_start():
    dis.fill(black)
    message("Welcome to Snake!", yellow, 2.5, 3)
    message("Press Return to Play the Game!", yellow, 3, 2.5)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()


game_start()
