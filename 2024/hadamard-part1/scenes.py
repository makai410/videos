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
            text='Hadamard不等式',
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

class ExampleIntro(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR
        title = Text(
            text='2020·天津卷 P20',
            color=GRAY_C,
            font=DEF_FONT,
            weight=HEAVY,
            font_size=24
        ).move_to(UP * 3 + LEFT * 5)
        
        tex = Tex(
            r'$f(x)=x^3 + k\ln x$  $(k \in R)$, $f^\prime (x)$为$f(x)$的导数',
            tex_template=TexTemplateLibrary.ctex,
            font_size=42
        ).move_to(UP * 2)
        self.play(
            Create(title),
            Create(tex)
        )
        self.wait()