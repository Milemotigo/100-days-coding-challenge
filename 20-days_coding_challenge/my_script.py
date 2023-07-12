import colorama
from colorama import Fore, Style

# Define the available brightness levels
BRIGHTNESS = [Style.NORMAL, Style.BRIGHT]

# Loop through each foreground color
for fore in Fore:
    # Loop through each brightness level
    for brightness in BRIGHTNESS:
        # Set the color and brightness
        color = f"{fore}{brightness}"

        # Print the colored text
        print(color + "Hello world!" + Style.RESET_ALL)
