
##################################
""" INTRODUCTION TO MATPLOTLIB """
##################################
import pip

"""
Matplotlib Architecture:
    - Scripting Layer (pyplot)
    - Artist Layer (Artist)
    - Backend Layer (FigureCanvas, Renderer, Event)
    
Backend Layer has 3 built-in abstract interface classes:
    - FigureCanvas: 
        matplotlib.backend_bases.FigureCanvas
        (encompasses the area onto which the figure is drawn)
    - Renderer: 
        matplotlib.backend_bases.Renderer
        (knows how to draw on the FigureCanvas)
    - Event: 
        matplotlib.backend_bases.Event
        (handles user inputs such as keyboard strokes and mouse clicks)
        
Artist Layer:
    - comprised of one main object (Artist) which knows how to use the renderer to draw on the canvas
    - title, lines, tick labels and images all correspond to individual artist instances
    - Two types of Artist objects:
        1. Primitive: Line2D, Rectangle, Circle and Text
        2. Composite: Axis, Tick, Axes and Figure
    - each composite artist may contain other composite artists as well as primitive artists
    
Scripting Layer:
    - comprised of mainly pyplot, a scripting interface that is lighter that Artist

"""

###########################################
# generating a histogram using Artist layer
###########################################
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas  # import FigureCanvas
from matplotlib.figure import Figure  # import Figure artist
fig = Figure()
canvas = FigureCanvas(fig)

# create 10000 random numbers
import numpy as np
x = np.random.randn(10000)

ax = fig.add_subplot(111)  # create and axes artist

ax.hist(x, 100)  # generate a histogram of the 10000 numbers with 100 bins

# add a title to the figure and save it
ax.set_title("Normal Distribution With mu=0, sigma=1$")
fig.savefig("matplotlib_histogram.png")

###################################################
# generating histogram of 10000 numbers with pyplot
###################################################
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, 100)
plt.title(r"Normal Distribution With mu=0, sigma=1$")
plt.savefig("matplotlib_histogram.png")
plt.show()


######################################
""" BASIC PLOTTING WITH MATPLOTLIB """
######################################

# basic plot of a point at coordinates (5,5)
import matplotlib.pyplot as plt

plt.plot(5, 5, "o")
plt.show()

"""
In Jupyter use the backend:
    - %matplotlib inline -> to generate plots within page
    - %matplotlib notebook -> to generate updated plots within page, titles, axes, etc. can be added
      after the creation of the plot, unlike using the backend inline
"""

# matplotlib and pandas basic plots
# consider we have a dataframe called india_china
india_china_df.plot(kind="line")  # creates a line graph from the data in dataframe
india_china_df["india"].plot(kind="hist")  # creates histogram on india data


########################################
""" DATASET ON IMMIGRATION TO CANADA """
########################################

# we will need to import the following
import numpy as np
import pandas as pd

# install xlrd to extract data from Excel
# !pip install xlrd

# read dataframe
df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

df_can.head()


##################
""" LINE PLOTS """
##################

"""
- use with continuous data
"""

















