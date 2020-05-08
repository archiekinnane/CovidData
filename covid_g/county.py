def get_data(county, state):
    import pandas as pd
    #state1 = lengthen_state(state)

    url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
    df = pd.read_csv(url, error_bad_lines=False)

    if state == 'null':
        state = raw_input('What state?')
        if len(state) == 2:
            state = lengthen_state(state)

    is_state = df['state'] == state
    state_data = df[is_state]
    is_county = state_data['county'] == county
    county_data = state_data[is_county]
    return county_data

def graph(county = 'null', state = 'null'):
    import pandas as pd
    if state == 'null':
        state = raw_input('What state? ')
        if len(state) == 2:
            state = lengthen_state(state)

    if county == 'null':
        county = raw_input('What county? ')

    county_data = get_data(county, state)

    import matplotlib.pyplot as plt
    from datetime import datetime

    date_numb = county_data['date'].values
    dates = []
    for i in range(0, len(county_data)):
        dates.append(datetime.strptime(date_numb[i], '%Y-%m-%d'))

    cases = county_data['cases'].values
    deaths = county_data['deaths'].values
    new_county_cases = [cases[0]]
    new_county_deaths = [deaths[0]]
    for i in range(1, len(county_data)):
        new_county_cases.append(cases[i] - cases[i-1])
        new_county_deaths.append(deaths[i] - deaths[i-1])
        
    print ('deaths on ' + str(max(dates)) + ': ' + str(new_county_deaths[len(new_county_deaths) - 1]))
    print ('cases on ' + str(max(dates)) + ': ' + str(new_county_cases[len(new_county_deaths) - 1]))


        
    import numpy as np
    cases = np.array(new_county_cases, dtype=np.float32)
    rolling_cases = pd.rolling_mean(cases, 7, min_periods=4)   
    deaths_ = np.array(new_county_deaths, dtype=np.float32)
    rolling_deaths = pd.rolling_mean(deaths_, 7, min_periods=4) 
    
    plt.title(county + ' county, ' + state + ': cases, deaths')
    plt.plot(dates, county_data['cases'].values, label = county + ' county cases: ' + "{:,}".format(max(county_data['cases'])))
    plt.plot(dates, county_data['deaths'].values, color = 'r', label = county + ' county deaths: ' + "{:,}".format(max(county_data['deaths'])))
    plt.legend(loc='upper left')
    plt.yscale('log')
    plt.show()

    plt.title('Daily Cases')
    plt.bar(dates, new_county_cases, label = 'cases')
    plt.plot(dates, rolling_cases, color = 'r', linewidth = '2', label = '7 day rolling average')
    plt.legend(loc='upper left')
    plt.show()
    
    plt.title('Daily Deaths')
    plt.bar(dates, new_county_deaths, label = 'deaths')
    plt.plot(dates, rolling_deaths, color = 'r', linewidth = '2', label = '7 day rolling average')
    plt.legend(loc='upper left')
    plt.show()



def lengthen_state(state):
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'American Samoa': 'AS',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'District of Columbia': 'DC',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Guam': 'GU',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Northern Mariana Islands':'MP',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Puerto Rico': 'PR',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virgin Islands': 'VI',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY'
    }

    abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))

    return abbrev_us_state[state]
    