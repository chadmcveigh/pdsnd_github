import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
citys = ('chicago', 'new york', 'washington')
months = ('january', 'february', 'march', 'april', 'may', 'june')
weekdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
    city = get_choice('Would you like to see data for Chicago, New York, or Washington?', citys, True)
    month = get_choice('Which month would you like to filter by? (Jauary, February, March, April, May, or June? Type no for no month filter.', months, False)
    day = get_choice('Which day would you like to filter by? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? Type no for no day filter.', weekdays, False)

    print('-'*40)
    return city, month, day

def get_choice(question, bucket, first):
    """
    Asks user for what filters they would like.
    
    Returns:
        (str) choice - users decision on which filter to execute

    """
    while True:
        choice = input(question)
        choice = choice.strip().lower()
        if ((choice == 'no') and (first == False)):
            choice = 'all'
            break
        elif choice not in bucket:
            print("Invalid selection, please try again")
            continue
        else:
            break
    return choice

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    if(city == 'new york'):
        city = 'new york city'
    
    #Reading in csv file to dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    
    if day != 'all':
        df = df[df['Weekday'] == day.title()]

    return df


def time_stats(df, day, month, city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    if day == 'all' and month == 'all':
        print('Filter: ' + city )
    elif day == 'all' and month != 'all':
        print('Filter: ' + month + ', ' + city)
    elif day != 'all' and month == 'all':
        print('Filter: ' + day + ', ' + city)
    else:
        print('Filter: ' + day + ', ' + month + ', ' + city)

    # display the most common month
    if month == 'all':
        com_month = df['Month'].mode()[0]
        print('The month with the most travel is: ' + str(months[com_month - 1]) + '.')

    # display the most common day of week
    if day == 'all':
        com_day = df['Weekday'].mode()[0]
        print('The most common day is: ' + str(com_day) + '.')

    # display the most common start hour
    com_hour = df['Start Hour'].mode()[0]
    print('The most common hour is: ' + str(com_hour) + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, day, month, city):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    if day == 'all' and month == 'all':
        print('Filter: ' + city )
    elif day == 'all' and month != 'all':
        print('Filter: ' + month + ', ' + city)
    elif day != 'all' and month == 'all':
        print('Filter: ' + day + ', ' + city)
    else:
        print('Filter: ' + day + ', ' + month + ', ' + city)
    # display most commonly used start station
    com_start_station = df['Start Station'].mode()[0]
    print("The most common start station is: " + str(com_start_station))

    # display most commonly used end station
    com_end_station = df['End Station'].mode()[0]
    print("The most common end station is: " + str(com_end_station))

    # display most frequent combination of start station and end station trip
    df['Start/End Station Combination'] = (df['Start Station'] + ' - ' + df['End Station'])
    com_start_end = df['Start/End Station Combination'].mode()[0]
    print("The most common start-end startion is: " + str(com_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, day, month, city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    if day == 'all' and month == 'all':
        print('Filter: ' + city )
    elif day == 'all' and month != 'all':
        print('Filter: ' + month + ', ' + city)
    elif day != 'all' and month == 'all':
        print('Filter: ' + day + ', ' + city)
    else:
        print('Filter: ' + day + ', ' + month + ', ' + city)
    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel))

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, day, month, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    if day == 'all' and month == 'all':
        print('Filter: ' + city )
    elif day == 'all' and month != 'all':
        print('Filter: ' + month + ', ' + city)
    elif day != 'all' and month == 'all':
        print('Filter: ' + day + ', ' + city)
    else:
        print('Filter: ' + day + ', ' + month + ', ' + city)
    # Display counts of user types
    user_type_count = df['User Type'].value_counts().to_string()
    print('User types:')
    print(user_type_count)

    # Display counts of gender
    try:
        gender_count = df['Gender'].value_counts().to_string()
        print('Gender Count:')
        print(gender_count)
    except KeyError:
        print("There is no gender data for this filter")
        
    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = str(int(df['Birth Year'].min()))
        recent_birth = str(int(df['Birth Year'].max()))
        common_birth = str(int(df['Birth Year'].mode()[0]))
        
        print('The earliest birth year is: ' + earliest_birth)
        print('The most recent birth year is: ' + recent_birth)
        print('The most common birth year is: ' + common_birth)
    except:
        print('There is no data for birth year in this filter')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    print('Raw Data:')
    index = 0
    while True:
        #loop to run 5 lines of raw data
        for x in range (0, 5):
            print(df.iloc[index:index + 5].to_string())
            print('\n')
            index += 5
            
            raw_data_choice = input("Would you like to see more raw Data?(Y/N)")
            if raw_data_choice.lower() == 'y':
                continue
            else:
                print("You chose not to see more raw data")
                break
        break

def main():
    while True:
        #Loading data in dataframe
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        #Running function to show all stats
        time_stats(df, day, month, city)
        station_stats(df, day, month, city)
        trip_duration_stats(df, day, month, city)
        user_stats(df, day, month, city)
        
        #Prompting user if they would like to see Raw Data
        see_raw_data = input('Would you like to see raw data?(Y/N)')
        if see_raw_data.lower() == 'y':
            raw_data(df)
        
        #Prompting user to restart program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        else:
            continue


if __name__ == "__main__":
	main()
