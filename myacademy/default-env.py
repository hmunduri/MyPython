#!/bin/python

import os
stage = (os.getenv("STAGE") or "develeopment" ).upper()
output = "we're running in %s" % stage

if stage.startswith("PROD"):
    output = "DANGER !!!! - " + output 

print(output)
