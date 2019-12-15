import os
import sys

import requests

print(sys.executable)
print(sys.version)


def greetings(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://www.google.com")
print(r.status_code)
print("hello")
