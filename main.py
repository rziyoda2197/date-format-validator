from datetime import datetime

def sana_formatini_tekshir(sana):
    try:
        datetime.strptime(sana, '%Y-%m-%d')
        return True
    except ValueError:
        return False

sana = input("Sana kiriting: ")
if sana_formatini_tekshir(sana):
    print("Sana formati to'g'ri")
else:
    print("Sana formati noto'g'ri")
```

```python
from dateutil.parser import parse

def sana_formatini_tekshir(sana):
    try:
        parse(sana)
        return True
    except ValueError:
        return False

sana = input("Sana kiriting: ")
if sana_formatini_tekshir(sana):
    print("Sana formati to'g'ri")
else:
    print("Sana formati noto'g'ri")
