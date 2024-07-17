from manim import *

class Graph(Scene):
    def construct(self):

        #Create Axes
        axes = Axes(
            x_range=[0,800,100],
            y_range=[0,600000,100000],
            axis_config={"include_numbers":True}
        )
        axes.scale(0.9)
        # labels = axes.get_axis_labels(x_label='LeetCode Hours', y_label='Salary')
        # self.add(labels)
        #I think labels make it look to busy
        x_axis = axes.x_axis
        y_axis = axes.y_axis
        x_axis.save_state()
        y_axis.save_state()

        self.play(Create(axes))

        self.play(x_axis.animate.scale(1.2).set_color(ORANGE))
        self.play(Restore(x_axis), run_time = 1)

        self.play(y_axis.animate.scale(1.2).set_color(GREEN))
        self.play(Restore(y_axis), run_time = 1)


        #Create horizontal line
        def horizontal_line(x):
            #plots functions. so you could even plot a parabola - return x**2
            '''Creates a horizontal line'''
            return 300000
        
        line = axes.plot(horizontal_line, color=BLUE_E)
        self.play(Create(line))
        # self.wait(1)

        # Data points
        x_values = [120,200,300,350,600,650,700]  
        y_values = [49000,100000,250000,350000,400000,450000,450000] 

        # Create dots for each point
        dots = VGroup(*[
            Dot(point=axes.c2p(x, y), color=YELLOW_E, radius=0.05) #c2p is coord 2 points. ensure on axes
            for x, y in zip(x_values, y_values)
        ])

        # Calculate error residuals

        # Animate the scatter points
        self.play(Create(dots))
        self.wait(1)

        # # Creates a group of straight lines from the dots to the horizontal
        # vert_lines = VGroup(*[
        #     Line(dot,axes.c2p(x, 300000)) 
        #     for dot, x in zip(dots,x_values)
        # ])
        # self.play(Create(vert_lines))
        # # self.wait(3)

        # # Minimize residuals via linear regression (animate line best fit)
        
        # #See calculations.ipynb
        # new_y = [92838.35689517,146651.10696186,213917.04454521,247550.01333689,
        #         415714.85729528,449347.82608696,482980.79487863]
        
        # def updated_line(x):
        #     '''Creates y=mx+b for data points'''
        #     #can improve by not using calculations.ipynb and doing calc in here
        #     return x*672.65937583 + 12119.231795145432
        
        # new_line = axes.plot(updated_line, color=PINK)

        # new_vert_lines = VGroup(*[
        #     Line(dot,axes.c2p(x, y)) 
        #     for dot, x, y in zip(dots,x_values,new_y)])

        # self.play(Transform(line, new_line),Transform(vert_lines, new_vert_lines))
        # # self.wait(3)

        # #create sliding box from x and y axis to show price and sqfoot

        # # we can do two decimal numbers to get (x,y)

        # decimal_x = DecimalNumber(
        #     0,
        #     num_decimal_places=2,
        #     unit= r" ,"
        # )

        # decimal_y = DecimalNumber(
        #     0,
        #     num_decimal_places=2,
        #     unit=None
        # )

        # left_paren = Tex("(")
        # right_paren = Tex(")")

        # def update_decimal_x(d):
        #     d.next_to(track, UP)
        #     x_value = axes.p2c(track.get_edge_center(RIGHT))[0]
        #     d.set_value(x_value)

        # def update_decimal_y(d):
        #     d.next_to(decimal_x, RIGHT * 0.1)
        #     y_value = axes.p2c(track.get_edge_center(UP))[1]
        #     d.set_value(y_value)

        # decimal_x.add_updater(update_decimal_x)
        # left_paren.add_updater(lambda x : x.next_to(decimal_x, LEFT))
        # self.add(decimal_x, left_paren)
        # decimal_y.add_updater(update_decimal_y)
        # right_paren.add_updater(lambda x : x.next_to(decimal_y, RIGHT))
        # self.add(decimal_y, right_paren)

        # track = axes.get_lines_to_point(axes.coords_to_point(100,79385.1693785), color=GREEN)
        # track_2 = axes.get_lines_to_point(axes.coords_to_point(700,482980.7948761454), color = GREEN)
        # track_3 = axes.get_lines_to_point(axes.coords_to_point(350,246204.6945839854), color = GREEN)
        # self.play(Create(track)) 
        # # self.wait(2)
        # self.play(ReplacementTransform(track,track_2, run_time = 3))
        # self.add(decimal_x)
        # self.wait(1)
        # self.remove(track_2)
        # self.play(ReplacementTransform(track,track_3, run_time = 3))
        # self.add(decimal_x)
        # self.wait(2)
        

