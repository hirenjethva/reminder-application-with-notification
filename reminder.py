import winsound
from win10toast import ToastNotifier

def timer (reminder,seconds):
    notificator = ToastNotifier()
    notificator.show_toast("Reminder",f"""Alarm will go off in {seconds} seconds.""",duration=20)
    notificator.show_toast(f"Reminder",reminder,duration=20)

    #alarm
    frequency=2500
    duration=1000
    winsound.Beep(frequency,duration)

if __name__ == "__main__":
    words = input("What would your reminder of:")
    sec = int(input("Enter seconds:"))
    timer(words,sec)
