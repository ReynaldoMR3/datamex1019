import pandas as pd
import numpy as np
import warnings
import regex as re

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

warnings.filterwarnings(action='ignore')


def read_csv(ruta):
    # Leyendo el archivo de csv
    guarda_csv = pd.read_csv(ruta)
    return guarda_csv


def dropping_columns(CONSTANT):
    # Eliminando columnas extras
    clean_data = CONSTANT.drop(columns=['Unnamed: 22', 'Unnamed: 23'])
    return clean_data


def renaming_columns(CONSTANT):
    # Cambiando el nombre de las columnas que contienen espacios entre sus nombres
    new_columns = CONSTANT.rename(
        columns={'Case Number': 'CaseNumber', 'Sex ': 'Sex', 'Fatal (Y/N)': 'Fatal', 'Species ': 'Species',
                 'Investigator or Source': 'Investigator', 'pdf': 'PDF', 'href formula': 'RefLink',
                 'Case Number.1': 'CaseNumber1', 'Case Number.2': 'CaseNumber2', 'original order': 'OriginalOrder'})
    return new_columns


def cleaning_colyear(CONSTANT):  # Eliminando años que no contengan 4 digitos
    # Cambiando el dtype de int a str
    CONSTANT['Year'] = CONSTANT['Year'].astype(str)
    CONSTANT['Year'] = CONSTANT['Year'].str.extract(r'^(\d{4})', expand=False)
    CONSTANT['Year'].fillna(0, inplace=True)
    # Cambiando el dtype de str a int
    CONSTANT['Year'] = CONSTANT['Year'].astype(int)
    return CONSTANT


def changing(string):
    # Changes date to number
    a = ''
    dictionary = {'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06', 'jul': '07',
                  'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'}
    for i in dictionary.keys():
        if str(i) in str(string):
            a = str(string).replace(str(i), dictionary[i]).replace('r', '').replace('ap', '04')
    return a


def cleaning_coldate(CONSTANT):
    CONSTANT['Date'] = CONSTANT['Date'].astype(str)
    CONSTANT['Date'] = CONSTANT['Date'].str.extract(r'^(\d+-(\w+|d+)-\d+)', expand=False)
    CONSTANT['Date'] = CONSTANT['Date'].str.lower()
    CONSTANT['Date'] = CONSTANT['Date'].apply(changing)
    return CONSTANT


def cleaning_cnum(CONSTANT):
    CONSTANT['CaseNumber'] = CONSTANT['CaseNumber'].astype(str)
    CONSTANT['CaseNumber'] = CONSTANT['CaseNumber'].str.replace('.', '-')
    CONSTANT['CaseNumber'] = CONSTANT['CaseNumber'].str.extract(r'(\d+-\d+-\d{2})', expand=False)
    CONSTANT['CaseNumber1'] = CONSTANT['CaseNumber1'].str.replace('.', '-')
    CONSTANT['CaseNumber1'] = CONSTANT['CaseNumber1'].str.extract(r'(\d+-\d+-\d{2})', expand=False)
    CONSTANT['CaseNumber2'] = CONSTANT['CaseNumber2'].astype(str)
    CONSTANT['CaseNumber2'] = CONSTANT['CaseNumber2'].str.replace('.', '-')
    CONSTANT['CaseNumber2'] = CONSTANT['CaseNumber2'].str.extract(r'(\d+-\d+-\d{2})', expand=False)
    return CONSTANT


def cleaning_type(CONSTANT):
    CONSTANT['Type'] = CONSTANT['Type'].astype(str)
    CONSTANT['Type'] = CONSTANT['Type'].str.replace('Boating', 'Boat')
    return CONSTANT


def cleaning_country(CONSTANT):
    CONSTANT['Country'] = CONSTANT['Country'].astype(str)
    CONSTANT['Country'] = CONSTANT['Country'].str.lower()
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('\(uae\)', '')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('?', '')
    CONSTANT['Country'] = CONSTANT['Country'].str.rstrip(" ")
    CONSTANT['Country'] = CONSTANT['Country'].str.lstrip(" ")
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('atlantic ocean', 'sea').replace('diego garcia', '')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('st. maartin', 'st. martin')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('gulf of aden', 'sea').replace('nan', '')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('caribbean sea', 'sea').replace('egypt / israel', 'egypt')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('northern arabian sea', 'sea').replace('egypt / israel',
                                                                                                 'egypt')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('north atlantic ocean', 'sea').replace('south china sea',
                                                                                                 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('pacific ocean', 'sea').replace('south pacific ocean',
                                                                                          'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('red sea', 'sea').replace('north pacific ocean',
                                                                                    'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('mid atlantic ocean', 'sea').replace('south atlantic ocean',
                                                                                               'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('mid atlantic ocean', 'sea').replace('south atlantic ocean',
                                                                                               'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('north sea', 'sea').replace('?', '').replace(
        'andaman / nicobar islandas',
        'andaman')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('iran \/ iraq', 'iran').replace('central pacific', 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('indian ocean', 'sea').replace('central pacific', 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('\ / vanuatu', 'solomon islands').replace('central pacific',
                                                                                                    'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('southwest pacific ocean', 'sea').replace('mid-pacifc ocean',
                                                                                                    'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('\ / croatia', 'italy').replace('ocean', 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('mediterranean sea', 'sea').replace(
        'between portugal & india', 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('asia', 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('sea / sea', 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('mid sea', 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('solomon islandssolomon islands', 'solomon islands')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('southwest sea', 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('italyitaly', 'italy')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('equatorial guinea / cameroon', 'cameroon')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('tasman sea', 'sea')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('ceylon \(sri lanka\)', 'sri lanka')
    CONSTANT['Country'] = CONSTANT['Country'].str.replace('coast of africa', 'africa')
    return CONSTANT


def clear_area(CONSTANT):
    CONSTANT['Area'] = CONSTANT['Area'].astype(str)
    CONSTANT['Area'] = CONSTANT['Area'].str.lower()
    CONSTANT['Area'] = CONSTANT['Area'].str.rstrip(" ")
    CONSTANT['Area'] = CONSTANT['Area'].str.lstrip(" ")
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('nan', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('-', ' ')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('.', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('\(', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('\)', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('\'', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('·', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace(',', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace(r'(\d+\s+\w+\s+\w+\s+)', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('st  catherine', 'st catherine')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('maranh„o', 'maranho')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('peter the great bay khasan primorsky krai far east',
                                                    'primorsky krai')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('telyakovsky bay khasan  primorsky krai far east', 'primorsky krai')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('cook islans', 'cook islands')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between somalia & yemen', 'somalia')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('of the canary islands', 'canary islands')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('cargados carajos shoals st  brandon', 'st brandon')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('st  johns reef', 'st johns reef')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('kwazulu natal between port edward and port st johns', 'kwazulu')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('cikobia island north of vanua levu', 'cikobia island')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('dí…tang salè', 'salè')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('mexico / caribbean sea', 'caribbean sea')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace(r'\d+\W+\w+\s+\d+\W+\w+', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace(r'\d+\w+\s+\d+\W+\w+', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace(r'\d+\w+', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace(r'\d+\w+\s+\d+\w+', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace(r'\d+\w+\s\W+\s+\d+\w+', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace(r'\W+\d+\W+', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('the coast of iran & 483km from mouth of persian gulf',
                                                    'the coast of iran')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between dr and puerto rico', 'puerto rico')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between honiara & isabel island', 'honiara')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('st  marys parish', 'st marys parish')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('st  marys parish', 'st marys parish')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between timor & darwin australia', 'timor')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between hawaii & wake island', 'hawaii')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between kwajalein atoll & johnston island', 'kwajalein atoll')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('in transit between tinian and leyte', 'tinian')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between southampton & canary islands', 'southampton')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between england & south africa', 'england')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('near the andaman & nicobar islands', 'the andaman')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between comores & madagascar', 'comores')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between hawaii and usa', 'hawaii')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('near the fiji islands', 'fiji islands')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace(' \/ ', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('off ', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('of ', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('"', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('in convoy ob ', '')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between noumea & sydney', 'noumea')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('somewhere between philadelphia and hiogo japan', 'philadelphia')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('somewhere between philadelphia and hiogo japan', 'philadelphia')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between hastings & fairlight sussex', 'hastings')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between australia & usa', 'australia')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between new ireland & new britain', 'new ireland')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between beira & maputo', 'beira')
    CONSTANT['Area'] = CONSTANT['Area'].str.replace('between perth & colombo', 'perth')
    return CONSTANT


def clear_location(CONSTANT):
    CONSTANT['Location'] = CONSTANT['Location'].astype(str)
    CONSTANT['Location'] = CONSTANT['Location'].str.lower()
    CONSTANT['Location'] = CONSTANT['Location'].str.rstrip(" ")
    CONSTANT['Location'] = CONSTANT['Location'].str.lstrip(" ")
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('nan', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('-', ' ')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('.', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('\(', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('\)', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('\'', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('·', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace(',', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace(' \/ ', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('off ', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('of ', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('"', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('?', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('20 k the spit the gold coast', 'gold coast')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('8 miles mobile', 'mobile')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('20 miles from shore', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('500 km the coast pernambuco', 'coast pernambuco')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('winterhaven park           ponce inlet volusia county',
                                                            'winterhaven park')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('butler beach st augustine       st johns county',
                                                            'butler beach st augustine')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('between dee why and long reef', 'dee why')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('between sodwana & cape vidal', 'sodwana')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('350 miles from faial island', 'faial island')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('between dyer island and pearly beach', 'dyer island')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('100 miles ft myers beach', 'myers beach')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('between st maarten & anguilla', 'st maarten')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('albany incident took place 200 metres from swimmers',
                                                            'albany')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('3 km port victoria yorke peninsula', 'port victoria')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace(
        '1/4 to 1/2 m north the jetty at bunkers eureka humboldt county', 'bunkers eureka humboldt county')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace(
        'coco beach dar es salaam reported as the 5th fatality in 3 months at coco beach', 'coco beach')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('coco beach dar es salaam', 'coco beach')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace(
        'long island near madang about 500 km 310 miles north the south pacific nations capital port moresby',
        'long island')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('coco beach in oyster bay 7 km north dar es salaam',
                                                            'coco beach')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('between  makena & molokini maui', 'makena')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('panama bay 8∫n 79∫w', 'panama bay')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('v?ng t‡u', '')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('15 miles up the cataract river', 'cataract river')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('18 miles southwest bermuda', 'southwest bermuda')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('35 miles fujairah', 'fujairah')
    CONSTANT['Location'] = CONSTANT['Location'].str.replace('3 miles jupiter palm beach county',
                                                            'jupiter palm beach county')
    return CONSTANT


def human_activity(string):
    new = ''
    list_of_activity = ['surfing', 'swimming', 'fishing', 'spearfishing', 'bathing', 'diving', 'boarding', 'wading',
                        'snorkeling', 'kayaking', 'floating', 'skiing', 'walking', 'playing', 'standing', 'lying',
                        'sitting', 'racing', 'race', 'fell', 'sea disaster', 'sank', 'caught fire', 'catching',
                        'finning', 'resting', 'sunk', 'attempting to swim', 'wreck', 'opihi', 'hauling',
                        'washed overboard',
                        'jumped', 'tsunami', 'gathering', 'feeding', 'photographing', 'filming', 'rescuing', 'washing',
                        'touching', 'rowing', 'disaster', 'crash', 'hurricane', 'torpedo', 'hit', 'went down',
                        'swamped', 'exhibition']
    for i in list_of_activity:
        if i in string:
            new = string.replace(string, i)
    return new


def cleaning_activity(CONSTANT):
    CONSTANT['Activity'] = CONSTANT['Activity'].astype(str)
    CONSTANT['Activity'] = CONSTANT['Activity'].str.lower()
    CONSTANT['Activity'] = CONSTANT['Activity'].str.rstrip(" ")
    CONSTANT['Activity'] = CONSTANT['Activity'].str.lstrip(" ")
    CONSTANT['Activity'] = CONSTANT['Activity'].str.replace('nan', '')
    CONSTANT['Activity'] = CONSTANT['Activity'].apply(human_activity)
    return CONSTANT


def cleaning_names(CONSTANT):
    CONSTANT['Name'] = CONSTANT['Name'].astype(str)
    CONSTANT['Name'] = CONSTANT['Name'].str.lower()
    CONSTANT['Name'] = CONSTANT['Name'].str.rstrip(" ")
    CONSTANT['Name'] = CONSTANT['Name'].str.lstrip(" ")
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('unknow', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('male', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('female', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('occupant: ', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('\\n', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('*', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace(r'\d+', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('fe', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('_', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('-', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('boat: occupants: ', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('occupants', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('no details', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('fishermen', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('nan', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('boy', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('boat', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('anonymous', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('sailor', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('child', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('girl', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('stoways', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('fishing . : ', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('a british citizen', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("24' boat shark tagger occupant keith poe", '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("occupants: hamza humaid al sahraía & 5 crew",
                                                    'hamza humaid al sahraía')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace(" m :   stephen & andrew crust", 'stephen & andrew crust')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("kayak: occupant kelly janse van rensburg",
                                                    'kelly janse van rensburg')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("dinghy: occupant robbie graham", 'robbie graham')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("avalon, a carbon kevlar monohull: 8 occupants", '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("racing scull: occupant trevor carter", 'trevor carter')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("22-ft boat.  occupant captain scott fitzgerald",
                                                    'scott fitzgerald')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("boat: occupants: tim watson & allan de sylva",
                                                    'tim watson & allan de sylva')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("passenger rry norman atlantic", '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('people claimed to have been injured by a "baby" shark', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('avalon, a carbon kevlar monohull:  ', '')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('dinghy. : jeff kurr and andy casagrande',
                                                    'eff kurr and andy casagrande')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace('m inflatable . : bhad battle & kevin overmeyer',
                                                    'bhad battle & kevin overmeyer')
    CONSTANT['Name'] = CONSTANT['Name'].str.replace("", "", '')
    return CONSTANT


def cleaning_sex(CONSTANT):
    CONSTANT['Sex'] = CONSTANT['Sex'].astype(str)
    CONSTANT['Sex'] = CONSTANT['Sex'].str.rstrip(" ")
    CONSTANT['Sex'] = CONSTANT['Sex'].str.lstrip(" ")
    CONSTANT['Sex'] = CONSTANT['Sex'].str.replace("nan", '').replace('lli', '').replace("N", '').replace('.', '')
    return CONSTANT


def cleaning_age(CONSTANT):
    CONSTANT['Age'] = CONSTANT['Age'].astype(str)
    CONSTANT['Age'] = CONSTANT['Age'].str.rstrip(" ")
    CONSTANT['Age'] = CONSTANT['Age'].str.lstrip(" ")
    CONSTANT['Age'] = CONSTANT['Age'].str.extract(r'^(\d{2})', expand=False)
    CONSTANT['Age'].fillna(0, inplace=True)
    return CONSTANT


def cleaning_injuries(CONSTANT):
    CONSTANT['Injury'] = CONSTANT['Injury'].astype(str)
    CONSTANT['Injury'] = CONSTANT['Injury'].str.rstrip(" ")
    CONSTANT['Injury'] = CONSTANT['Injury'].str.lstrip(" ")
    return CONSTANT


def cleaning_fatal(CONSTANT):
    CONSTANT['Fatal'] = CONSTANT['Fatal'].astype(str)
    CONSTANT['Fatal'] = CONSTANT['Fatal'].str.rstrip(" ")
    CONSTANT['Fatal'] = CONSTANT['Fatal'].str.lstrip(" ")
    CONSTANT['Fatal'] = CONSTANT['Fatal'].str.replace("nan", '')
    CONSTANT['Fatal'] = CONSTANT['Fatal'].str.replace("UNKNOWN", '')
    CONSTANT['Fatal'] = CONSTANT['Fatal'].str.replace("F", '')
    CONSTANT['Fatal'] = CONSTANT['Fatal'].str.replace("#VALUE", '')
    CONSTANT['Fatal'] = CONSTANT['Fatal'].str.replace("n", 'N')
    CONSTANT['Fatal'] = CONSTANT['Fatal'].str.replace("!", 'N')
    return CONSTANT


def cleaning_time(CONSTANT):
    CONSTANT['Time'] = CONSTANT['Time'].astype(str)
    CONSTANT['Time'] = CONSTANT['Time'].str.rstrip(" ")
    CONSTANT['Time'] = CONSTANT['Time'].str.lstrip(" ")
    CONSTANT['Time'] = CONSTANT['Time'].str.extract(r'^(\d{2}\w\d{2})', expand=False)
    return CONSTANT


def shark_species(string):
    new = ''
    list_of_activity = ['tiger', 'white', 'bull', 'blacktip', 'blue', 'nurse', 'lemon', 'white', 'angel', 'tawny','mako',
                        'bronze', 'wobbegong', 'grey', 'sandtiger', 'silky', 'spinner', 'hammerhead', 'juvenile', 'baby',
                        'small', 'whitetip', 'reef', 'raggedtooth', 'zambesi', 'porbeagle', 'cow', 'sevengill', 'basking',
                        'dusky', 'blackfin', 'soupfin', 'sand', 'leopard', 'sandbar', 'copper', 'carpet', 'broadnose',
                        'thresher', 'silvertip', 'whale', 'shovelnose', 'blue pointer']
    for i in list_of_activity:
        if i in string:
            new = string.replace(string, i)
    return new


def cleaning_species(CONSTANT):
    CONSTANT['Species'] = CONSTANT['Species'].astype(str)
    CONSTANT['Species'] = CONSTANT['Species'].str.lower()
    CONSTANT['Species'] = CONSTANT['Species'].str.rstrip(" ")
    CONSTANT['Species'] = CONSTANT['Species'].str.lstrip(" ")
    CONSTANT['Species'] = CONSTANT['Species'].apply(shark_species)
    return CONSTANT

