import pandas 
import plotly_express

df = pandas.read_csv("covidinfo.csv")
figure = plotly_express.scatter(df, x = "date", y = "cases", color = "country", title = "Covid-Cases"  )
figure.show()