Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /k ""cd /d C:\Users\fahee\Desktop\Bismi\BillApp_new && envBismi\Scripts\activate.bat && python manage.py runserver 8000""", 0, False
