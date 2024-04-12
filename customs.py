from manim import *
from manim.camera.camera import Camera
class CustomScene(Scene):
    def __init__(self, renderer=None, camera_class=..., always_update_mobjects=False, random_seed=None, skip_animations=False):
        super().__init__(renderer, camera_class, always_update_mobjects, random_seed, skip_animations)