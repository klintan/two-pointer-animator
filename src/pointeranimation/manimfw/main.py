from manim import *
import copy

import numpy as np


class Array(Scene):
    def construct(self):
        # 8 x 14 grid is the screen, 0 in the origin or center.
        arr = [5, 8, 13, 0, 1, 0, 3, 12]
        align = len(arr) // 2
        array_ = self.render_array(arr)
        self.render_pointer(3, array_)

    def render_pointer(self, p, arr):
        arr[p].set_fill(BLUE, opacity=1.0)
        self.play(Create(arr[p]))

    def render_array(self, arr):
        squares = []
        for idx, n in enumerate(arr):
            square = Rectangle(height=1, width=1, stroke_width=2)
            square.stroke_color = WHITE
            square.to_edge(RIGHT).shift(idx * LEFT)
            text = Text(str(n), font_size=52)
            text.to_edge(RIGHT).shift(np.array([(idx * -1) - 0.25, 0, 0]))
            self.add(square, text)
            squares.append(square)
        return squares