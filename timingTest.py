from astral.sun import sun
from astral import LocationInfo
from pytz import timezone
from datetime import timedelta
import time
import datetime


def get_solar_events(city):
    s = sun(city.observer, date=datetime.date.today(), tzinfo=city.timezone)
    dawn = s['dawn']
    sunrise = s['sunrise']
    noon = s['noon']
    sunset = s['sunset']
    dusk = s['dusk']
    start_time = dawn - timedelta(minutes=20)
    end_time = dusk + timedelta(minutes=20)

    return dawn, sunrise, noon, sunset, dusk, start_time, end_time

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


east_tz = timezone('US/Eastern')
west_tz = timezone('US/Pacific')
nyc = LocationInfo("New York", "USA", "US/Eastern", 40.730610, -73.935242)

now = datetime.datetime.now(east_tz)


dawn, sunrise, noon, sunset, dusk, start_time, end_time = get_solar_events(nyc)
write_solar_events_to_file(f"\n🟢 Starting: {now}\n\n", dawn, sunrise, noon, sunset, dusk, start_time, end_time)




while True:

    now = datetime.datetime.now(east_tz)
    now_object = datetime.datetime.now(east_tz).time()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    if (start_time <= now <= end_time):
        with open('timelapseLog.txt', 'a') as f:
            f.write(f"🌝 {timestamp}\n")

    else:
        with open('timelapseLog.txt', 'a') as f:
            f.write(f"🌚 {timestamp}\n")
    


    # Update the solar events for the next day around midnight each night
    # 
    if (datetime.time(0, 0) <= now_object <= datetime.time(0, 6)):

        dawn, sunrise, noon, sunset, dusk, start_time, end_time = get_solar_events(nyc)
        write_solar_events_to_file(f"\n🟣 Updating Solar Events for the Day\n🟢 Starting: {now}\n\n", dawn, sunrise, noon, sunset, dusk, start_time, end_time)



    time.sleep(300)
