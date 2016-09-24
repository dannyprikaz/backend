import csv
from api.models import Location


with open("communitygardens.csv", 'r') as f:
    reader = csv.reader(f)
    next(f) #skips first line so we don't import headers
    for r in reader:
        loc = Location(name=r[1], category=r[2],address_1=r[3], city=r[4], state=r[5],zipcode=r[6], latitude=float(r[7]), longitude=float(r[8]))
        loc.save()