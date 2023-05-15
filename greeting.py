import time

time_now=time.strftime('%H:%M:%S')
# print(time_now)
time_hour=time.strftime('%H')
time_min=time.strftime('%M')
time_sec=time.strftime('%S')

if int(time_hour)>21:
    print("\n** GOOD NIGHT SIR ** \n  Sleep Well.")
    
elif int(time_hour)>17:
    print("\n** GOOD EVENING SIR ** \n  I hope you are having a great evening.")
    
elif int(time_hour)>12:
    print("\n** GOOD AFTERNOON SIR ** \n  I trust you are enjoying this lovely afternoon.")
    
else:
    print("\n** GOOD MORNING SIR ** \n  Have a great day ahead.")
    