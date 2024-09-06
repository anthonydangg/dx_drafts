from manim import *

# config.pixel_height = 1920  # Height for portrait
# config.pixel_width = 1080   # Width for portrait
# config.frame_height = 9  # Manim units (scales content to fit the height)
# config.frame_width = 16    # Manim units (scales content to fit the width)

class style(Scene):
    def construct(self):
        self.camera.background_color = hex_to_rgb("#312b54")
        svg = SVGMobject("assets/rain.svg")
        svg.set_color(WHITE)
        self.play(FadeIn(svg))