import plotly.express

fig = plotly.express.bar(x = ["A","B","C"], y = [10,20,30])
fig.write_html("bar_chart.html")
fig.show()