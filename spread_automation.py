"""
poetry add ezsheets
"""
import ezsheets
sheet_url = "your_google_sheet_url"
# open the sheet
sheet = ezsheets.Spreadsheet(sheet_url)
# set the title
sheet.title = "Super Sheet Demo"
# get the first sheet page
first = sheet[0]
# set A1 cell to "Hello"
first["A1"] = "Hello"
# update multiple cells
first.updateRow(1, ["Hello2333444", "World", "!!!"])

# update multiple cells
data = [1,2,3,4,5,6,7,8,9,10]
for i in data:
    first.updateRow(i + 1, [data[i]])