
#####################
""" WAFFLE CHARTS """
#####################

"""
Waffle Chart: visualise data that is normally created to display progress towards goals.For example, 
tiles will represent a countries contribution towards a goal.

Matplotlib does not have this by default so we need to created our own function.
"""


###################
""" WORD CLOUDS """
###################

"""
Word Cloud: depiction of frequency of different words in some textual data. Words with higher
frequency will appear bigger and bolder.

Matplotlib does not have this by default so we need to created our own function, but there is 
a package that does help us to create this.
"""


##################################
""" SEABORN & REGRESSION PLOTS """
##################################

"""
- Seaborn is a Python visualization library based on Matplotlib
- Visuals that need around 20 lines of code can be reduced 5-fold
"""

# create a regression plot with one line
import seaborn as sns
ax = sns.regplot(x="year", y="total", data=df_total)

# add parameters to change color and/or marker
ax = sns.regplot(x="year", y="total", data=df_total, color="green", marker="+")
