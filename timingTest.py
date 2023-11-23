from astral.sun import sun
from astral import LocationInfo
from pytz import timezone
from datetime import timedelta
import time
import datetime


east_tz = timezone('US/Eastern')
west_tz = timezone('US/Pacific')
city = LocationInfo("New York", "USA", "US/Eastern", 40.730610, -73.935242)

s = sun(city.observer, date=datetime.date.today(), tzinfo=city.timezone)
dawn = s['dawn']
sunrise = s['sunrise']
noon = s['noon']
sunset = s['sunset']
dusk = s['dusk']

print((
    f'Dawn:    {dawn}\n'
    f'Sunrise: {sunrise}\n'
    f'Noon:    {noon}\n'
    f'Sunset:  {sunset}\n'
    f'Dusk:    {dusk}\n'
))

now = datetime.datetime.now(east_tz)
print(f"starting: {now}")


start_time = dawn - timedelta(minutes=20)
end_time = dusk + timedelta(minutes=20)


with open('timelapseLog.txt', 'a') as f:
    f.write(f'\n☉ Dawn:    {dawn}\n')
    f.write(f'☉ Sunrise: {sunrise}\n')
    f.write(f'☉ Noon:    {noon}\n')
    f.write(f'☉ Sunset:  {sunset}\n')
    f.write(f'☉ Dusk:    {dusk}\n\n')
    f.write(f'  start:   {start_time}\n')
    f.write(f'  end:     {end_time}\n')
    f.write(f"\n🟢 starting: {now}\n\n")
    

while True:

    now = datetime.datetime.now(east_tz)
    now_object = datetime.datetime.now(east_tz).time()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    if (start_time <= now <= end_time):

        print(f"🌝 waking - {timestamp}")

        with open('timelapseLog.txt', 'a') as f:
            f.write(f"🌝 waking - {timestamp}\n")

    else:
        print(f"🌚 sleeping - {timestamp}")

        with open('timelapseLog.txt', 'a') as f:
            f.write(f"🌚 sleeping - {timestamp}\n")
        
    # Update the solar events for the next day around midnight each night
    # 
    if (datetime.time(0, 0) <= now_object <= datetime.time(0, 15)):
    # if (datetime.time(13, 40) <= now_object <= datetime.time(13, 50)):

        s = sun(city.observer, date=datetime.date.today(), tzinfo=city.timezone)
        dawn = s['dawn']
        sunrise = s['sunrise']
        noon = s['noon']
        sunset = s['sunset']
        dusk = s['dusk']

        start_time = dawn - timedelta(minutes=20)
        end_time = dusk + timedelta(minutes=20)

        print((
            f'Dawn:    {dawn}\n'
            f'Sunrise: {sunrise}\n'
            f'Noon:    {noon}\n'
            f'Sunset:  {sunset}\n'
            f'Dusk:    {dusk}\n\n'
            f'Start:   {start_time}\n'
            f'End:     {end_time}\n'
        ))

        with open('timelapseLog.txt', 'a') as f:
            f.write(f"\n🕛 Updating Solar Events for the Day\n")
            f.write(f'☉ Dawn:    {dawn}\n')
            f.write(f'☉ Sunrise: {sunrise}\n')
            f.write(f'☉ Noon:    {noon}\n')
            f.write(f'☉ Sunset:  {sunset}\n')
            f.write(f'☉ Dusk:    {dusk}\n\n')
            f.write(f'  start:   {start_time}\n')
            f.write(f'  end:     {end_time}\n')
            f.write(f"\n🟣 REstarting: {now}\n\n")

    time.sleep(300)
