
import pygame
import heapq

pygame.init()

# config
ROWS, COLS = 30, 40
CELL_SIZE = 20
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
GREEN = (0, 200, 0)     
RED = (200, 0, 0)      
BLUE = (0, 100, 255)    
YELLOW = (255, 215, 0) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinding Visualizer")
clock = pygame.time.Clock()

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
start = None
end = None


def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            value = grid[row][col]
            color = WHITE
            if value == 1:
                color = BLACK
            elif value == 2:
                color = GREEN
            elif value == 3:
                color = RED
            pygame.draw.rect(
                screen, color,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
            pygame.draw.rect(
                screen, GREY,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
            )


def get_neighbors(node):
    row, col = node
    neighbors = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
        r, c = row + dr, col + dc
        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] != 1:
            neighbors.append((r, c))
    return neighbors


def draw_cell(pos, color):
    row, col = pos
    pygame.draw.rect(
        screen, color,
        (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    )
    pygame.draw.rect(
        screen, GREY,
        (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
    )
    pygame.display.update()


def reconstruct_path(came_from, current):
    while current in came_from:
        current = came_from[current]
        if current != start:
            draw_cell(current, YELLOW)
            pygame.time.delay(15)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


def dijkstra():

    queue = [(0, start)]  # (distance, node)
    distances = {start: 0}
    came_from = {}
    visited = set()

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        current_dist, current = heapq.heappop(queue)

        if current in visited:
            continue
        visited.add(current)

        if current == end:
            reconstruct_path(came_from, end)
            return True

        if current != start:
            draw_cell(current, BLUE)
            pygame.time.delay(5)

        for neighbor in get_neighbors(current):
            new_dist = current_dist + 1
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                came_from[neighbor] = current
                heapq.heappush(queue, (new_dist, neighbor))

    return False  # no path found


def main():
    global start, end

    running = True
    while running:
        draw_grid()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif pygame.mouse.get_pressed()[0]:  # left click
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE
                pos = (row, col)

                if not start and pos != end:
                    start = pos
                    grid[row][col] = 2
                elif not end and pos != start:
                    end = pos
                    grid[row][col] = 3
                elif pos != start and pos != end:
                    grid[row][col] = 1

            elif pygame.mouse.get_pressed()[2]:  # right click
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE
                pos = (row, col)
                if pos == start:
                    start = None
                elif pos == end:
                    end = None
                grid[row][col] = 0

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    dijkstra()
                elif event.key == pygame.K_c:
                    grid[:] = [[0 for _ in range(COLS)] for _ in range(ROWS)]
                    start = None
                    end = None

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
