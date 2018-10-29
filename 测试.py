# -*- coding:utf-8

import subprocess
ADSL_BASH='adsl-stop;adsl-start'
(status, output) = subprocess.getstatusoutput(ADSL_BASH)