def graph(state = 'null'):
    if state == 'null':
        state = raw_input('What state? ')
    if len(state) > 2:
        state = shorten_state(state)


    import pandas as pd
    #state1 = lengthen_state(state)

    url = 'https://covidtracking.com/api/v1/states/daily.csv'
    df = pd.read_csv(url, error_bad_lines=False)

    is_state = df['state'] == state
    state_data = df[is_state]

    import matplotlib.pyplot as plt
    from datetime import datetime

    date_numb = state_data['date'].values
    dates = []
    for i in range(0, len(state_data)):
        dates.append(datetime.strptime(str(date_numb[i]), '%Y%m%d'))

    positive = state_data['positive'].values
    tested = state_data['total'].values
    death = state_data['death'].values
    hospitalized = state_data['hospitalized'].values
    newcases = state_data['positiveIncrease'].values
    newtests = state_data['totalTestResultsIncrease'].values
    newdeaths = state_data['deathIncrease'].values
    newhosp = state_data['hospitalizedIncrease'].values
    cases = state_data['positive'].values
    #deaths = state_data['deaths'].values
    new_state_cases = state_data['positiveIncrease'].values
    reversed_ = new_state_cases[::-1]
    
    new_state_deaths = state_data['deathIncrease'].values
    reversed_death = new_state_deaths[::-1]
    
    rolling_deaths = pd.rolling_mean(reversed_death, 7, min_periods=1)
    
    plt.bar(dates, state_data['total'].values, label = 'tests: ' + "{:,}".format(int(max(state_data['total'].values))))
    plt.bar(dates, state_data['positive'].values, label = 'cases: ' + "{:,}".format(int(max(state_data['positive'].values))), color = 'r')
    plt.legend(loc='upper left')
    plt.title(state + ': cases and tests')
    plt.show()

    plt.title(state + ': cases and tests, log scale')
    plt.plot(dates, tested, label = 'tests')
    plt.plot(dates, positive, label = 'cases', color = 'r')
    plt.yscale('log')
    plt.legend(loc='upper left')
    plt.show()

    plt.title(state + ': deaths and cumulative hospitilizations')
    plt.bar(dates, hospitalized, label = 'hospitalizations: ' + str(max(hospitalized)))
    plt.bar(dates, death, label = 'deaths: ' + str(max(death)), color = 'r')
    plt.legend(loc='upper left')
    plt.show()

    plt.title(state + ': deaths and cumulative hospitilizations, log scale')
    plt.plot(dates, hospitalized, label = 'hospitalizations')
    plt.plot(dates, death, label = 'deaths', color = 'r')
    plt.yscale('log')
    plt.legend(loc='upper left')
    plt.show()

    plt.title('Daily deaths')
    plt.bar(dates, reversed_death[::-1], label = 'deaths')
    plt.plot(dates, rolling_deaths[::-1], color = 'r', linewidth = '2', label = '7 day rolling average')
    plt.legend(loc = 'upper left')
    plt.show()

    import numpy as np
    cases = np.array(new_state_cases, dtype=np.float32)
    rolling_cases = pd.rolling_mean(reversed_, 7, min_periods=1) 
    
    plt.title('Daily cases')
    plt.bar(dates, reversed_[::-1], label = 'cases')
    plt.plot(dates, rolling_cases[::-1], color = 'r', linewidth = '2', label = '7 day rolling average')
    plt.legend(loc = 'upper left')
    plt.show()
    
    import math
    if math.isnan(state_data.iloc[0]['hospitalizedCurrently']):
        print ''
    else:
        plt.plot(dates, state_data['hospitalizedCurrently'].values, label = 'hosp currently')
    plt.plot(dates, state_data['hospitalized'], label = 'hosp total')
    plt.legend(loc='upper left')
    plt.show()

def shorten_state(state):
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

    return us_state_abbrev[state]