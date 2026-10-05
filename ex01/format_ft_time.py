
import time as tm
from datetime import datetime

data = tm.localtime()
str_mouth = datetime.now().strftime("%b")
print(f'Second since January 1, 1970: {tm.time():,}' )
print(f'{str_mouth} {data.tm_mday} {data.tm_year}')