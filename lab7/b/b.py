import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button Example")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Определение текста на кнопке
font = pygame.font.Font(None, 36)
text = font.render("Click me!", True, BLACK)

# Создание прямоугольника кнопки
button_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Основной цикл программы
def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка нажатия кнопки мыши в пределах кнопки
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")
                music_file = "kavkaz-Лезгинка-kissvk.com.mp3"
                play_music(music_file)

    # Заливка экрана белым цветом
    screen.fill(WHITE)

    # Отрисовка кнопки
    pygame.draw.rect(screen, GRAY, button_rect)
    screen.blit(text, button_rect.topleft)

    # Обновление экрана
    pygame.display.flip()

