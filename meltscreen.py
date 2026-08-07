import ctypes as B,random as E,time
A=B.windll.user32
F=B.windll.gdi32
A.SetProcessDPIAware()
G,H=A.GetSystemMetrics(0),A.GetSystemMetrics(1)
C=A.GetDC(0)
while 1:D=E.randint(0,G);F.BitBlt(C,D,1,10,H,C,D,0,13369376);time.sleep(.01)
