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



        # Data points
        x_values = [100,120,150,200,300,350,400,500,600,650,700,635,720]  
        y_values = [80000,49000,51000,60000,100000,250000,350000,340000,375000,400000,450000,450000,365000] 

        # Create dots for each point
        dots = VGroup(*[
            Dot(point=axes.c2p(x, y), color=WHITE, radius=0.05) #c2p is coord 2 points. ensure on axes
            for x, y in zip(x_values, y_values)
        ])

        # Calculate error residuals

        # Animate the scatter points
        self.play(Create(dots))
        self.wait(1)

        #Create horizontal line
        def horizontal_line(x):
            #plots functions. so you could even plot a parabola - return x**2
            '''Creates a horizontal line'''
            return 300000
        
        line = axes.plot(horizontal_line, color=BLUE_E)
        self.play(Create(line))
        # self.wait(1)

        # Creates a group of straight lines from the dots to the horizontal
        vert_lines = VGroup(*[
            Line(dot,axes.c2p(x, 300000), color = RED_E, stroke_width = 0.9) 
            for dot, x in zip(dots,x_values)
        ])
        self.play(Create(vert_lines), run_time = 3)
        # self.wait(3)

        # Minimize residuals via linear regression (animate line best fit)
        
        #See calculations.ipynb
        new_y = [44988.15422359, 58249.50692707, 78141.5359823, 111294.917741,
       177601.68125842, 210755.06301713, 243908.44477583, 310215.20829325,
       376521.97181066, 409675.35356937, 442828.73532807, 399729.33904175,
       456090.08803156]
        
        def updated_line(x):
            '''Creates y=mx+b for data points'''
            #can improve by not using calculations.ipynb and doing calc in here
            return x*663.06763517 - 21318.609293823363
        
        new_line = axes.plot(updated_line, color=BLUE_E)

        new_vert_lines = VGroup(*[
            Line(dot,axes.c2p(x, y), color = RED_E, stroke_width = 0.9) 
            for dot, x, y in zip(dots,x_values,new_y)])

        self.play(Transform(line, new_line),Transform(vert_lines, new_vert_lines))
        #HERE
        # self.wait(3)

        #create sliding box from x and y axis to show price and sqfoot

        # we can do two decimal numbers to get (x,y)

        decimal_x = DecimalNumber(
            0,
            num_decimal_places=0,
            unit= r'hr'
            
        )

        decimal_y = DecimalNumber(
            0,
            num_decimal_places=0,
            unit=None
        )

        #make y a vgroup with a prefix $. use buff=

        def update_decimal_x(d):
            
            x_value = axes.p2c(track.get_edge_center(RIGHT))[0]
            d.set_value(x_value)
            d.set_color(ORANGE)
            d.next_to(track, UP)

        def update_decimal_y(d):
            
            y_value = axes.p2c(track.get_edge_center(UP))[1]
            d.set_value(y_value)
            d.set_color(GREEN)
            d.next_to(track, RIGHT)

        

        track = axes.get_lines_to_point(axes.coords_to_point(100,44988), color=YELLOW)
        track_2 = axes.get_lines_to_point(axes.coords_to_point(700,442828), color = YELLOW)
        track_3 = axes.get_lines_to_point(axes.coords_to_point(350,210755), color = YELLOW)

        decimal_x.set_opacity(0).add_updater(update_decimal_x)
        decimal_y.set_opacity(0).add_updater(update_decimal_y)
        self.add(decimal_x, decimal_y)

        self.play(Create(track)) 
        decimal_x.set_opacity(1)
        decimal_y.set_opacity(1)
        self.play(FadeIn(decimal_x),FadeIn(decimal_y))
        self.wait(2)
        self.play(Transform(track,track_2, run_time = 3))
        self.wait(1)
        self.play(Transform(track,track_3, run_time = 3))
        self.wait(2)
        

