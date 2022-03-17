import random
import copy
# Import and initialize the pygame library
import pygame


def main(arr):
    original_arr = copy.deepcopy(arr)
    pygame.init()

    font = pygame.font.SysFont('Arial', 14)
    pygame.display.set_caption('Animation')

    rectangle_offset = 10

    clock = pygame.time.Clock()

    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])

    def reset_rects(arr):
        arr_rects = []
        texts = []
        for idx, num in enumerate(arr):
            temp_rect = pygame.Rect(((50 * idx) + rectangle_offset, 50), (50, 50))
            temp_rect_instance = pygame.draw.rect(screen, (0, 255, 0), temp_rect)
            arr_rects.append(temp_rect_instance)

            texts.append(add_text(num, temp_rect_instance))
        return arr_rects

    def restart(arr):
        # Fill the background with white
        screen.fill((255, 255, 255))
        arr_rects = []
        texts = []
        for idx, num in enumerate(arr):
            temp_rect = pygame.Rect(((50 * idx) + rectangle_offset, 50), (50, 50))
            temp_rect_instance = pygame.draw.rect(screen, (0, 255, 0), temp_rect)
            arr_rects.append(temp_rect_instance)

            texts.append(add_text(num, temp_rect_instance))
        return arr_rects

    def add_text(text, rect, pointer=False, font_surface=None):
        if not pointer:
            pos = (rect.x, rect.y)
        else:
            pos = (rect.x, rect.y + 30)

        font_surface = font.render(f"{text}", True, (0, 0, 0))
        screen.blit(font_surface, pos)
        pygame.display.update()
        return font_surface

    def animate(arr, p1, p2, file_num):
        update_rects(arr, p1, p2)
        filename = f"snaps/{file_num}.png"
        pygame.image.save(screen, filename)
        clock.tick(0.5)

    def move_zeroes_algorithm(arr, file_num):
        slow = 0
        for fast in range(len(arr)):
            if arr[fast] != 0:
                file_num += 1
                animate(arr, ("fast", fast), ("slow", slow), file_num)

                arr[slow], arr[fast] = arr[fast], arr[slow]
                slow += 1
        file_num += 1
        animate(arr, ("fast", fast), ("slow", slow), file_num)

    def two_sum_sorted_algorithm(arr, file_num):
        target = 9
        l, r = 0, len(arr) - 1

        while l <= r:
            file_num += 1
            animate(arr, ("r", r), ("l", l), file_num)

            if arr[l] + arr[r] == target:
                return [l + 1, r + 1]

            if arr[l] + arr[r] > target:
                r -= 1
            else:
                l += 1

            print(r, l)

        file_num += 1
        animate(arr, ("r", r), ("l", l), file_num)


        return False

    def update_rects(arr, *pointers):
        # Fill the background with white
        screen.fill((255, 255, 255))

        reset_rects(arr)

        # update current pointers
        same = all([pointers[i][1] == pointers[i - 1][1] for i in range(1, len(pointers))])
        if same:
            rect1_text = pointers[0][0]
            rect2_text = pointers[1][0]

            # indices will be the same so we need to create a new rectangle
            rect1_index = pointers[0][1]

            arr_rects[rect1_index].width = arr_rects[rect1_index].width // 2

            # create new rect
            rect2 = pygame.Rect(
                (arr_rects[rect1_index].x + arr_rects[rect1_index].width, arr_rects[rect1_index].y),
                (arr_rects[rect1_index].width, 50))

            pygame.draw.rect(screen, (255, 0, 0), arr_rects[rect1_index])
            add_text(rect1_text, arr_rects[rect1_index], pointer=True)

            pygame.draw.rect(screen, (0, 0, 255), rect2)
            add_text(rect2_text, rect2, pointer=True)
            pygame.display.update()

        else:

            for idx, p in enumerate(pointers):
                if idx % 2 == 0:
                    color = (255, 0, 0)
                else:
                    color = (0, 0, 255)

                pygame.draw.rect(screen, color, arr_rects[p[1]])
                add_text(p[0], arr_rects[p[1]], pointer=True)
                pygame.display.update()

        # update numbers
        for rect, num in zip(arr_rects, arr):
            add_text(num, rect)

    arr_rects = restart(arr)

    pygame.display.update()

    # Run until the user asks to quit
    running = True
    file_num = 0
    while running:
        arr = copy.copy(original_arr)
        arr_rects = restart(arr)
        # reset_rects(arr)
        clock.tick(0.5)
        filename = f"snaps/{file_num}.png"
        pygame.image.save(screen, filename)

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #move_zeroes_algorithm(arr, file_num)
        two_sum_sorted_algorithm(arr, file_num)
        # Flip the display
        pygame.display.update()
        break
    # Done! Time to quit.
    pygame.quit()


if __name__ == '__main__':
    nums = [2,7,11,15]
    #nums = [5, 8, 13, 0, 1, 0, 3, 12]
    main(nums)
