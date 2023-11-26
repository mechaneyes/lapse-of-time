from astral.sun import sun
from astral import LocationInfo
from pytz import timezone
from datetime import timedelta
import time
import datetime

# get solar events for the day
# 
def get_solar_events(city, date):
    s = sun(city.observer, date=date, tzinfo=city.timezone)
    dawn = s['dawn']
    sunrise = s['sunrise']
    noon = s['noon']
    sunset = s['sunset']
    dusk = s['dusk']
    start_time = dawn - timedelta(minutes=20)
    end_time = dusk + timedelta(minutes=20)

    return dawn, sunrise, noon, sunset, dusk, start_time, end_time

# print solar events to console
# 
def print_solar_events(dawn, sunrise, noon, sunset, dusk, start_time, end_time):
    print((
        f'Dawn:    {dawn}\n'
        f'Sunrise: {sunrise}\n'
        f'Noon:    {noon}\n'
        f'Sunset:  {sunset}\n'
        f'Dusk:    {dusk}\n\n'
        f'Start:   {start_time}\n'
        f'End:     {end_time}\n'
    ))

# log solar events to file
# 
def write_solar_events_to_file(message, dawn, sunrise, noon, sunset, dusk, start_time, end_time):
    with open('timeLapseLog.txt', 'a') as file:
        file.write(message)
        file.write(f'☉ Dawn:    {dawn}\n')
        file.write(f'☉ Sunrise: {sunrise}\n')
        file.write(f'☉ Noon:    {noon}\n')
        file.write(f'☉ Sunset:  {sunset}\n')
        file.write(f'☉ Dusk:    {dusk}\n\n')
        file.write(f'  Start:   {start_time}\n')
        file.write(f'  End:     {end_time}\n\n')

# log current time passing appropriate message
# 
def write_time_to_file(message):
    with open('timeLapseLog.txt', 'a') as file:
        file.write(message)



east_tz = timezone('US/Eastern')
west_tz = timezone('US/Pacific')
nyc = LocationInfo("New York", "USA", "US/Eastern", 40.730610, -73.935242)


now = datetime.datetime.now(east_tz)

dawn, sunrise, noon, sunset, dusk, start_time, end_time = get_solar_events(nyc, now.date())
write_solar_events_to_file(f"\n🟢 Starting: {now}\n\n", dawn, sunrise, noon, sunset, dusk, start_time, end_time)




while True:

    now = datetime.datetime.now(east_tz)
    time_now = datetime.datetime.now(east_tz).time()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    if (start_time <= now <= end_time):
        write_time_to_file(f"🌝 {timestamp}\n")

    else:
        write_time_to_file(f"🌚 {timestamp}\n")
    


    # Update the solar events for the next day around midnight each night
    # 
    if (datetime.time(1, 0) <= time_now <= datetime.time(1, 6)):

        dawn, sunrise, noon, sunset, dusk, start_time, end_time = get_solar_events(nyc, now.date())
        write_solar_events_to_file(f"\n🟣 Updating Solar Events for the Day\n🟢 Starting: {now}\n\n", dawn, sunrise, noon, sunset, dusk, start_time, end_time)



    time.sleep(300)
