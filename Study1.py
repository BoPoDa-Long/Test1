from datetime import(
    datetime as dt,
    timezone as tz,
    timedelta as td
    )
open_time = dt.now(tz.utc)
fd = open_time.tzname()
print(fd)
