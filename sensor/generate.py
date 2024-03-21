import random
from datetime import datetime


def generate_record():
    current_datetime = datetime.now().replace(microsecond=0)
    date = current_datetime.isoformat()
    deaths = random.randint(1,99)
    births = random.randint(1,99)
    record = {'time':date,
              'deaths':deaths,
              'births':births}
    return record
    