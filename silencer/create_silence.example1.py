#!/usr/bin/env python3

import requests
import socket
import datetime
import time

req = requests.post("http://prom1:9093/alertmanager/api/v2/silences", json={
    "matchers": [
        {"name": "job", "value": "myjob", "isRegex": False},
        {"name": "instance", "value": "{}:1234".format(socket.gethostname()), "isRegex": False},
        ],
    "startsAt": datetime.datetime.utcfromtimestamp(time.time()).isoformat(),
    "endsAt": datetime.datetime.utcfromtimestamp(time.time() + 4*3600).isoformat(),
    "comment": "Example on {}".format(socket.gethostname()),
    "createdBy": "karl.rink example script",
    },
    )

req.raise_for_status()

silenceID = req.json()["silenceID"]
print(silenceID)

