import datetime
from plyer import notification


#Calendar Set
notification_message="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eleifend felis vitae ipsum eleifend eleifend porttitor vapien tincidunt dignis"
notification_title="Lorem Ipsum"

alarm_set_day=datetime.datetime.now().day
alarm_set_hour=datetime.datetime.now().hour
alarm_set_min=datetime.datetime.now().minute

i=1
while i==1:
    if(alarm_set_day== (datetime.datetime.now().day)  and alarm_set_hour == datetime.datetime.now().hour and alarm_set_min== datetime.datetime.now().minute):
        #playsound()
        notification.notify(
            title = notification_title,
            message=notification_message,
            timeout=10)
    i=i+1