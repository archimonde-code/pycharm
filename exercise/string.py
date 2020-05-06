import sys


print(sys.argv)

string = 'string'

reply = """
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""

values = {"name": "Docker", "age": 18}
print(reply % values)
