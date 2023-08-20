# %%
# importing the required modules
import glob
import pandas as pd

# specifying the path to csv files, use // and not \ for hardcoding filepath eg "C://Screenshot Code//1AugData"
path = "C://Screenshot Code//1AugData"

# csv files in the path
files = glob.glob(path + "/*.xlsx")

# defining an empty list to store
# content
data_frame = pd.DataFrame()
content = []
#contentDF=pd.DataFrame()
RCDict = {}

# checking all the csv files in the
# specified path
for filename in files:
	
	# reading content of csv file
	# content.append(filename)
	df = pd.read_excel(filename, sheet_name='Sheet1')
	#print(df)
	rows=(len(df))
	cols=(len(df.columns))
	#adds new pair to dictionary
	RCDict.update({filename:[rows,cols]})
	

# converting content to data frame, transpose and clean headers
RCDictDF = pd.DataFrame.from_dict(RCDict)
RCDictDF_transposed = RCDictDF.T
RCDictDF_transposed.columns = ['Rows', 'Cols']

# print results in console and export to excel (excel preferred)
RCDictDF_transposed.to_excel(r'format_checker.xlsx')
print (RCDictDF_transposed)



