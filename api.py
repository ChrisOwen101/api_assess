import json


def load_counties():
    f = open("countries.json")
    return json.load(f)


###
#
# Create an API that
#
# 1. Returns a list of all of the counties (e.g. /countries)
# 2. Filters a list of countries based on a URL query parameter (/countries?search=united)
# 3. Gets a country based on it's code (e.g. /countries/GB)
#
# We'll continue to add tasks to this as time allows
