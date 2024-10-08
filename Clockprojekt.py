import pygame
import math
import time

pygame.init()

screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Analog Clock")

# de farver jeg skal bruge
def colors():
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    return white, black, red

# bruger function til at tegne clock face
def clock_face(screen, center, radius, color):
    pygame.draw.circle(screen, color, center, radius, 5)

# tegner ticks til uret
def the_clock_ticks(screen, center, radius, color):
    for i in range(60):  # 60  ticks for min/sec                       
        angle = math.radians(i * 6)  # hver tick er 6 grader fra hinden
        tick_length = 20 if i % 5 == 0 else 10  # længere ticks for hour marks
        start_x = center[0] + (radius - tick_length) * math.cos(angle)
        start_y = center[1] + (radius - tick_length) * math.sin(angle)
        end_x = center[0] + radius * math.cos(angle)
        end_y = center[1] + radius * math.sin(angle)
        pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), 2)





# vinkler bassseret på den aktulle tid
def the_clock_hands(screen, center, radius, hour_color, minute_color, second_color, hour, minute, second):
    # Calculate angles based on current time
    hour_angle = -90 + (hour % 12) * 30 + (minute / 60) * 30   # hver time repræsentere 30 grader
    minute_angle = -90 + (minute * 6)                       # hver minut 6 grader(360 grader delt med 60 giver 6 grader pr. minut)
    second_angle = -90 + (second * 6)                        # hver sekund repsæntere også 6 grader.

    # længden:
    hour_length = radius * 0.5  # Hour hand is 50%
    minute_length = radius * 0.75  # Minute hand is 75%
    second_length = radius * 0.9  # Second hand is 90%

    # tgner hour hand
    hour_x = center[0] + hour_length * math.cos(math.radians(hour_angle))
    hour_y = center[1] + hour_length * math.sin(math.radians(hour_angle))
    pygame.draw.line(screen, hour_color, center, (hour_x, hour_y), 8)

    #  minute hand
    minute_x = center[0] + minute_length * math.cos(math.radians(minute_angle))
    minute_y = center[1] + minute_length * math.sin(math.radians(minute_angle))
    pygame.draw.line(screen, minute_color, center, (minute_x, minute_y), 6)

    #  second hand
    second_x = center[0] + second_length * math.cos(math.radians(second_angle))
    second_y = center[1] + second_length * math.sin(math.radians(second_angle))
    pygame.draw.line(screen, second_color, center, (second_x, second_y), 2)

# Main loop
def main():
    white, red, black = colors()  
    center = (screen_size[0] // 2, screen_size[1] // 2)  
    radius = 250 

    running = True
    while running:
        #  current time
        current_time = time.localtime()  
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        screen.fill(red)  
        
        # tegner clock face og ticks
        clock_face(screen, center, radius, black)
        the_clock_ticks(screen, center, radius, black)

        #  tegner clock hands
        the_clock_hands(screen, center, radius, black, black, black, hour, minute, second)

        pygame.display.flip()  
        
        # delay (10000) 
        pygame.time.delay(1000)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

#run the main loop
if __name__ == "__main__":
    main()

