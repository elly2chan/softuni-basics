exam_start_hour = int(input())
exam_start_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

arrival_in_minutes = arrival_hour * 60 + arrival_minute
exam_in_minutes = exam_start_hour * 60 + exam_start_minute

hours = 0
minutes = 0

if arrival_in_minutes > exam_in_minutes:
    status = "Late"
    print(status)
    if (arrival_in_minutes - exam_in_minutes) < 60:
        minutes = arrival_in_minutes - exam_in_minutes
        print(f'{minutes} minutes after the start')
    elif arrival_in_minutes - exam_in_minutes > 60:
        hours = int((arrival_in_minutes - exam_in_minutes) / 60)
        minutes = arrival_minute - exam_start_minute
        if minutes < 10:
            print(f'{hours}:0{minutes} hours after the start')
        else:
            print(f'{hours}:{minutes} hours after the start')
    elif (arrival_in_minutes - exam_in_minutes) == 60:
        hours = 1
        if minutes < 10:
            print(f'{hours}:0{minutes} hours after the start')
        else:
            print(f'{hours}:{minutes} hours after the start')

elif arrival_in_minutes <= exam_in_minutes:
    if exam_in_minutes == arrival_in_minutes:
        status = "On time"
        print(status)
    elif (exam_in_minutes - arrival_in_minutes) <= 30:
        status = "On time"
        print(status)
        minutes = exam_in_minutes - arrival_in_minutes
        print(f'{minutes} minutes before the start')
    else:
        status = "Early"
        print(status)
        if 30 < (exam_in_minutes - arrival_in_minutes) < 60:
            minutes = exam_in_minutes - arrival_in_minutes
            print(f'{minutes} minutes before the start')
        elif exam_in_minutes - arrival_in_minutes > 60:
            hours = int((exam_in_minutes - arrival_in_minutes ) / 60)
            minutes = (exam_in_minutes - arrival_in_minutes) - (hours * 60)
            if minutes < 10:
                print(f'{hours}:0{minutes} hours before the start')
            else:
                print(f'{hours}:{minutes} hours before the start')
        elif (exam_in_minutes - arrival_in_minutes) == 60:
            hours = 1
            print(f'{hours}:00 hours before the start')