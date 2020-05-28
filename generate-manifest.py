from parse import parse
import csv
from datetime import datetime, timedelta

input = """HV Disc 1d
•	1:48:36 – 1:50:48 = Max playing with Jacob 1999
•	1:50:48 – 1:54:02 = Mimi sleeps in the guest room
•	1:54:03 – 1:57:15 = Jacob’s 1st Birthday
•	1:57:16 – 2:00:30 = Baby Paul laughing"""

def seconds_helper(time):
    try:
        t = datetime.strptime(time, "%H:%M:%S")
    except ValueError:
        t = datetime.strptime(time, "%M:%S")
    return(timedelta(hours=t.hour, minutes=t.minute, seconds=t.second).total_seconds())


disks = input.split("\n\n")

for disk in disks:
    filename = disk.split('\n')[0]
    videos = disk.split('\n')[1:]
    with open(filename + '.csv', 'w') as csvfile:
        csvfile.seek(0)
        writer = csv.writer(csvfile)
        writer.writerow(['start_time', 'length', 'rename_to'])
        for video in videos:
            start_time, end_time, title = parse("{} – {} = {}", video[2:])
            start_time = int(seconds_helper(start_time))
            length = int(seconds_helper(end_time) - start_time)
            writer.writerow([start_time, length, 'clips/'+title.strip()])
        csvfile.truncate()