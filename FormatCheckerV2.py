# %%
# importing the required modules
import glob
import pandas as pd

# specifying the path to csv files, use // and not \ for hardcoding filepath eg "C://Screenshot Code//1AugData"
path = "C://Screenshot Code//1AugData"
# OR alternatively, use bottom code and comment out above lineif you want to put this file in the folder with the Excel files 
# (easier to track output)
#path = os. getcwd()

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
	colnames=list(df. columns)
	#adds new pair to dictionary
	RCDict.update({filename:[colnames,rows,cols]})

#print(RCDict)	

# converting content to data frame, transpose and clean headers
RCDictDF = pd.DataFrame.from_dict(RCDict)
RCDictDF_transposed = RCDictDF.T
RCDictDF_transposed.columns = ['ColNames','Rows', 'Cols']

# print results in console and export to excel (excel preferred)
RCDictDF_transposed.to_excel(r'format_checker.xlsx')
print (RCDictDF_transposed)



