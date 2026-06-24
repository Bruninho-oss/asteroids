import pygame

pygame.init()
print("[LOG]: setup start")

window = pygame.display.set_mode(size=(600, 480))
print("[LOG]: setup end")

print("[LOG]: initio do loop")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

