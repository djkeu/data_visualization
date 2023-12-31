# data_visualization

Python crash course
Project 2: Data visualization

Note: 'q' closes figure

# Chapter 15: Generating data, p.305

# Installing MatplotLib, p.306
# Plotting a simple line graph, p.306
        mpl_squares.py
    Changing the label type and line thickness, p.307
    Correcting the plot, p.309
    Using built-in styles, p.310
    Plotting and styling individual points with scatter(), p.310
        scatter_squares.py
    Plotting a series of points with scatter(), p.312
    Calculating data automatically, p.312
    Defining custom colors, p.314
    Using a colormap, p.314
    Saving your plots automatically, p.315


# Try it yourself, p.315
## 15-1 Cubes
        A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.
            cubes.py
    
## 15-2 Coloured cubes
        Apply a colormap to your cubes plot.
            cubes.py


# Random walks, p.315
    Creating the RandomWalk() class, p.316
        random_walk.py
    Choosing directions, p.316
    Plotting the random walk, p.317
        rw_visual.py
    Generating multiple random walks, p.318
    Styling the walk, p.319
        Coloring the points, p.319
        Plotting the starting and endig points, p.320
        Cleaning up the axes, p.321
        Adding plot points, p.321
        Altering the size to fill the screen, p.322


# Try it yourself, p.323
## 15-3 Molecular motion
        Modify rw_visual.py by replacing plt.scatter() with plt.plot(). To simulate the path of a pollen grain on the surface of a drop of water, pass in the rw.x_values and rw.y_values, and include a linewidth argument. Use 5000 instead of 50,000 points
            molecular_motion.py
    
## 15-4 Modified random walks
        In the RandomWalk class, x_step and y_step are generated from the same set of conditions. The direction is chosen randomly from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4]. Modify the values in these lists to see what happens to the overall shape of your walks. Try a longer list of choices for the distance, such as 0 through 8, or remove the −1 from the x or y direction list.
            molecular_walk.py
    
## 15-5 Refactoring
        The fill_walk() method is lengthy. Create a new method called get_step() to determine the direction and distance for each step, and then calculate the step. You should end up with two calls to get_step() in fill_walk():
        
        x_step = self.get_step()
        y_step = self.get_step()
        
        This refactoring should reduce the size of fill_walk() and make the method easier to read and understand.
            random_walk.py


# Rolling dice with Plotly, p.323
    Installing Plotly, p.324
    Creating the Die class, p.324
        die.py
    Rolling the die, p.325
        die_visual.py
    Analyzing the results
    Rolling two dice, p.328
    Rolling dice of different sized, p.329


# Try it yourself, p.331
## 15-6 Two D8's
    Create a simulation showing what happens when you roll two eight-sided dice 1000 times. Try to picture what you think the visualization will look like before you run the simulation; then see if your intuition was correct. Gradually increase the number of rolls until you start to see the limits of your system’s capabilities.
        two_d8s.py

## 15-7 Three Dice
    When you roll three D6 dice, the smallest number you can roll is 3 and the largest number is 18. Create a visualization that shows what happens when you roll three D6 dice.
        three_dice.py

## 15-8 Multiplication
    When you roll two dice, you usually add the two numbers together to get the result. Create a visualization that shows what happens if you multiply these numbers instead.
        multiplication.py

## 15-9 Die Comprehensions
    For clarity, the listings in this section use the long form of for loops. If you’re comfortable using list comprehensions, try writing a comprehension for one or both of the loops in each of these programs.

## 15-10 Practicing with Both Libraries
    Try using Matplotlib to make a die-rolling visualization, and use Plotly to make the visualization for a random walk. (You’ll need to consult the documentation for each library to complete this exercise.)
        mpl_die.py
        plotly_walk.py
