# Data load and clean 

import pandas as pnd

ALLData = pnd.read_csv("./test.csv")
# print(ALLData)

# removing character 
ALLData['value'] = ALLData['value'].astype(str).replace("[^0-9.-]","", regex=True)  
# converting string to number
ALLData['value'] = pnd.to_numeric(ALLData['value'],errors="coerce")
# drop nan values
ALLData = ALLData.dropna(subset=["value"])

sortedData = ALLData.sort_values(by="value", ascending=True)

sortedData.to_csv("sortedData2.csv", index=False)
# print(f'dataa{sortedData}')
# sortedDatas = pnd.read_csv("./sortedData.csv")
# print(sortedDatas)
