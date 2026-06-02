import pygame
from tkinter import messagebox, Tk
import sys


window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width,window_height))

column = 25
row = 25

box_w = window_width // column
box_h = window_height // row

grid = []
queu = []

class Box:
    def __init__(self,i,j):
        self.x = i
        self.y = j
        self.start = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neigh = []
    def draw(self,win,color):
        pygame.draw.rect(win,color,(self.x * box_w, self.y * box_h, box_w - 2, box_h - 2))
    
    def set_neighbour(self):
        if self.x > 0:
            self.neigh.append(grid[self.x - 1][self.y])
        if self.x < column - 1 :
            self.neigh.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neigh.append(grid[self.x][self.y - 1])
        if self.y < row - 1:
            self.neigh.append(grid[self.x ][self.y + 1])

for i in range(column):
    arr = []
    for j in range(row):
        arr.append(Box(i,j))
    grid.append(arr)

for i in range(column):
    for j in range(row):
        grid[i][j].set_neighbour()

start_box = grid[0][0]
start_box.start = True
start_box.visited = True
queu.append(start_box)

def main():
    begin_search = False
    target_box_set = False
    searching = True
    target_box = None
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                if event.buttons[2] and not target_box_set:
                    i = x // box_w
                    j = y // box_h
                    target_box = grid[i][j]
                    target_box.target = True
                    target_box_set = True
            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True
            
        if begin_search:
            if len(queu) > 0 and searching:
                current_box = queu.pop(0)
                current_box.visited = True
                if current_box == target_box:
                    searching = False
                for neighbour in current_box.neigh:
                    if not neighbour.visited and not neighbour.queued:
                        neighbour.queued = True
                        queu.append(neighbour)
            else:
                if searching:
                    Tk().wm_withdraw()
                    messagebox.showinfo("Sem solução")
                    searching = False
                

        window.fill((0,0,0))
        for i in range(column):
            for j in range(row):
                box = grid[i][j]
                box.draw(window,(50,50,50))
                if box.queued:
                    box.draw(window,(0,200,0))
                if box.start:
                    box.draw(window,(0,200,200))
                if box.target:
                    box.draw(window,(200,200,0))
        pygame.display.flip()

main()