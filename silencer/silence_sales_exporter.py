#!/usr/bin/env python3

import requests

url = "http://prom1:9093/alertmanager/api/v2/silences"

import sys
_date = sys.argv[1] #2021-03-12

start = _date + "T03:00:00.000000" #7pm PST
end   = _date + "T15:00:00.000000" #7am PST

req = requests.post(url, json={
    "matchers": [
        {"name": "job", "value": "sales_exporter", "isRegex": False},
        ],
    "startsAt": start,
    "endsAt": end,
    "comment": "Auto Expire please",
    "createdBy": "karl.rink script",
    },
    )

req.raise_for_status()

silenceID = req.json()["silenceID"]
print(silenceID)

