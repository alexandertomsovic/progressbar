# Progress bar loading animation

### The progress bar immitates a loading animation inside the terminal for the beginning of your project to start off seamlessly!

You can delete the bar after it reaches 100% by importing the system library and creating a function to do so like you see below.

```
import sys

def delete_last_line():
  sys.stdout.write('\x1b[1A')
  sys.stdout.write('\x1b[2K')
```
