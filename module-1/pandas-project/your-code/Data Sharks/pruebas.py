from Callinit import *

data_shark = read_csv('attacks.csv')

data_shark_clean = dropping_columns(data_shark)

data_shark_clean = renaming_columns(data_shark_clean)

new_data = cleaning_colyear(data_shark_clean)

clear_date = cleaning_coldate(new_data)

clear_date = cleaning_cnum(clear_date)

clear_type = cleaning_type(clear_date)

clear_country = cleaning_country(clear_type)

clear_areav = clear_area(clear_country)

clear_database = clear_location(clear_areav)

clear_database = cleaning_activity(clear_database)

clear_database = cleaning_names(clear_database)

clear_database = cleaning_sex(clear_database)

clear_database = cleaning_age(clear_database)

clear_database = cleaning_injuries(clear_database)

clear_database = cleaning_fatal(clear_database)

clear_database = cleaning_time(clear_database)

clear_database = cleaning_species(clear_database)

#print(clear_database.head())
print(clear_database['Time'].value_counts())
print(clear_database.columns)

clear_database.to_csv('sharks_clean.csv')
