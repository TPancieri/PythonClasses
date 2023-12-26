from datetime import datetime, timezone
import zoneinfo

# Timezone keys for creating the ZoneInfo objects.
zones = (
    'Europe/Paris',
    'Europe/London',
    'Asia/Hong_Kong',
    'Africa/Nairobi',
)

# Get the current time, in UTC
utc_now = datetime.now(tz=timezone.utc)

for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    required_time = utc_now.astimezone(tz).strftime('%H:%M:%S, %z - %Z')
    # The city is the last item, after splitting the zone at the /
    city = zone.split('/')[-1]
    print(f'The time in {city} is {required_time}')
