import ctypes
import traceback

# Load libraries
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Make process DPI aware
user32.SetProcessDPIAware()

# Constants
SM_CXSCREEN = 0
SM_CYSCREEN = 1
PATINVERT = 0x005A0049
LIGHTRGB = 0x00FFFFFF  # White brush, you can change this

def main():
    try:
        while True:
            # Get device context for entire screen
            hdc = user32.GetDC(None)

            # Get screen dimensions
            w = user32.GetSystemMetrics(SM_CXSCREEN)
            h = user32.GetSystemMetrics(SM_CYSCREEN)

            # Create brush
            brush = gdi32.CreateSolidBrush(LIGHTRGB)

            # Select brush into DC
            gdi32.SelectObject(hdc, brush)

            # Invert the screen area
            gdi32.PatBlt(hdc, 0, 0, w, h, PATINVERT)

            # Clean up
            gdi32.DeleteObject(brush)
            user32.ReleaseDC(None, hdc)

    except Exception:
        print("An error occurred:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
