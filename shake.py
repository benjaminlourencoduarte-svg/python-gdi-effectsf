import win32gui
import win32con
import win32api
import time
import traceback
import ctypes

def main():
    
    try:
        ctypes.windll.user32.SetProcessDPIAware()
        print("process dpi wenabled")
    except Exception:
        print("ERROR:")
        traceback.print_exc()

    try:
        while True:
            try:
                hdc = win32gui.GetDC(0)
                x = win32api.GetSystemMetrics(0)  # screen width
                y = win32api.GetSystemMetrics(1)  # screen height

                # Attempt the blit operations
                win32gui.StretchBlt(hdc, -10, -10, x + 20, y + 20,
                                    hdc, 0, 0, x, y, win32con.SRCCOPY)

                win32gui.StretchBlt(hdc, 10, 10, x - 20, y - 20,
                                    hdc, 0, 0, x, y, win32con.SRCCOPY)

                win32gui.ReleaseDC(0, hdc)

            except Exception:
                print("Error during GDI call:")
                traceback.print_exc()

            # Wait 0.01 seconds
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\nExiting on Ctrl+C")
    except Exception:
        print("Unexpected error occurred:")
        traceback.print_exc()

if __name__ == "__main__":
    main()
