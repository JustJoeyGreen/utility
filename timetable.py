################################################################################
# Time Table Generator
# by Joey Green
################################################################################

from datetime import datetime
from random import shuffle
from prettytable import PrettyTable

################################################################################

work_activities = ['Thesis', 'Report 3', 'Cyber Presentation Slides', 'Test Neural Models on Different Variables', 'Loss Function']
leisure_activities = ['Nintendo Switch', 'Press Ups', 'Sit Ups']

work_time = 45 # minutes work per hour
work_end = 18 # 6pm end
lunch_hour = 13 # 1pm lunch

################################################################################
shuffle(work_activities)
shuffle(leisure_activities)
################################################################################

current_datetime = datetime.now()
# year, month, day, hour, minute, second, microsecond
current_time = '{}:{}'.format(current_datetime.hour, current_datetime.minute)
start_hour = current_datetime.hour + 1

print "*** Timetable for {}/{}/{} ***".format(current_datetime.day, current_datetime.month, current_datetime.year)
print "> Current Time: {}".format(current_time)
print ""
table = PrettyTable(['Start Time', 'End Time', 'Activity'])
table.add_row([current_time, '{}:00'.format(start_hour), 'Mentally Prepare Yourself'])

for hour_counter in range(start_hour, work_end):

    if hour_counter == lunch_hour:
        table.add_row(['{}:00'.format(hour_counter), '{}:00'.format(hour_counter+1), '+ LUNCH +'])
    else:
        table.add_row(['{}:00'.format(hour_counter), '{}:{}'.format(hour_counter, work_time), work_activities[hour_counter % len(work_activities)]])
        table.add_row(['{}:{}'.format(hour_counter, work_time), '{}:00'.format(hour_counter+1), leisure_activities[hour_counter % len(leisure_activities)]])

print table
