#!/usr/bin/env python3

import requests
import sys

silenceID = sys.argv[1]

req = requests.delete("http://prom1:9093/alertmanager/api/v2/silence/{}".format(silenceID))

req.raise_for_status()

print(req)

