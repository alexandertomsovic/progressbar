# Progress Bar Loading Animation

### The progress bar immitates a loading animation inside the terminal which allows your python project to start seamlessly!

You can delete the bar after it reaches 100% by importing the system library and creating a function to do so like you see below.

```
import sys

def delete_last_line():
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
```

You can also view the working project in your browser by visiting my REPLIT below!               

https://replit.com/@AlexTomsovic/Progress-Bar#main.py
