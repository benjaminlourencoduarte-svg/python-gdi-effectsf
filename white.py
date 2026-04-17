import ctypes
import traceback
import time

# Load libraries
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Make process DPI aware
user32.SetProcessDPIAware()

# Constants
SM_CXSCREEN = 0
SM_CYSCREEN = 1
PATCOPY = 0x00F00021
WHITENESS = 0x00FF0062
WHITE = 0x00FFFFFF

def main():
    try:
        while True:
            # Get device context for entire screen
            hdc = user32.GetDC(0)

            # Screen dimensions
            w = user32.GetSystemMetrics(SM_CXSCREEN)
            h = user32.GetSystemMetrics(SM_CYSCREEN)

            # Create a white brush
            brush = gdi32.CreateSolidBrush(WHITE)
            gdi32.SelectObject(hdc, brush)

            # Paint white over the screen
            gdi32.PatBlt(hdc, 0, 0, w, h, PATCOPY)
            # Alternatively: gdi32.PatBlt(hdc, 0, 0, w, h, WHITENESS)

            # Clean up
            gdi32.DeleteObject(brush)
            user32.ReleaseDC(0, hdc)

            # Slow down so you can see the fade
            time.sleep(0.05)

    except Exception:
        print("An error occurred:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
