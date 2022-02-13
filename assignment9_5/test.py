from box import Box
from dots_and_boxes_game import DotsAndBoxesGame

g = DotsAndBoxesGame(4, 4, "Liisa", "Katarina");
g.add_line(1,1, Box.UP, "Liisa")
g.add_line(1,1, Box.RIGHT, "Katarina")
print(g.one_row_of_grid(1))