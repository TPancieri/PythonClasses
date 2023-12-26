# paris, london, hong kong, nairobi
from datetime import datetime, timezone
import zoneinfo

utc_now = datetime.now(timezone.utc)

paris_tz = zoneinfo.ZoneInfo('Europe/Paris')
paris_now = utc_now.astimezone(paris_tz)
print(paris_now.strftime('%H:%M:%S'), paris_now.tzname())

london_tz = zoneinfo.ZoneInfo('Europe/London')
london_now = utc_now.astimezone(london_tz)
print(london_now.strftime('%H:%M:%S'), london_now.tzname())

hk_tz = zoneinfo.ZoneInfo("Asia/Hong_Kong")
hk_now = utc_now.astimezone(hk_tz)
print(hk_now.strftime('%H:%M:%S'), hk_now.tzname())

nairobi_tz = zoneinfo.ZoneInfo("Africa/Nairobi")
nairobi_now = utc_now.astimezone(nairobi_tz)
print(nairobi_now.strftime('%H:%M:%S'), nairobi_now.tzname())
