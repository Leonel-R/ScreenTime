from datetime import datetime, timedelta 

file_in = input("Please enter desired text filename:")
date_in = input("Please enter starting date in dd.mm.yyyy format:")
start_date = datetime.strptime(date_in, "%d.%m.%Y")
timespan = int(input("How many days do you want to track?:"))
print("Please type in screen time (in minutes) for TV, computer, and mobile device each seperated by a space:")

with open(file_in, "w") as my_file:
    total_min = 0
    i = 0
    data = {}
    while i < timespan:
        delta_time = timedelta(days=i) + start_date
        i+=1
        info = input(f"Screen time {delta_time.strftime(('%d.%m.%Y'))}:")
        data[delta_time] = info.replace(" "," / ")
        parts = info.split()
        parts_int = [eval(x) for x in parts]
        total_min += sum(parts_int)
    print(f"Data has been stored in newly created file {file_in}")
    
    my_file.write(f"Time period: {start_date.strftime('%d.%m.%Y')} - {delta_time.strftime('%d.%m.%Y')}\n")
    my_file.write(f"Total screen time in minutes: {total_min}\n")
    my_file.write(f"Average minutes: {total_min/timespan:.2f}\n")
    my_file.write("Screen time log:\n")
    for key, value in data.items():
        my_file.write(f"{key.strftime('%d.%m.%Y')}: {value}\n")
    
