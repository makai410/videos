from manim import *
from queue import Queue
BACKGROUND_COLOR = ManimColor('#1f2428')
TEXT_COLOR = ManimColor('#e1e4e8')
DEF_PURPLE = ManimColor('#b392f0')
DEF_ORANGE = ManimColor('#f8a56e')
DEF_FONT = 'Source Han Serif SC'
CODE_FONT = 'Cascadia Code'

class Intro(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        taffy = Text(
            text="塔菲带你入门图论(2)",
            t2c={
                '[6:8]': '#b392f0'
            },
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY
        )
        self.play(
            Create(taffy)
        )
        self.wait()

class DFSGraphing(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        vertices = [i for i in range(6)]
        edges = [
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 5),
            (2, 5),
            (3, 5),
            (4, 5)
        ]
        '''Graph'''
        g = Graph(
            vertices,
            edges,
            layout={
                0:[0, 3, 0],
                1:[-2, 0, 0],
                2:[-1, 0, 0],
                3:[1, 0, 0],
                4:[2, 0, 0],
                5:[0, -3, 0]
            }
        )

        self.play(Create(g))
        self.wait()
        g.generate_target()
        g.target.shift(RIGHT * 3).scale(0.8)
        self.play(
            MoveToTarget(g)
        )
        self.wait()
        '''Graph Labeled'''
        g1 = Graph(
            vertices,
            edges,
            layout={
                0:[0, 3, 0],
                1:[-2, 0, 0],
                2:[-1, 0, 0],
                3:[1, 0, 0],
                4:[2, 0, 0],
                5:[0, -3, 0]
            },
            labels=True
        ).shift(RIGHT * 3).scale(0.8)
        self.play(
            ReplacementTransform(g, g1)
        )
        self.wait()
        '''Code block'''
        dfs_pseudo = Code(
            file_name='assets/codes/dfs_pseudo.cpp',
            font=CODE_FONT,
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
            Create(dfs_pseudo)
        )
        label = Text(
            text="深度优先搜索之递归实现",
            t2c={
                '[7:9]':'#b392f0'
            },
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=BOLD,
            font_size=24,
            fill_opacity=0.6
        ).align_to(dfs_pseudo, UL).shift((0, 2, 0))
        self.play(
            Create(label)
        )
        self.wait()
        '''Execution Box'''
        box = RoundedRectangle(
            corner_radius=0.08,
            color=WHITE,
            height=0.42,
            width=5.6
        ).set_stroke(width=2.5).align_to(dfs_pseudo, UL).shift((-0.1, 0.05, 0.0))
        line = [box.get_center() + (0, -0.4 * i, 0) for i in range(6)]
        self.play(
            Create(box)
        )
        self.wait()
        '''DFS Process'''
        mtx = [[1, 2, 3, 4], [0, 5], [0, 5], [0, 5], [0, 5], [1, 2, 3, 4]]
        root = 0
        visited = [False for i in range(6)]
        def dfs(v):
            self.play(
                ApplyMethod(
                    box.move_to,
                    line[0]
                ),
                ApplyMethod(
                    g1[v][0].set_color, GREEN_E
                ),
                ApplyMethod(
                    g1[v][1].set_color, WHITE
                )
            )
            self.wait()
            visited[v] = True
            self.play(
                ApplyMethod(
                    box.move_to,
                    line[1]
                ),
                ApplyMethod(
                    g1[v][0].set_color, DEF_PURPLE
                ),
                ApplyMethod(
                    g1[v][1].set_color, BLACK
                )
            )
            self.wait()
            for u in mtx[v]:
                self.play(
                    ApplyMethod(
                        box.move_to,
                        line[2]
                    ),
                    ApplyMethod(
                        g1.edges[(v, u) if v < u else (u, v)].set_color,
                        GREEN_E
                    ),
                    ApplyMethod(
                        g1[v][0].set_color, YELLOW_D
                    ),
                    ApplyMethod(
                        g1[v][1].set_color, BLACK
                    )
                )
                self.wait()
                if not visited[u]:
                    self.play(
                        ApplyMethod(
                            box.move_to,
                            line[3]
                        ),
                        ApplyMethod(
                            g1.edges[(v, u) if v < u else (u, v)].set_color,
                            DEF_PURPLE
                        ),
                        ApplyMethod(
                            g1[u][0].set_color, GREEN_E
                        ),
                        ApplyMethod(
                            g1[u][1].set_color, WHITE
                        )
                    )
                    self.wait()
                    self.play(
                        ApplyMethod(
                            box.move_to,
                            line[4]
                        ),
                        ApplyMethod(
                            g1[v][0].set_color, DEF_PURPLE
                        ),
                        ApplyMethod(
                            g1[v][1].set_color, BLACK
                        )
                    )
                    dfs(u)
                else:
                    self.play(
                        ApplyMethod(
                            box.move_to,
                            line[3]
                        ),
                        ApplyMethod(
                            g1.edges[(v, u) if v < u else (u, v)].set_color,
                            RED_E
                        ),
                        ApplyMethod(
                            g1[u][0].set_color, RED_E
                        ),
                        ApplyMethod(
                            g1[u][1].set_color, WHITE
                        )
                    )
                    self.wait()
                self.play(
                        ApplyMethod(
                            g1.edges[(v, u) if v < u else (u, v)].set_color,
                            DEF_PURPLE
                        ),
                        ApplyMethod(
                            g1[u][0].set_color, DEF_PURPLE
                        ),
                        ApplyMethod(
                            g1[u][1].set_color, BLACK
                        )
                    )
                self.wait()
            self.play(
                ApplyMethod(
                    box.move_to,
                    line[5]
                ),
                ApplyMethod(
                    g1[v][0].set_color, DEF_PURPLE
                ),
                ApplyMethod(
                    g1[v][1].set_color, BLACK
                )
            )
        dfs(root)

class BFSGraphing(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        vertices = [i for i in range(6)]
        edges = [
            (0, 1),
            (0, 2),
            (0, 3),
            (0, 4),
            (1, 5),
            (2, 5),
            (3, 5),
            (4, 5)
        ]
        '''Graph'''
        g = Graph(
            vertices,
            edges,
            layout={
                0:[0, 3, 0],
                1:[-2, 0, 0],
                2:[-1, 0, 0],
                3:[1, 0, 0],
                4:[2, 0, 0],
                5:[0, -3, 0]
            }
        )

        self.play(Create(g))
        self.wait()
        g.generate_target()
        g.target.shift(RIGHT * 3).scale(0.8)
        self.play(
            MoveToTarget(g)
        )
        self.wait()
        '''Graph Labeled'''
        g1 = Graph(
            vertices,
            edges,
            layout={
                0:[0, 3, 0],
                1:[-2, 0, 0],
                2:[-1, 0, 0],
                3:[1, 0, 0],
                4:[2, 0, 0],
                5:[0, -3, 0]
            },
            labels=True
        ).shift(RIGHT * 3).scale(0.8)
        self.play(
            ReplacementTransform(g, g1)
        )
        self.wait()
        '''Code block'''
        dfs_pseudo = Code(
            file_name='assets/codes/bfs_pseudo.cpp',
            font=CODE_FONT,
            tab_width=2,
            insert_line_no=True,
            style='github-dark',
            background='rectangle',
            line_spacing=0.5,
            font_size=20
        ).move_to(LEFT * 3)
        dfs_pseudo.background_mobject.become(VMobject())
        dfs_pseudo.line_numbers.set_color(GREY_B)
        self.play(
            Create(dfs_pseudo)
        )
        label = Text(
            text="宽度优先搜索之队列实现",
            t2c={
                '[7:9]':'#b392f0'
            },
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=BOLD,
            font_size=24,
            fill_opacity=0.6
        ).align_to(dfs_pseudo, UL).shift((0, 2, 0))
        self.play(
            Create(label)
        )
        self.wait()
        '''Execution Box'''
        box = RoundedRectangle(
            corner_radius=0.08,
            color=WHITE,
            height=0.36,
            width=7.7
        ).set_stroke(width=2.5).align_to(dfs_pseudo, UL).shift((-0.1, 0.05, 0.0))
        line = [box.get_center() + (0, -0.31 * i, 0) for i in range(10)]
        self.play(
            Create(box)
        )
        self.wait()
        queue = []
        q_label = Text(
            text='Queue',
            color=DEF_ORANGE,
            font=DEF_FONT,
            font_size=24
        ).align_to(dfs_pseudo, DL).shift((0, -1, 0))
        def q_push(elm: int):
            rect = Text(
                text=str(elm),
                color=ManimColor('#e1e4e8'),
                font=DEF_FONT,
                font_size=24
            )
            if queue:
                rect.next_to(queue[-1], RIGHT, buff=0.1)
            else:
                rect.align_to(q_label, DL).shift((0, -0.5, 0))
            self.play(Create(rect))
            queue.append(rect)
        def q_pop():
            self.play(queue[0].animate.shift(LEFT * 3), rate_func=smooth)
            self.remove(queue.pop(0))
        '''BFS Process'''
        mtx = [[1, 2, 3, 4], [0, 5], [0, 5], [0, 5], [0, 5], [1, 2, 3, 4]]
        root = 0
        visited = [False for i in range(6)]
        def bfs(v):
            self.play(
                ApplyMethod(
                    box.move_to,
                    line[0]
                ),
                ApplyMethod(
                    g1[v][0].set_color, GREEN_E
                ),
                ApplyMethod(
                    g1[v][1].set_color, WHITE
                )
            )
            self.wait()
            q = Queue()
            self.play(
                ApplyMethod(
                    box.move_to,
                    line[1]
                ),
                Create(q_label)
            )
            self.wait()
            visited[v] = True
            q.put(v)
            q_push(v)
            self.play(
                ApplyMethod(
                    box.move_to,
                    line[2]
                ),
                ApplyMethod(
                    g1[v][0].set_color, DEF_PURPLE
                ),
                ApplyMethod(
                    g1[v][1].set_color, BLACK
                )
            )
            self.wait()
            while not q.empty():
                self.play(
                    ApplyMethod(
                        box.move_to,
                        line[3]
                    )
                )
                self.wait()
                w = q.get()
                self.play(
                    ApplyMethod(
                        box.move_to,
                        line[4]
                    ),
                    ApplyMethod(
                        g1[w][0].set_color, YELLOW_D
                    ),
                    ApplyMethod(
                        g1[w][1].set_color, BLACK
                    )
                )
                self.wait()
                q_pop()
                for u in mtx[w]:
                    self.play(
                        ApplyMethod(
                            box.move_to,
                            line[5]
                        ),
                        ApplyMethod(
                            g1.edges[(w, u) if w < u else (u, w)].set_color,
                            GREEN_E
                        )
                    )
                    self.wait()
                    self.play(
                        ApplyMethod(
                            box.move_to,
                            line[6]
                        )
                    )
                    self.wait()
                    if not visited[u]:
                        self.play(
                            ApplyMethod(
                                box.move_to,
                                line[7]
                            ),
                            ApplyMethod(
                                g1[u][0].set_color, GREEN_E
                            ),
                            ApplyMethod(
                                g1[u][1].set_color, WHITE
                            )
                        )
                        self.wait()
                        visited[u] = True
                        q.put(u)
                        # self.play(
                        #     ApplyMethod(
                        #         g1.edges[(w, u) if w < u else (u, w)].set_color,
                        #         DEF_PURPLE
                        #     ),
                        #     ApplyMethod(
                        #         g1[u][0].set_color, DEF_PURPLE
                        #     ),
                        #     ApplyMethod(
                        #         g1[u][1].set_color, BLACK
                        #     )
                        # )
                        q_push(u)
                    else:
                        self.play(
                            ApplyMethod(
                                g1.edges[(w, u) if w < u else (u, w)].set_color,
                                RED_E
                            ),
                            ApplyMethod(
                                g1[u][0].set_color, RED_E
                            ),
                            ApplyMethod(
                                g1[u][1].set_color, WHITE
                            )
                        )
                        self.wait()
                    self.play(
                        ApplyMethod(
                            g1.edges[(w, u) if w < u else (u, w)].set_color,
                            DEF_PURPLE
                        ),
                        ApplyMethod(
                            g1[u][0].set_color, DEF_PURPLE
                        ),
                        ApplyMethod(
                            g1[u][1].set_color, BLACK
                        )
                    )
                    self.wait()
                self.play(
                    ApplyMethod(
                        box.move_to,
                        line[8]
                    ),
                    ApplyMethod(
                        g1[w][0].set_color, DEF_PURPLE
                    ),
                    ApplyMethod(
                        g1[w][1].set_color, BLACK
                    )
                )
                self.wait()
            self.play(
                ApplyMethod(
                    box.move_to,
                    line[9]
                )
            )
            self.wait()
        bfs(root)

class END(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        '''END'''
        bye = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=DEF_FONT,
                   color=DEF_PURPLE).shift(2 * UP)
        bye2 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=DEF_FONT,
                   color=DEF_ORANGE).next_to(bye, DOWN)
        bye3 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=DEF_FONT,
                   color=TEXT_COLOR).next_to(bye2, DOWN)
        bye4 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=DEF_FONT,
                   color=DEF_PURPLE).next_to(bye3, DOWN)
        bye5 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=DEF_FONT,
                   color=DEF_ORANGE).next_to(bye4, DOWN)
        bye6 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=DEF_FONT,
                   color=TEXT_COLOR).next_to(bye5, DOWN)
        grp4 = Group(bye, bye2, bye3, bye4, bye5, bye6)
        grp4.generate_target()
        grp4.target.scale(1.2)
        self.play(
            FadeIn(grp4)
        )
        self.wait()
        self.play(
            MoveToTarget(grp4)
        )
        self.wait()