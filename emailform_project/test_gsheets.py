import gspread

# Authenticate using your service account credentials
gc = gspread.service_account(filename='credentials.json')

# Open the spreadsheet by its name
sh = gc.open('Emails')  # Replace 'Emails' with your sheet's exact name

# Select the first worksheet
worksheet = sh.sheet1

# Data to append
row = ['test2@example.com', 'Test Subject', 'Test Content', '', '']

# Append the row
worksheet.insert_row(row,2)

print("Row appended successfully!")
