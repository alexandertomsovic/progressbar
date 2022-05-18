# PROGRESS BAR by Alex Tomsovic
# linktr.ee/alextomsovic

# Libraries 
import math
from colorama import Fore

# Progress bar function
def progressbar(progress, total):
  percentage = 50 * (progress / float(total))
  bar = Fore.LIGHTGREEN_EX + '█' * int(percentage) + Fore.WHITE + '-' * (50 - int(percentage))
  print(f"\r |{bar}| {percentage * 2:.2f}%", end = "\r")

# Getting the list to iterate length
nums = [x * 2 for x in range(2000, 3000)]
results = []

# for loop to enumerate / increase 
progressbar(0, len(nums))
for i, x in enumerate(nums):
  results.append(math.factorial(x))
  progressbar(i + 1, len(nums))
