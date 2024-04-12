from manim import *

BACKGROUND_COLOR = ManimColor('#1f2428')
TEXT_COLOR = ManimColor('#e1e4e8')
CUS_PURPLE = ManimColor('#b392f0')
CUS_ORANGE = ManimColor('#f8a56e')
GOD_FONT = 'snas-serif'
# def read_txt(filename: str) -> list[str]:
#     lines = []
#     with open(filename, 'r', encoding='utf8') as file:
#         for line in file.readlines():
#             lines.append(line)
#     return lines
# LINES = read_txt('assets/lines.txt')

class Test(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        icon_matrix = SVGMobject('assets/matrix.svg').scale(0.6).shift(2 * LEFT)
        icon_matrix.generate_target()
        icon_matrix.target.shift(2 * RIGHT).scale(1.2)
        self.play(
            MoveToTarget(icon_matrix)
        )
        self.wait()
        '''Matrix Detail'''
        icon_matrix.generate_target()
        icon_matrix.target.scale(0.3).shift(6.5 * LEFT + 3.5 * UP)
        self.play(
            MoveToTarget(icon_matrix)
        )
        t0 = IntegerTable(
            [[0,1,0,1,0],
            [1,0,0,1,0],
            [0,0,0,0,1],
            [1,1,0,0,1],
            [0,0,1,1,0],],
            col_labels=[
                MathTex("0"),
                MathTex("1"),
                MathTex("2"),
                MathTex("3"),
                MathTex("4")],
            row_labels=[
                MathTex("0"),
                MathTex("1"),
                MathTex("2"),
                MathTex("3"),
                MathTex("4")],
            h_buff=1
            # element_to_mobject_config={"unit": "^{\circ}"}
        ).set_color(TEXT_COLOR).set_row_colors(CUS_ORANGE).set_column_colors(CUS_PURPLE)
        t0.generate_target()
        t0.target.scale(0.8).shift(3 * LEFT)
        self.play(
            Create(t0).set_run_time(2.5)
        )
        self.wait()
        
        '''Example Graph Again'''
        vertices3 = [0, 1, 2, 3, 4]
        edges3 = [(0, 1), (0, 3), (1, 3), (3, 4), (2, 4)]
        self.play(
            MoveToTarget(t0)
        )
        self.wait()
        g3 = Graph(vertices3, edges3, labels=True, layout='circular').shift(3 * RIGHT)
        self.play(
            Create(g3)
        )
        self.wait()
        

class Introduce(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        '''Title'''
        big_man = Text(text='塔菲带你入门图论(1)',
                       font=GOD_FONT,
                       t2c={
                           '[6:8]': '#b392f0'
                           },
                       color=TEXT_COLOR
                       )
        self.play(Create(big_man))
        self.wait(4)
        
        '''Graph Example.'''
        vertices1 = [1, 2, 3, 4]
        edges1 = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g1 = Graph(vertices1, edges1, layout='circular').shift(3 * LEFT)
        self.play(
            ReplacementTransform(big_man, g1)
        )
        self.wait()

        vertices2 = [0, 1, 2, 3, 4, 5]
        edges2 = [(0, 2), (1, 3), (2, 3), (3, 5), (4, 5), (5, 0)]
        g2 = DiGraph(vertices2, edges2, layout='circular').shift(3 * RIGHT)
        self.play(
            Create(g2)
        )
        self.wait(4)
        
        '''Graph Set'''
        graph_formula = Text(text='G = (V, E)',
                             t2c={'[5:6]':'#b392f0',
                                  '[8:9]':'#f8a56e'
                                  },
                             color=TEXT_COLOR)
        graph_formula.generate_target()
        graph_formula.target.shift(UP).scale(0.8)
        self.play(
            FadeOut(g1),
            FadeOut(g2)
        )
        self.wait()
        self.play(Create(graph_formula))
        self.wait()
        expl = Text(text='集合V称为点集，集合E称为边集',
                    font=GOD_FONT,
                    t2c={'[2:3]':'#b392f0',
                         '[5:7]':'#b392f0',
                         '[10:11]':'#f8a56e',
                         '[13:]':'#f8a56e'
                        },
                    color=TEXT_COLOR)
        self.play(MoveToTarget(graph_formula),
                  Create(expl))
        self.wait(3)
        
        '''Graph Example.'''
        self.play(
            FadeOut(graph_formula)
        )
        self.wait()
        self.play(
            ReplacementTransform(expl, g1)
        )
        self.wait()
        self.play(
            Create(g2)
        )
        self.wait(6)
        
        '''Graph Storage'''
        icon_matrix = SVGMobject('assets/matrix.svg').scale(0.6).shift(2 * LEFT)
        icon_form = SVGMobject('assets/form.svg').scale(0.6).shift(2 * RIGHT)
        self.play(FadeTransform(g1, icon_matrix),
                  FadeTransform(g2, icon_form))
        self.wait(9)
        
        '''Adjacency Matrix'''
        icon_matrix.generate_target()
        icon_matrix.target.shift(2 * RIGHT).scale(1.2)
        self.play(
            ReplacementTransform(icon_form, icon_matrix)
        )
        self.wait()
        self.play(
            MoveToTarget(icon_matrix)
        )
        self.wait()
        matrix_text = Text(
            text='邻接矩阵',
            font=GOD_FONT,
            color=CUS_PURPLE
        ).next_to(icon_matrix, DOWN)
        self.play(Create(matrix_text.scale(0.9)))
        self.wait()
        
        '''Matrix Detail'''
        icon_matrix.generate_target()
        icon_matrix.target.scale(0.3).shift(6.5 * LEFT + 3.5 * UP).set_color('#b392f0')
        self.play(
            MoveToTarget(icon_matrix),
            FadeOut(matrix_text)
        )
        '''2d array'''
        t0 = IntegerTable(
            [[0,1,0,1,0],
            [1,0,0,1,0],
            [0,0,0,0,1],
            [1,1,0,0,1],
            [0,0,1,1,0],],
            col_labels=[
                MathTex("0"),
                MathTex("1"),
                MathTex("2"),
                MathTex("3"),
                MathTex("4")],
            row_labels=[
                MathTex("0"),
                MathTex("1"),
                MathTex("2"),
                MathTex("3"),
                MathTex("4")],
            h_buff=1
            # element_to_mobject_config={"unit": "^{\circ}"}
        ).set_color(TEXT_COLOR).set_row_colors(CUS_ORANGE).set_column_colors(CUS_PURPLE)
        t0.generate_target()
        t0.target.scale(0.8).shift(3 * LEFT)
        self.play(
            Create(t0).set_run_time(2.5)
        )
        self.wait()
        
        '''Example Graph Again'''
        vertices3 = [0, 1, 2, 3, 4]
        edges3 = [(0, 1), (0, 3), (1, 3), (3, 4), (2, 4)]
        self.play(
            MoveToTarget(t0)
        )
        self.wait()
        g3 = Graph(vertices3, edges3, labels=True, layout='circular').shift(3 * RIGHT)
        self.play(
            Create(g3)
        )
        self.wait(7)
        nongraph_grp = Group(t0, g3)
        
        '''Directed Graph Storage'''
        t1 = IntegerTable(
            [[0,1,0,0,0],
            [0,0,0,1,0],
            [0,0,0,0,1],
            [1,0,0,0,1],
            [0,0,0,0,0],],
            col_labels=[
                MathTex("0"),
                MathTex("1"),
                MathTex("2"),
                MathTex("3"),
                MathTex("4")],
            row_labels=[
                MathTex("0"),
                MathTex("1"),
                MathTex("2"),
                MathTex("3"),
                MathTex("4")],
            h_buff=1
            # element_to_mobject_config={"unit": "^{\circ}"}
        ).set_color(TEXT_COLOR).set_row_colors(CUS_ORANGE).set_column_colors(CUS_PURPLE).scale(0.8).shift(3 * LEFT)
        vertices4 = [0, 1, 2, 3, 4]
        edges4 = [(0, 1), (0, 3), (1, 3), (3, 4), (2, 4)]
        g4 = DiGraph(vertices4, edges4, labels=True, layout='circular').shift(3 * RIGHT)
        digraph_grp = Group(t1, g4)
        self.play(
            ReplacementTransform(nongraph_grp, digraph_grp)
        )
        self.wait(7)
        
        '''Adjacency List'''
        icon_form = SVGMobject('assets/form.svg').scale(0.6)
        icon_form.scale(1.2).scale(0.3).move_to(icon_matrix.get_center()).set_color('#b392f0')

        t2 = Table(
            [["1", "3"],
            ["3", " "],
            ["4", " "],
            ["4", " "],
            [" ", " "],],
            row_labels=[Text("0", color=CUS_PURPLE), Text("1", color=CUS_PURPLE), Text("2", color=CUS_PURPLE), Text("3", color=CUS_PURPLE), Text("4", color=CUS_PURPLE)],
            include_outer_lines=True).scale(0.8).shift(3 * LEFT)
        t2.remove(*t2.get_vertical_lines())
        self.play(
            ReplacementTransform(t1, t2),
            ReplacementTransform(icon_matrix, icon_form)
        )
        self.wait(8)
        grp3 = Group(icon_matrix, icon_form, t2, g4)
        
        '''Brilliant'''
        vertices5 = [1, 2, 3, 4, 5, 6, 7, 8]
        edges5 = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
                 (2, 8), (3, 4), (6, 1), (6, 2),
                 (6, 3), (7, 2), (7, 4)]
        autolayouts = ["spring", "circular", "kamada_kawai",
                       "planar", "random", "shell",
                       "spectral", "spiral"]
        graphs = [Graph(vertices5, edges5, layout=lt).scale(0.5)
                  for lt in autolayouts]
        r1 = VGroup(*graphs[:3]).arrange()
        r2 = VGroup(*graphs[3:6]).arrange()
        r3 = VGroup(*graphs[6:]).arrange()
        grpb = VGroup(r1, r2, r3).arrange(direction=DOWN)
        self.play(
            TransformMatchingShapes(grp3, grpb)
        )
        self.wait()
        
        graphs = [Graph(vertices5, edges5, layout=lt).scale(0.5)
                  for lt in autolayouts]
        r1 = VGroup(*graphs[:3]).arrange()
        r2 = VGroup(*graphs[3:6]).arrange()
        r3 = VGroup(*graphs[6:]).arrange()
        grpb2 = VGroup(r1, r2, r3).arrange(direction=DOWN)
        self.play(
            ReplacementTransform(grpb, grpb2)
        )
        self.wait()
        
        '''END'''
        bye = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=GOD_FONT,
                   color=CUS_ORANGE).shift(2 * UP)
        bye2 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=GOD_FONT,
                   color=CUS_PURPLE).next_to(bye, DOWN)
        bye3 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=GOD_FONT,
                   color=TEXT_COLOR).next_to(bye2, DOWN)
        bye4 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=GOD_FONT,
                   color=CUS_ORANGE).next_to(bye3, DOWN)
        bye5 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=GOD_FONT,
                   color=CUS_PURPLE).next_to(bye4, DOWN)
        bye6 = Text('关注永雏塔菲喵~ 关注永雏塔菲谢谢喵！',
                   font=GOD_FONT,
                   color=TEXT_COLOR).next_to(bye5, DOWN)
        grp4 = Group(bye, bye2, bye3, bye4, bye5, bye6)
        grp4.generate_target()
        grp4.target.scale(1.2)
        self.play(
            TransformMatchingShapes(grpb2, grp4)
        )
        self.wait()
        self.play(
            MoveToTarget(grp4)
        )
        self.wait()
        # self.play(FadeOut(g2))
        # self.wait()
        # self.play(Create(icon_form))
        # self.intro_lines()
    
    # def intro_lines(self):
    #     line = Text(text='',
    #                  font="sans-serif",
    #                  color=TEXT_COLOR)
    #     for line_str in LINES:
    #         line = Text(text=line_str,
    #                     font="sans-serif",
    #                     color=TEXT_COLOR).shift(2*DOWN)
    #         self.play(
    #             Create(line)
    #         )
    #         self.wait()
    #         self.play(
    #             FadeOut(line).set_run_time(0.5)
    #         )
