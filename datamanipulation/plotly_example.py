#import plotly.express as px

#df = px.data.iris()

#fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
#fig.show()

#Example 2

import plotly.express as px

df = px.data.gapminder().query("country == 'France'")

fig = px.line(df, x="year", y="gdpPercap", title="GDP over time")
fig.show()
#example 3
fig = px.bar(df, x="year", y="gdpPercap")
fig.show()