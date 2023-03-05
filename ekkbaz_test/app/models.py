from django.db import models

data = [
    {"Google": 500},
    {"Yahoo": 2001},
    {"Netflix": 1948},
    {"Facebook": 108},
    {"WhatsApp": 63},
    {"Twitter": 3500},
    {"YouTube": 1040},
    {"Instagram": 20},
    {"Around Borders": 360.12}
]

# Create your models here.
class BusinessData:

    def getBusinesses(self):
        return [{"name": j, "distance": i[j]} for i in data for j in i.keys() if i[j] <= 2000]