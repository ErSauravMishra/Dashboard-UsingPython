import pandas as pnd

cleanedData = pnd.read_csv("./sortedData2.csv")

# finding top 5 values 
cleanedData["value"] = pnd.to_numeric(cleanedData["value"], errors="coerce")

topValues = cleanedData.groupby("industry_name_ANZSIC").filter(lambda x: x["value"].max() > 100000)

# topValues.to_csv('topvalues.csv',index=False)
print(topValues)

# print(topValues)