# Progress bar loading animation

The progress bar immitates a loading animation inside the terminal for the beginning of your project to start off seamlessly. 

You can delete the bar after it reaches 100% by importing the system library and adding a function to do so:
'''
import sys
def delete_last_line():
  sys.stdout.write('\x1b[1A')
'''

