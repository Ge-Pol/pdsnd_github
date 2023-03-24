import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    cities_list = ['chicago', 'new york city', 'washington']
    months_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('\nWould you like to see the data for Chicago, New York City or Washington? Please enter the city of your choice:').lower()
        except KeyboardInterrupt:
            print('\nOops! That was no valid input. Try again!\n')
            continue
        if city in cities_list:
            break
        else:
            print('\nOops! That was no valid input. Try again!\n')


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('\nPlease enter one of the following months: January, February, March, April, May, June. If you would like to see results for all the months mentioned, enter all:').lower()
        except KeyboardInterrupt:
            print('\nOops! That was no valid input. Try again!\n')
            continue
        if month in months_list:
            break
        else:
            print('\nOops! That was no valid input. Try again!\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('\nPlease enter one of the following days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. If you would like to see results for all days of the week, enter all:').lower()
        except KeyboardInterrupt:
            print('\nOops! That was no valid input. Try again!\n')
            continue
        if day in days_list:
            break
        else:
            print('\nOops! That was no valid input. Try again!\n')



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 'all' to apply no month filter
        (str) day - name of the day of week to filter by, or 'all' to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
       # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Arg:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of week is:', popular_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
        Arg:
            df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('The most commonly used end station is:', popular_end)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Combination'] = df['Start Station'] + ' - ' + df['End Station']
    popular_combination = df['Start End Combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is:', popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
        Arg:
            df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time in seconds is:', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time in seconds is:', round(mean_travel_time, ndigits=1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
        Arg:
            df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print('The counts of user types are:', count_user_types)


    # TO DO: Display counts of gender
    try:
        count_gender = df['Gender'].value_counts()
        print('The counts of user gender are:', count_gender)

    except:
        print('No data exists on the gender of users in Washington.')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_year = df['Birth Year'].min()
        print('This is the earliest year of birth:', int(min_year))

        max_year = df['Birth Year'].max()
        print('This is the most recent year of birth:', int(max_year))

        mode_year = df['Birth Year'].mode()[0]
        print('This is the most common year of birth:', int(mode_year))

    except:
        print('No data exists on the birth year of users in Washington.')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Displays five rows of raw data upon user's request.

    Arg:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    start_index = 0
    #TO DO: get user input for request
    while True:
        try:
            show_more = input('\nWould you like to see five (more) rows of raw data? Please enter yes or no.').lower()
        except KeyboardInterrupt:
            print('\nOops! That was no valid input. Try again!\n')
            continue
        if show_more == 'no':
            break
        elif show_more == 'yes':
            pd.set_option('display.max_columns',200)
            print(df[start_index: start_index + 5])
            start_index += 5
            if start_index > len(df.index):
                print('\nYou have seen all rows of raw data.\n')
                break
        else:
            print('\nOops! That was no valid input. Try again!\n')

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Please enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
