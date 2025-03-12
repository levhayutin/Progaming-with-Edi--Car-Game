import pygame
from pygame.locals import *
import random

# Shape perameters
size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
# location parameters
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
# animation parameters
speed = 2



# init app
pygame.init()
running = True

# set window size
screen = pygame.display.set_mode(size)
# Set window title
#pygame.display.set_captation("Don't Hit Me")
# Set backround color
screen.fill((60,220,0))
# Apply Changes
pygame.display.update()


# load player vehicle
car = pygame.image.load("car.png")
#resize image
#car = pygame.transform.scale(car, (250, 250))
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8


# load enemy vehicle
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2


counter = 0
# game loop
while running:
    counter += 1

    # increase game difficulty overtime
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)

    # animate enemy vehicle
    car2_loc[1] += speed
    if car2_loc[1] > height:
        # randomly select lane
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    # end game logic
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

        # event listeners
    for event in pygame.event.get():
        if event.type == quit:
            # collapse the app
            running = False
        if event.type == KEYDOWN:
            # move user car to the left
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            # move user car to the right
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])

                # draw road
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (width/2-road_w/2, 0, road_w, height))
    # draw centre line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height))
    # draw left road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
    # draw right road marking
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))

    # place car images on the screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # apply changes
    pygame.display.update()

# collapse application window
pygame.quit()


#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUxYTXFiRkI2SW5nbmxzdVpiZk1mZVJFalJ0QXxBQ3Jtc0tsbW1lTzBwR0pBTTlTd1NIUmd4bTFFeWNpWDhLaUZHWk1NTngtaXhXWTVzNC1Ma1p3TC1kWnY3VkItZ2phbWdPWk05M0lXTU5HMms4ZzFzZG5pRlpWOHQyUjQyVnJueWd4RTdWeEE4UE1RT25JYlJ6UQ&q=https%3A%2F%2Fwww.freepik.com%2F&v=W-QOtdD3qx4
