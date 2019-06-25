
import os
import psutil

print(psutil.sensors_battery())

print(psutil.disk_usage("/root"))

tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

print("Total ram = "+str(tot_m))
print("Used ram = "+str(used_m))
print("Free ram = "+str(free_m))

