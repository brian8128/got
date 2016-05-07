from __future__ import absolute_import, division, print_function

import os

# This script detects the stage dev/prod and sets the appropriate environment variables.

stage = os.environ["STAGE"]
stage = stage.lower()

print("Running in stage: {}".format(stage))

if stage == 'dev':
    from .dev import *
elif stage == 'prod':
    from .prod import *

else:
    print("Unknown stage: {}".format(stage))
