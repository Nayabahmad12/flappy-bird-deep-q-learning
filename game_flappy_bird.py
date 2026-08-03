import flappy_bird_gymnasium
import gymnasium
import pygame

env = gymnasium.make("FlappyBird-v0", render_mode="human")

obs, _ = env.reset()

running = True

while running:
    action = 0  # do nothing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                action = 1  # flap

    obs, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        obs, _ = env.reset()

env.close()
pygame.quit()