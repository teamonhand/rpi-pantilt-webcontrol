import subprocess
import cmd
import time

pan=4      # customize servo number
tilt=3     # customize your servo number
cw=-1      # clockwise rotation step
acw=1      # anti-clockwise rotation step
location=50 # starting point
pause=0.2   # time delay in msecs

# ------------------------------------------------------------
# Drives the given servo in the given direction and range
# Remembers the current location
# Inputs: 	direction
#		servo
#		beg
#		end
#
# Returns: current location
# ------------------------------------------------------------
def motion(direction, servo, beg, end):
	# adjust the end count to account for index 0 to n-1
	if (direction == acw):
		end = end+1
	elif (direction == cw):
		end = end-1

	for i in range(beg,end,direction):
		# -------------------------------------------------
		# syntax of the command is 
		# echo [servo-number]=[movement]%>/dev/servoblaster 
		# where servo-number = 3 for tilt, 4 for pan
		# 	movement = 0 to 100 for a 180 deg rotation
		# -------------------------------------------------
		buf="echo %s=%s%%>/dev/servoblaster" %(servo, i)
		print '\n'
		print buf
		time.sleep(pause)
		subprocess.call([buf], shell=True)
	return i

#count = input("enter count?")
count=1
type(count)

while True:
	location=motion(cw, pan, 50,10)
	location=motion(acw, pan, location,90)
	location=motion(cw, pan, location,50)

	location=motion(cw, tilt, location,10)
	location=motion(acw, tilt, location,90)
	location=motion(cw, tilt, location,50)

	count -= 1
	if count <= 0:
		break
