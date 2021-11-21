
##################
""" AREA PLOTS """
##################
import numpy as np

"""
Area Plot: represent cumulated totals using numbers or percentages over time.

Note that we need to use the '.transpose()' method as Matplotlib by default would have the
country names in the x-axis whereas, we want the years to be there instead.
"""

# generating area plot
# first we create a transposed dataframe
years = list(map(str, range(1980, 2014)))

df_canada.sort_values(["Total"]), ascending = False, axis = 0, inplace = True)

df_top5 = df_canada.head()
df_top5 = df_top5[years].transpose()  # to switch axes

# now we create the area plot
import matplotlib as mpl
import matplotlib.pyplot as plt

df_top5.plot(kind="area")
plt.title("Immigration trend of top 5 countries")
plt.ylabel("Number of immigrants")
plt.xlabel("Years")
plt.show()


##################
""" HISTOGRAMS """
##################

"""
Histograms: represent the frequency of distribution of a variable.
"""

# generating histogram
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as mp

count, bin_edges = np.histogram(df_canada["2013"])  # aligns the bin edges with ticks on x-axis
df_canada["2013"].plot(kind="hist")
plt.title("Histogram of immigration from 195 countries in 2013")
plt.ylabel("Number of countries")
plt.xlabel("Number of immigrants")
plt.show()


##################
""" BAR CHARTS """
##################

"""
Bar Charts: used to compare values of a variable at a given point in time.
"""

# generating bar chart

import matplotlib as mpl
import matplotlib.pyplot as plt

df_canada["2013"].plot(kind="bar")
plt.title("Histogram of immigration from 195 countries in 2013")
plt.ylabel("Number of countries")
plt.xlabel("Number of immigrants")
plt.show()
