import platform
import psutil
import pyudev
from gi.repository import Gio

System=platform.uname().system
Dist=platform.uname().version
Arch=platform.uname().machine
print("Fetched Details ::")
print("\nSystem----------------")
print("System       : ",System)
print("Distribution : ",Dist)
#print("Architecture : ",Arch)

battery_status=psutil.sensors_battery().power_plugged
battery_percent=psutil.sensors_battery().percent
if(battery_status):
	battery_status="Plugged"
else:
	battery_status="Not Plugged"
battery_percent=battery_percent*100
battery_percent=int(battery_percent)
battery_percent=battery_percent/100.0
print("\nBATTERY---------------")
print("Battery Status     : ",battery_status)
print("Battery Percentage : ",battery_percent)

Ram=psutil.virtual_memory()
Total=Ram.total
Free=Ram.free
Available=Ram.available
Used=Ram.used
Percent=Ram.percent
print("\nRAM-----------------")
print("Total     : ",Total)
print("Free      : ",Free)
print("Available : ",Available)
print("Used      : ",Used)
print("Percent   : ",Percent)

print("\nDISK----------------")
vm = Gio.VolumeMonitor.get()
for v in vm.get_volumes():
	print (v.get_name())
