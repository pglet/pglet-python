import json
import os, sys, inspect
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pglet

with pglet.page(web=False, permissions="*") as page:
    print(page.name, page.url)
    time.sleep(10)
    page.clean()
    print("can_access:", page.can_access("test_user"))
