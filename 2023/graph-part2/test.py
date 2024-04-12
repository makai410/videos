from manim import *

class Queue(Scene):
    def construct(self):
        queue = []
        for i in range(5):
            rect = Square(side_length=0.5)
            if queue:
                rect.next_to(queue[-1], RIGHT, buff=0.1)
            else:
                rect.to_edge(LEFT)
            self.play(Create(rect))
            queue.append(rect)
            self.wait(0.5)

        while queue:
            self.play(queue[0].animate.shift(LEFT * 3), rate_func=linear)
            self.remove(queue.pop(0))
            self.wait(0.5)
class Tst(Scene):
    def construct(self):
        '''Code block'''
        dfs_pseudo = Code(
            file_name='assets/codes/dfs_pseudo.cpp',
            font='Cascadia Code',
            tab_width=2,
            insert_line_no=True,
            style='github-dark',
            background='rectangle',
            line_spacing=0.5,
            font_size=26
        ).move_to(LEFT * 3)
        dfs_pseudo.background_mobject.become(VMobject())
        dfs_pseudo.line_numbers.set_color(GREY_B)
        self.play(
            FadeIn(dfs_pseudo)
        )
        self.wait()
        box = RoundedRectangle(
            corner_radius=0.08,
            color=WHITE,
            height=0.42,
            width=5.6
        ).set_stroke(width=2.5).align_to(dfs_pseudo, UL).shift((-0.1, 0.05, 0.0))
        line = [box.get_center() + (0, 0.4 * i, 0) for i in range(5)]
        self.play(
            Create(box)
        )
        self.wait()
        label = Text(
            text="深度优先搜索之递归实现",
            t2c={
                '[7:9]': '#b392f0'
            },
            color=ManimColor('#e1e4e8'),
            font='Smiley Sans',
            font_size=24,
            fill_opacity=0.6
        ).align_to(dfs_pseudo, UL).shift((0, 1, 0))
        self.play(
            Create(label)
        )
        self.wait()