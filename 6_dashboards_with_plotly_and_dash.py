
#############################
""" DASHBOARDING OVERVIEW """
#############################

"""
Dashboards give:
    - real-time visuals
    - understand business moving parts
    - visually track, analyse and display key performance indicators (KPI)
    - take informed decisions and improve performance
    - reduced hours of analysing
"""


##############################
""" INTRODUCTION TO PLOTLY """
##############################

"""
Plotly: an interactive, open-source plotting library (Python, R, javascript).

Plotly Graph Objects: low-level interface to figures, traces and layout.

Plotly Express: high-level wrapper
"""

# using plotly.graph_objects
# import required packages
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# set random seed for reproducibility
np.random.seed(10)
x = np.arange(12)
# create random y values
y = np.random.randint(50, 500, size=12)

# Line Plot using graph objects
# plotly.graph contains a JSON object which has a structure of dict
# here, 'go', is the plotly JSON object
# updating values of 'go' object keywords, chart can be plotted
# create figure and add trace (scatter)

fig = go.Figure(data=go.Scatter(x=x, y=y))
fig.update_layout(title="Simple Line Plot", xaxis_title="Month", yaxis_title="Sales")
fig.show()

# using plotly.express
# entire line chart can be created in single command
fig = px.line(x=x, y=y, title="Simple Line Plot", labels=dict(x="Month", y="Sales"))
sig.show()


############################
""" INTRODUCTION TO DASH """
############################

"""
Dash: 
    - open-source user interface Python library form Plotly
    - easy to build GUI
    - declarative and reactive
    - rendered in web browser and can be deployed to servers
    - inherently cross-platform and mobile ready
    
Dash has two components:
    - Core components -> import dash_core_components as dcc
    - HTML components -> import dash_html_components as html
"""


###################################
""" MAKE DASHBOARDS INTERACTIVE """
###################################

"""
Dash Callback Function: automatically called by Dash whenever input component's property changes.
It is decorated by -> @app.callback
"""






















