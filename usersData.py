# Import necessary modules
import pandas as pd
import numpy as np

# Read the existing user data from the Excel file
try:
    userData = pd.read_excel("usrData9.xlsx", sheet_name="usersData8")
except:
    # If the file does not exist or the sheet does not exist, create a new data frame
    userData = pd.DataFrame()

# Get user input
firstN = str(input("Please Enter your First Name: "))
lastN = str(input("Please Enter your Last Name: "))
dateOfb = input("Please Enter your Date of birth: ")

# Calculate age based on date of birth for the new user and add to the 'Age' column
today = pd.to_datetime('today')
newAge = np.floor((today - pd.to_datetime(dateOfb, format='%Y-%m-%d')).days / 365.25)

# Add the new user data and calculated age to the data frame
newData = pd.DataFrame({'FirstName': [firstN],
                        'LastName': [lastN],
                        'DateOfBirth': [dateOfb],
                        'Age': [newAge]})
userData = userData.append(newData, ignore_index=False)

# Write the updated user data to the Excel file
with pd.ExcelWriter("usrData9.xlsx", engine="xlsxwriter", mode="w") as writer:
    userData.to_excel(writer, sheet_name="usersData8", index=False)
