import csv
print("the first day of the project : 28/4/2022",end="\n")
file = open(r"C:\Users\moham\Downloads\Emissions.csv")
mydict = {}
#read the file
reader = csv.reader(open(r"C:\Users\moham\Downloads\Emissions.csv"))
for i, rows in enumerate(reader):

        k = rows[0]
        v = rows[1:]
        if not k in mydict:
            mydict[k] = [v]
        else:
            mydict[k].append(v)


#take input from user
year = input("enter the year : ")
index_of_year =None
lines = []
"""
Step 2: Extracting index of the year
"""
# Loop through First VALUE of Dictionary and if year present in list then set index of VALUE as index_of
for item in next(iter(mydict.values())):
    if year in item:
        index_of = (item.index(year))

total = 0
i = 0
emissions_in_year = []
"""
Step 3: Creating the list of emission in year
"""
# Loop through VALUES of Dictionary
for value in mydict.values():
    # For the first loop skip the code because in our case it contains Column Names and Years
    if i != 0:
        # Add VALUE of Emission to total
        total += float(value[index_of])
        # Append the value to emissions_in_year
        emissions_in_year.append(list(mydict.values())[i][index_of])
    i += 1


"""
Step 4: Performing the analysis
"""
# Let's try to understand this from inner Single Line loop. We converted String to float and created list, from this
# list we found the maximum and minimum float value, converted that into string and got the index of maximum and
# minimum emission country.
max_country_index = int(emissions_in_year.index(str(max(float(str_value) for str_value in emissions_in_year))))
min_country_index = int(emissions_in_year.index(str(min(float(str_value) for str_value in emissions_in_year))))
average_emissions = total / 195

# Using index value we got the Name of maximum and minimum country name
max_emission = list(mydict.keys())[max_country_index + 1]
min_emission = list(mydict.keys())[min_country_index + 1]


"""
Step 5: Printing the data in required format using formatted string
"""
print(f'In {year}, countries with minimum and maximum CO2 emission levels were: [{min_emission}] '
      f'and [{max_emission}] respectively.')
print(f'Average CO2 emissions in {year} were {"%.6f" % round(average_emissions, 6)}')
print()

