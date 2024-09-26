from manim import *
#import sklearn?

# config.pixel_height = 1920  # Height for portrait
# config.pixel_width = 1080   # Width for portrait
# config.frame_height = 9  # Manim units (scales content to fit the height)
# config.frame_width = 16    # Manim units (scales content to fit the width)
config.background_color = hex_to_rgb("#312b54")
class intro(Scene):
    def construct(self):
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

class decision_boundary(Scene):
    def construct(self):
        plane = NumberPlane()
        db = Line(start=[-5,-3,0], end=[5,3,0])
        self.add(db)
        # self.add(plane)
        self.play(Create(db))
        # self.wait(1)

        grad = SVGMobject("assets/graduate.svg")
        grad.shift(3*UP + 2*RIGHT)
        grad2 = SVGMobject("assets/graduate.svg")
        grad2.shift(2*UP + 2*LEFT)
        grad3 = SVGMobject("assets/graduate.svg")
        grad3.shift(1*DOWN + 5*LEFT)
        grads = VGroup(grad,grad2,grad3)
        grads.set_color(WHITE) 
        self.play(FadeIn(grads))
        gamer = SVGMobject("assets/gamer.svg")
        gamer.shift(2*DOWN)
        gamer2 = SVGMobject("assets/gamer.svg")
        gamer2.shift(2*DOWN + 5*RIGHT)
        gamer3 = SVGMobject("assets/gamer.svg")
        gamer3.shift(3*DOWN + 2*RIGHT)
        gamers = VGroup(gamer,gamer2,gamer3)
        gamers.set_color(WHITE) 
        self.play(FadeIn(gamers))
        self.wait(1)
        

class zoom(MovingCameraScene):
    def construct(self):
        #arrange in gird

        grads = VGroup(*[
            SVGMobject("assets/graduate.svg")
            for i in range(24)
            ])
        grads.set_color(WHITE)
        grads.arrange_in_grid(
            buff=(0.25,0.5),
            col_alignments="lccccr",
            row_alignments="uccd", #don't understand row/col alignment
            col_widths=[1, *[None]*4, 1],
            row_heights=[1, None, None, 1],
            flow_order="rd"
        )
        for grad in grads:
            self.play(FadeIn(grad, scale=0.5), run_time=0.2)

        self.wait(1)

        self.play(grads.animate.scale(0.5))
        self.play(grads.animate.to_corner(DR))
        #just do half grads half gamers then split to left/right






    

#for loop to fill screen with svgs?/ can use uniform grid
#then shrink and disperse into train, test, valid