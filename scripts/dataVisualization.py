import pandas as pnd
import matplotlib.pyplot as matPlot
import seaborn as sea

filteredData = pnd.read_csv('./sortedData2.csv')
matPlot.figure(figsize=(8, 4))
sea.lineplot(x="industry_name_ANZSIC", y="value", data=filteredData)
matPlot.xticks(rotation=20)
matPlot.title("Dataaa")
matPlot.show()
