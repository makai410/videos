from manim import *

BACKGROUND_COLOR = ManimColor('#181818')
TEXT_COLOR = ManimColor('#dddddd')
DEF_GREEN = ManimColor('#66b395')
DEF_PURPLE = ManimColor('#a0a5d6')
DEF_ORANGE = ManimColor('#f3a580')
DEF_FONT = 'Source Han Serif SC'
CODE_FONT = 'Cascadia Code'

class Intro(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        detail = Text(
            text='高考数学公益网课系列',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=48
        )
        
        title = Text(
            text="六月边陲",
            color=DEF_GREEN,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=64
        ).move_to(UP * 1.4).align_to(detail, LEFT)
        
        author = Text(
            text='作者：@mapleland_ , @makai410',
            t2c= {
                '[0:3]':'#66b395'
            },
            color=GRAY_C,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=24
        ).move_to(DOWN * 2)
        self.play(
            Create(title)
        )
        self.play(
            Create(detail)
        )
        self.play(
            Create(author)
        )
        self.wait()
        
        subject = Text(
            text='高考导数中的高超方法',
            t2c= {
                '[6:]':'#66b395'
            },
            color=GRAY_C,
            font=DEF_FONT,
            weight=HEAVY
        )
        subject2 = Text(
            text='Hermite-Hadamard不等式',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY
        )
        self.play(
            FadeOut(title, author),
            Transform(detail, subject)
        )
        
        self.wait()
        detail.generate_target()
        detail.target.shift(UP*1.4).scale(0.8)
        self.play(
            MoveToTarget(detail)
        )
        self.play(
            Create(subject2)
        )
        self.wait()

class TianJin(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        title = Text(
            text='[2020·天津卷 T20]',
            color=GRAY_C,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=28
        ).move_to(UP * 3 + LEFT * 4.5)
        
        t1 = Text(
            text='已知函数',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=32
        ).move_to(UP * 2).align_to(title, LEFT)
        
        tex1 = MathTex(
            'f(x)=x^3+k\ln x (k \in R) , f^\prime (x)'
        ).move_to(t1.get_right(), LEFT)

        t2 = Text(
            text='为',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=32
        ).move_to(tex1.get_right(), LEFT)
        
        tex2 = MathTex('f(x)').move_to(UP * 2).move_to(t2.get_right(), LEFT)
        
        t3 = Text(
            text='的导函数',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=32
        ).move_to(tex2.get_right(), LEFT)
        vg1 = VGroup(t1, tex1, t2, tex2, t3)
        self.play(
            Create(title),
            Create(vg1)
        )
        self.wait()

class YaLiExample(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        title = Text(
            text='[2024.4·雅礼中学 T19]',
            color=GRAY_C,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=28
        ).move_to(UP * 3 + LEFT * 4.5)
        
        t1 = Text(
            text='已知函数',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=32
        ).move_to(UP * 2).align_to(title, LEFT)
        
        tex1 = MathTex(
            'f(x)=x^4+a\ln x (a \in R) \quad f^\prime (x)'
        ).move_to(t1.get_right(), LEFT)

        t2 = Text(
            text='为',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=32
        ).move_to(tex1.get_right(), LEFT)
        
        tex2 = MathTex('f(x)').move_to(UP * 2).move_to(t2.get_right(), LEFT)
        
        t3 = Text(
            text='的导函数,',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=32
        ).move_to(tex2.get_right(), LEFT)
        
        tex3 = MathTex('g(x)=f^\prime (x).').move_to(UP).align_to(title, LEFT)
        vg1 = VGroup(t1, tex1, t2, tex2, t3, tex3)
        
        
        '''小题'''
        a1 = Text(
            text='(2)',
            color=DEF_GREEN,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=26
        ).move_to(UP * 0.1).align_to(title, LEFT)
        a11 = Text(
            text="设",
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=26
        ).move_to(a1.get_right() * 0.98, LEFT)
        
        ex1 = MathTex(
            ". \,",
            r"P \bigl(x_1, g(x_1)\bigl), \; Q \bigl(x_2, g(x_2)\bigl),",
            ". \, ."
        ).move_to(a11.get_right(), LEFT)
        ex1[0].set_color(BACKGROUND_COLOR)
        ex1[2].set_color(BACKGROUND_COLOR)
        
        a2 = Text(
            text='其中',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=26
        ).move_to(ex1.get_right(), LEFT)
        
        ex2 = MathTex(
            ". \, ",
            "1 \le x_2 < x_1. ",
        ).move_to(a2.get_right(), LEFT)
        ex2[0].set_color(BACKGROUND_COLOR)
        
        a3 = Text(
            text='若直线PQ的斜率为k,  且',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=26
        ).move_to(UP * -1).align_to(a11, LEFT)
        
        ex3 = MathTex(
            ".\, ",
            "k < \cfrac{g^\prime(x_1) + g^\prime(x_2)}{2},",
            "\,."
        ).move_to(a3.get_right(), LEFT)
        ex3[0].set_color(BACKGROUND_COLOR)
        ex3[2].set_color(BACKGROUND_COLOR)
        
        a4 = Text(
            text='求实数a的取值范围.',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=26
        ).move_to(ex3.get_right(), LEFT)
        vg2 = VGroup(a1, a11, ex1, a2, ex2, a3, ex3, a4)
        self.play(
            Create(title),
            Create(vg1)
        )
        self.wait()

        self.play(
            Create(vg2)
        )
        self.wait()

class HNSD(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        
from scipy.optimize import root_scalar
class CoordProve(Scene):
    def construct(self):
        # 绘制交点，参考：https://discord.com/channels/581738731934056449/1216636172277776435
        self.camera.background_color = BACKGROUND_COLOR
        
        tracker = ValueTracker(1)
        def f(x):
            return tracker.get_value()*(3*x**2+53/x)/16 + (1-tracker.get_value())*(x+2)

        def t(x):
            return x+2
        
        def F(x):
            return tracker.get_value()*(x**3+53*np.log(x))/16  + (1-tracker.get_value())*(0.5*x**2 + 2*x)

        axes = Axes(x_range=[-1, 8, 1], y_range=[-1, 10, 1], x_length=9, y_length=7)
        
        linear = axes.plot(lambda x: t(x), x_range=[1, 7], color=TEXT_COLOR)
        
        func = always_redraw(
            lambda: axes.plot(lambda x: f(x),x_range=[1, 7], color=DEF_GREEN)
        )
        self.add(tracker)

        # def dotUpdater(mobj):
        #     roots = []
        #     for x0 in np.arange(1, 7, 0.1):
        #         root = root_scalar(lambda x: f(x)-t(x), x0 = x0, method = 'newton')
        #         if root.converged and root.root > 0:
        #             roots.append(root.root)
        #     roots = np.unique(np.round(roots,2))
        #     grp = VGroup(
        #         *[Dot().set_color(DEF_GREEN).move_to(axes.c2p(root, t(root))) for root in roots]
        #     )
        #     try:
        #         grp.add(Text(
        #                 text='A',
        #                 color=TEXT_COLOR,
        #                 font=DEF_FONT,
        #                 weight=BOLD,
        #                 font_size=30
        #             ).move_to(axes.c2p(roots[0], t(roots[0])), DR)
        #         )
        #         grp.add(Text(
        #                 text='B',
        #                 color=TEXT_COLOR,
        #                 font=DEF_FONT,
        #                 weight=BOLD,
        #                 font_size=30
        #             ).move_to(axes.c2p(roots[1], t(roots[1])), DR)
        #         )
        #     except:
        #         print('none')
        #     mobj.become(grp)
        # dots.add_updater(dotUpdater)
        grp = VGroup()
        roots = [1.14, 6.55]
        dots = VGroup(
            *[Dot().set_color(DEF_GREEN).move_to(axes.c2p(root, t(root))) for root in roots]
        )
        grp.add(
            Text(
                text='A',
                color=TEXT_COLOR,
                font=DEF_FONT,
                weight=BOLD,
                font_size=30
            ).move_to(axes.c2p(roots[0], t(roots[0])), DR)
        )
        grp.add(
            Text(
                text='B',
                color=TEXT_COLOR,
                font=DEF_FONT,
                weight=BOLD,
                font_size=30
            ).move_to(axes.c2p(roots[1], t(roots[1])), DR)
        )
        self.play(
            Create(axes),
            Create(func),
            Create(linear),
            Create(grp),
            Create(dots)
        )
        self.play(tracker.animate.set_value(0),run_time=5)
        self.wait()

        x1 = np.round((roots[0] + roots[1]) / 2,2)
        dC = Dot().set_color(DEF_GREEN).move_to(axes.c2p(x1, t(x1)))
        lbC = Text(
            text='C',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=BOLD,
            font_size=30
        ).move_to(axes.c2p(x1, t(x1)), DR)
        self.play(
            Create(dC),
            Create(lbC)
        )
        self.wait()
        
        dD = Dot().set_color(DEF_GREEN).move_to(axes.c2p(x1, np.round(f(x1), 2)))
        lbD = Text(
            text='D',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=BOLD,
            font_size=30
        ).move_to(axes.c2p(x1, np.round(f(x1), 2)), DL)
        self.play(
            Create(dD),
            Create(lbD)
        )
        self.wait()
        
        dtemp1 = Dot().move_to(axes.c2p(roots[0], 0)).set_color(DEF_GREEN)
        dtemp2 = Dot().move_to(axes.c2p(roots[1], 0)).set_color(DEF_GREEN)
        linA = Line(dots[0], dtemp1).set_color(DEF_GREEN)
        linB = Line(dots[1], dtemp2).set_color(DEF_GREEN)
        lines = axes.get_vertical_lines_to_graph(
            func, x_range=[roots[0], roots[1]], num_lines=30, color=DEF_GREEN
        )
        self.play(
            Create(dtemp1),
            Create(dtemp2),
            Create(linA),
            Create(linB),
            Create(lines)
        )
        self.wait()
        yE = np.round((F(roots[1]) - F(roots[0])) / (roots[1] - roots[0]), 2)
        dE = Dot().set_color(DEF_GREEN).move_to(axes.c2p(x1, yE))
        lbE = Text(
            text='E',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=BOLD,
            font_size=30
        ).move_to(axes.c2p(x1, yE), UR)
        self.play(
            Create(dE),
            Create(lbE)
        )
        self.wait()

class CoordProveOne(Scene):
    def construct(self):
        # 绘制交点，参考：https://discord.com/channels/581738731934056449/1216636172277776435
        self.camera.background_color = BACKGROUND_COLOR
        def f(x):
            return (3*x**2+53/x)/16

        def t(x):
            return x+2
        
        def F(x):
            return (x**3+53*np.log(x)) / 16

        axes = Axes(x_range=[-1, 8, 1], y_range=[-1, 10, 1], x_length=9, y_length=7)
        func = axes.plot(lambda x: (3*x**2+53/x)/16,x_range=[1, 7], color=DEF_GREEN)
        linear = axes.plot(lambda x: x+2, x_range=[1, 7], color=TEXT_COLOR)
        
        dots = VGroup()
        def dotUpdater(mobj):
            roots = []
            for x0 in np.arange(1, 7, 0.1):
                root = root_scalar(lambda x: f(x)-t(x), x0 = x0, method = 'newton')
                if root.converged and root.root > 0:
                    roots.append(root.root)
            roots = np.unique(np.round(roots,2))
            grp = VGroup(
                *[Dot().set_color(DEF_GREEN).move_to(axes.c2p(root, t(root))) for root in roots]
            )
            grp.add(Text(
                    text='A',
                    color=TEXT_COLOR,
                    font=DEF_FONT,
                    weight=BOLD,
                    font_size=30
                ).move_to(axes.c2p(roots[0], t(roots[0])), DR)
            )
            grp.add(Text(
                    text='B',
                    color=TEXT_COLOR,
                    font=DEF_FONT,
                    weight=BOLD,
                    font_size=30
                ).move_to(axes.c2p(roots[1], t(roots[1])), DR)
            )
            mobj.become(grp)
        dots.add_updater(dotUpdater)
        self.play(
            Create(axes),
            Create(func),
            Create(linear),
            Create(dots)
        )
        self.wait()
        roots = [1.14, 6.55]
        
        x1 = np.round((roots[0] + roots[1]) / 2,2)
        dC = Dot().set_color(DEF_GREEN).move_to(axes.c2p(x1, t(x1)))
        lbC = Text(
            text='C',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=BOLD,
            font_size=30
        ).move_to(axes.c2p(x1, t(x1)), DR)
        self.play(
            Create(dC),
            Create(lbC)
        )
        self.wait()
        
        dD = Dot().set_color(DEF_GREEN).move_to(axes.c2p(x1, np.round(f(x1), 2)))
        lbD = Text(
            text='D',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=BOLD,
            font_size=30
        ).move_to(axes.c2p(x1, np.round(f(x1), 2)), DR)
        self.play(
            Create(dD),
            Create(lbD)
        )
        self.wait()
        
        dtemp1 = Dot().move_to(axes.c2p(roots[0], 0)).set_color(DEF_GREEN)
        dtemp2 = Dot().move_to(axes.c2p(roots[1], 0)).set_color(DEF_GREEN)
        linA = Line(dots[0], dtemp1).set_color(DEF_GREEN)
        linB = Line(dots[1], dtemp2).set_color(DEF_GREEN)
        lines = axes.get_vertical_lines_to_graph(
            func, x_range=[roots[0], roots[1]], num_lines=30, color=DEF_GREEN
        )
        self.play(
            Create(dtemp1),
            Create(dtemp2),
            Create(linA),
            Create(linB),
            Create(lines)
        )
        self.wait()
        yE = np.round((F(roots[1]) - F(roots[0])) / (roots[1] - roots[0]), 2)
        dE = Dot().set_color(DEF_GREEN).move_to(axes.c2p(x1, yE))
        lbE = Text(
            text='E',
            color=TEXT_COLOR,
            font=DEF_FONT,
            weight=BOLD,
            font_size=30
        ).move_to(axes.c2p(x1, yE), DR)
        self.play(
            Create(dE),
            Create(lbE)
        )
        self.wait()