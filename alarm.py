# Getting started to my Alarm Project in Python. 
# import necessary modules. 
import time
from datetime import datetime
import winsound
# Setting alarm time here:
def set_alarm():
    alarm_list = []
    while True:
        alarm_time = int(input("Enter alarm time (HH:MM:SS) or done to finish: "))
        if alarm_time == "done":
            print("Thanks for using it...")
            exit()
        try:
            time.strptime(alarm_time,"%H:%M:%S")
            alarm_list.append(alarm_time)
            print(f"Alarm added for {alarm_time}")
        except Exception as e:
            print(e)
        return alarm_list
# Performing functionality to ring our alarms... 
def start_alarm(alarm_list):
    print("Monitoring Alarms")
    print(alarm_list)
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time in alarm_list:
            print(f"Alarm ringing for {current_time}!")
            winsound.Beep(1000,2000)
            break
        time.sleep(1)
        if not alarm_list:
            print("All alarms completed. Exiting")
            break
alarms = set_alarm()
start_alarm(alarms)
# Code Finalized.... 