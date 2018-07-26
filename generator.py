#!/usr/bin/env python3
import uuid
import random
import time
import collections
import json


logdict = collections.OrderedDict()
oplist = ['Write', 'Read', 'Allocate', 'Parse', 'Send']
hostlist = ['Node_1', 'Node_2', 'Node_3']
statuslist = ['Running', 'Down', 'Killed']


with open('generator.log', 'a') as logf:
    while True:
        logdict = {
            'Time': time.asctime(time.localtime(time.time())),
            'SessionID': str(uuid.uuid4()),
            'Operation': random.choice(oplist),
            'Host': random.choice(hostlist),
            'Status': random.choice(statuslist),
        }
        jsdict = json.dumps(logdict)
        logf.write(jsdict+'\n')
        time.sleep(0.1)
