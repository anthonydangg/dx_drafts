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
        self.play(Create(axes))

        # self.wait(1)

        #Create horizontal line
        def horizontal_line(x):
            #plots functions. so you could even plot a parabola - return x**2
            '''Creates a horizontal line'''
            return 300000
        
        line = axes.plot(horizontal_line, color=PINK)
        self.play(Create(line))
        # self.wait(1)

        # Data points
        x_values = [120,200,300,350,600,650,700]  
        y_values = [49000,100000,250000,350000,400000,450000,450000] 

        # Create dots for each point
        dots = VGroup(*[
            Dot(point=axes.c2p(x, y), color=BLUE, radius=0.09) #c2p is coord 2 points. ensure on axes
            for x, y in zip(x_values, y_values)
        ])

        # Calculate error residuals

        # Animate the scatter points
        self.play(Create(dots))
        # self.wait(1)

        # Creates a group of straight lines from the dots to the horizontal
        vert_lines = VGroup(*[
            Line(dot,axes.c2p(x, 300000)) 
            for dot, x in zip(dots,x_values)
        ])
        self.play(Create(vert_lines))
        # self.wait(3)

        # Minimize residuals via linear regression (animate line best fit)
        
        #See calculations.ipynb
        new_y = [92838.35689517,146651.10696186,213917.04454521,247550.01333689,
                415714.85729528,449347.82608696,482980.79487863]
        
        def updated_line(x):
            '''Creates y=mx+b for data points'''
            #can improve by not using calculations.ipynb and doing calc in here
            return x*672.65937583 + 12119.231795145432
        
        new_line = axes.plot(updated_line, color=PINK)

        new_vert_lines = VGroup(*[
            Line(dot,axes.c2p(x, y)) 
            for dot, x, y in zip(dots,x_values,new_y)])

        self.play(Transform(line, new_line),Transform(vert_lines, new_vert_lines))
        # self.wait(3)

        #create sliding box from x and y axis to show price and sqfoot

        #test: get ValueTracker moving along linear reg
        # -> axes.get_lines_to_point transform w/ ValueTracker

        track = axes.get_lines_to_point(axes.coords_to_point(100,300000), color=GREEN)
        self.play(Create(track))
        self.wait(3)

