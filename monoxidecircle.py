import win32gui
import win32con
import win32api
import time

def reflect2d(x, y, w, h):
    def function(v, maxv):
        v_abs = abs(v)
        if (v_abs // maxv) % 2:
            return maxv - (v_abs % maxv)
        else:
            return v_abs % maxv
    x = function(x, w - 1)
    y = function(y, h - 1)
    return x, y

def post_gdi_shader3(t, w, h, rc_bounds, hdc_dst, n_shader_three_seed=0):
    # No BitBlt here — we don’t overwrite the background

    t += n_shader_three_seed
    x = t * 16
    y = t * 16

    # Aurora colors for three rings
    aurora_colors = [
        win32api.RGB(0, 255, 255),   # cyan
        win32api.RGB(0, 255, 128),   # greenish
        win32api.RGB(128, 0, 255)    # purple
    ]

    # Draw red ball + 3 aurora rings
    for idx, i in enumerate([64, 48, 32]):
        hbr_ball = win32gui.CreateSolidBrush(win32api.RGB(255, 0, 0))  # red fill
        hpen_ball = win32gui.CreatePen(win32con.PS_SOLID, 2, aurora_colors[idx])

        win32gui.SelectObject(hdc_dst, hbr_ball)
        win32gui.SelectObject(hdc_dst, hpen_ball)

        x, y = reflect2d(x, y, w, h)

        win32gui.Ellipse(hdc_dst,
                         x + rc_bounds[0] - i,
                         y + rc_bounds[1] - i,
                         x + rc_bounds[0] + i,
                         y + rc_bounds[1] + i)

        win32gui.DeleteObject(hbr_ball)
        win32gui.DeleteObject(hpen_ball)

def main():
    hdc_dst = win32gui.GetDC(0)  # desktop DC
    w = win32api.GetSystemMetrics(0)
    h = win32api.GetSystemMetrics(1)
    rc_bounds = (0, 0, w, h)

    t = 0
    try:
        while True:
            post_gdi_shader3(t, w, h, rc_bounds, hdc_dst)
            t += 1
            time.sleep(0.05)
    except KeyboardInterrupt:
        win32gui.ReleaseDC(0, hdc_dst)

if __name__ == "__main__":
    main()
