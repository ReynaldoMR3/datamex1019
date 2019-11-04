#Using the pipeline to clean the data
The pipeline has the following functions to clean the data.

read_csv(ruta):
    Reads the csv archive and stores it in a variable.

dropping_columns(CONSTANT):
    Drops empty columns
 
renaming_columns(CONSTANT):
    renames the columns so they don't have blank spaces between their names.
    
cleaning_colyear(CONSTANT):
    drops years that doesn't contain 4 digits
    
changing(string):
    changes strings names of the months like (sep, oct, nov, etc) for the number of the month

cleaning_coldate(CONSTANT):
    changes the column Date type to string and cleans if the string doesnt contain the following order
    (digits, - , word or digit, - digits)
    
cleaning_cnum(CONSTANT):
    changes the column casenumber and cleans if its not a date, applies to all casenumber columns
    
cleaning_type(CONSTANT):
    changes the column type to str, lowercase and cleans it to have consistent values
    
cleaning_country(CONSTANT):
    changes the column country type to str, lowercase and cleans it to have consistent values

clear_area(CONSTANT):
    changes the column area type to str, lowercase and cleans it to have consistent values
    
clear_location(CONSTANT):
    changes the column location type to str, lowercase and cleans it to have consistent values


human_activity(string):
    returns a variable with a string in a list of the human activities

cleaning_activity(CONSTANT):
    changes the column activity to type str, lower case and applies the human_activity to have consistent activities
 
cleaning_names(CONSTANT):
    changes the column names type to str, lowercase and cleans it to have consistent values
    
cleaning_sex(CONSTANT):
    changes the column names type to str, lowercase and cleans it to have M, or F as values

cleaning_age(CONSTANT):
    changes the column age type to str, lowercase and cleans it to have only 2 digits values

cleaning_injuries(CONSTANT):
    changes the column Injury type to str, lowercase and cleans it to have consistent values

cleaning_fatal(CONSTANT):
    changes the column Fatal type to str, lowercase and cleans it to have Y, or N as values

cleaning_time(CONSTANT):
    changes the column type to str, lowercase, and cleans for consisten values of 2 digits, word, 2digits
    

shark_species(string):
    returns a variable that contains the type of the shark that is obtained from a list in the function.
    
cleaning_species(CONSTANT):
    cleans the column species, applies the shark_species function to have consistent values in the column Species
    
#Insights obtained

1.- The year with most shark attacks is 2015 with 139 attacks, data obtained from the following code:
    print(clear_database['Year'].value_counts())

2.- The top 3 human activities that causes more shark attacks are:
    1.- swimming (1017)
    2.- surfing (1013)
    3.- fishing(651)
    Data obtained from: print(clear_database['Year'].value_counts())

3.- The top 3 shark species that attacked the more humans are:
    1.- white (606)
    2.- tiger (250)
    3.- bull (163)
    Data obtained from: print(clear_database['Species'].value_counts())

4.- The top 3 countries with more shark attacks are:
    1.- usa (2116)
    2.- australia (1279)
    3.- south africa (565)
    data obtained from: print(clear_database['Country'].value_counts()
    
5.- 1552 attacks of sharks were fatal.
    data obtained from: print(clear_database['Fatal'].value_counts()

6.- The top 3 hours that sharks attacked the most are:
    1.- 11h00 (124)
    2.- 12h00 (108)
    3.- 15h00 (102)
    data obtained from: print(clear_database['Time'].value_counts())
    
#Interesting facts by column

#Activity
'washing his pig in preparation for a religious ceremony'
'closed circuit diving (submerged). diving to recover jettisoned packets of opium for police'
'defecating in water beneath the docks'
'during "an exhibition" he was tied in sack & thrown overboard'
'jumped overboard after murdering 2 shipmates'
'painting a ship'

#Name
'Richard Branson'

