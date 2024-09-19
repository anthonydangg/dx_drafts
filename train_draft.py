from manim import *
#import sklearn?

# config.pixel_height = 1920  # Height for portrait
# config.pixel_width = 1080   # Width for portrait
# config.frame_height = 9  # Manim units (scales content to fit the height)
# config.frame_width = 16    # Manim units (scales content to fit the width)

class intro(Scene):
    def construct(self):
        self.camera.background_color = hex_to_rgb("#312b54")
        grad = SVGMobject("assets/graduate.svg")
        grad.set_color(WHITE)
        self.play(SpiralIn(grad), run_time=3)
        self.wait(1)
        self.play(grad.animate.move_to(LEFT))
        
        gamer = SVGMobject("assets/gamer.svg")
        gamer.set_color(WHITE).scale(0.9)
        gamer.next_to(grad, RIGHT).shift(DOWN * 0.1, RIGHT * 0.3)
        
        self.play(SpiralIn(gamer), run_time =3)
        self.wait(1)
        
class features(Scene):
    def number_line(self, x_range, length, direction, pointer_direction, rotation):
        """
        Creates a number line with a pointer and a DecimalNumber that updates
        """
        number_line = NumberLine(
            x_range=x_range,
            length=length,
            include_numbers=False,
            rotation=rotation,
            label_direction=direction,
        )

        tracker = ValueTracker(0)
        pointer = Vector(pointer_direction)
        pointer.add_updater(lambda m: m.next_to(number_line.n2p(tracker.get_value()), direction))

        decimal = DecimalNumber(0)
        decimal.add_updater(lambda m: m.set_value(tracker.get_value()).next_to(pointer, direction))
        return number_line, pointer, decimal, tracker
    
    def construct(self):
        self.camera.background_color = hex_to_rgb("#312b54")

        lx, pointer_x, hours, tracker_x = self.number_line([0, 70, 5], 10, UP, DOWN, 0)
        hours.set_num_decimal_places(0)

        self.add(lx, pointer_x, hours)
        self.play(tracker_x.animate.set_value(70), run_time = 2)
        self.play(FadeOut(pointer_x,hours))
        self.wait(1) 

        ly, pointer_y, gpa, tracker_y = self.number_line([0, 4.5, 0.5], 7, RIGHT, LEFT, 90*DEGREES)

        self.play(ReplacementTransform(lx,ly))
        self.play(ly.animate.move_to(LEFT))
        

        self.add(ly, pointer_y, gpa)
        self.play(tracker_y.animate.set_value(4.5), run_time = 2)
        self.wait(1)

# class decision_boundary(Scene):
#     def construct(self):

    

#for loop to fill screen with svgs?
#then shrink and disperse into train, test, valid