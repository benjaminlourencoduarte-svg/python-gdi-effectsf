import win32gui
import win32ui
import win32con
import win32api
import time
import traceback
import ctypes

def scroll_screen_left():
    try:
        # Make the process DPI aware so coordinates are accurate
        ctypes.windll.user32.SetProcessDPIAware()

        hdesktop = win32gui.GetDesktopWindow()
        hdc = win32gui.GetWindowDC(hdesktop)
        srcdc = win32ui.CreateDCFromHandle(hdc)
        memdc = srcdc.CreateCompatibleDC()

        width = win32api.GetSystemMetrics(0)
        height = win32api.GetSystemMetrics(1)

        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, width, height)
        memdc.SelectObject(bmp)

        shift = 70   # pixels per frame
        delay = 0.00  # 1ms pause

        while True:
            # Copy screen into memory
            memdc.BitBlt((0, 0), (width, height), srcdc, (0, 0), win32con.SRCCOPY)

            # Shift everything left
            srcdc.BitBlt((0, 0), (width - shift, height), memdc, (shift, 0), win32con.SRCCOPY)

            # Wrap right edge back to left
            srcdc.BitBlt((width - shift, 0), (shift, height), memdc, (0, 0), win32con.SRCCOPY)

            time.sleep(delay)

    except Exception:
        print("An error occurred:")
        traceback.print_exc()
    finally:
        try:
            srcdc.DeleteDC()
            memdc.DeleteDC()
            win32gui.ReleaseDC(hdesktop, hdc)
            bmp.DeleteObject()
        except Exception:
            traceback.print_exc()

if __name__ == "__main__":
    scroll_screen_left()
