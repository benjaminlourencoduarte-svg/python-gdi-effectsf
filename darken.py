import ctypes
import traceback
import random
import math
import time

# Load libraries
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Make process DPI aware
user32.SetProcessDPIAware()

# Constants
SM_CXSCREEN = 0
SM_CYSCREEN = 1
SRCAND = 0x008800C6

def main():
    try:
        while True:
            # Get device context for entire screen
            hdc = user32.GetDC(0)

            # Screen metrics
            x = SM_CXSCREEN
            y = SM_CYSCREEN
            w = user32.GetSystemMetrics(0)
            h = user32.GetSystemMetrics(1)

            # Random offsets
            dx = random.randint(0, 9)
            dy = random.randint(0, 9)
            sx = int(random.randint(0, 9) * math.tan(x))
            sy = random.randint(0, 9)

            # BitBlt operation
            gdi32.BitBlt(hdc, dx, dy, w, h, hdc, sx, sy, SRCAND)

            # Sleep for 10 ms
            time.sleep(0.01)

            # Release DC
            user32.ReleaseDC(0, hdc)

    except Exception:
        print("An error occurred:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
