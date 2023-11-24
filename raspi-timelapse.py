import zoneinfo
from astral.sun import sun
from astral import LocationInfo
from pytz import timezone
from datetime import timedelta
# from picamera2 import Picamera2
# from libcamera import controls
import time
import datetime

picam2 = Picamera2()
picam2.resolution = (4608, 2592)


est_tz = timezone('US/Eastern')
city = LocationInfo("New York", "USA", "US/Eastern", 40.730610, -73.935242)

s = sun(city.observer, date=datetime.date.today(), tzinfo=city.timezone)
dawn = s['dawn']
sunrise = s['sunrise']
sunset = s['sunset']
dusk = s['dusk']

print((
    f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {s["sunrise"]}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'
))


start_time = dawn - timedelta(minutes=10)
end_time = dusk + timedelta(minutes=10)



# Run the loop until the current time is past the end time
while True:
    if (start_time <= now <= end_time):
        print("\nTime to stop!\n")
        break

    break

    # Get the current time as an aware datetime object
    now = datetime.datetime.now(est_tz)

    # Check the time immediately before each capture
    if not (start_time <= now <= end_time):
        print("\nTime to stop!\n")
        break
    
    picam2.start(show_preview=True)
    picam2.create_still_configuration(main={"size": (4608, 2592)})
    picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})


    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    directory = "/home/ray/Nostromo/projects/181202_timelapse/2023.11.13"
    filename = f"{directory}/{timestamp}.jpg"

    picam2.start_and_capture_files(filename)
    picam2.stop()

    time.sleep(10)
