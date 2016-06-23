# rpi-pantilt-webcontrol
Pan-Tilt web interface control for RPI

Purpose: To control pan-tilt motion from a web browser using micro servo motors and servodriver software

Requirements:
Hardware:
--------
- Any PI model (I used RPI-3)
- Mini Pan-Tilt assembly (https://www.adafruit.com/product/1967)
- 2 x TowerPro SG92R micro-servos (https://www.adafruit.com/product/169)
- Separate 5V DC supply 2A or more (https://www.adafruit.com/category/44)
- Breadboard
- 4 male to female jumper wires

Setup:
-----

Connect the wires on the servos as follows:  
Brown = Black = Ground  
Orange = Red = Positive (5V)  
Yellow = White = Signal (GPIO pins)  

Refer to this table for the GPIO connections  

|Servo number    |GPIO number   |Pin in P1 header|  
|----------------|--------------|----------------|
|          0     |         4    |         P1-7   |
|          1     |        17    |         P1-11  |
|          2     |        18    |         P1-12  |
|          3     |        27    |         P1-13  |
|          4     |        22    |         P1-15  |
|          5     |        23    |         P1-16  |
|          6     |        24    |         P1-18  |
|          7     |        25    |         P1-22  |


My software uses servo numbers 3,4 for tilt and pan respectively, but you can pick any one from the table and modify the software accordingly.  

Optional:
--------
- Rpi Camera board v2 with dedicated CSi interface

Descripton of the script files: 

pypantilt.py -   
rotates the pan motor from the middle position (50%) to the left, to the right and back to the rest position  (50%)  
rotates the tilt motor from the middle position (50%) to the top, to the bottom and back to the rest position (50%)  

pt.sh -   
positions the appropriate motor (pan or tilt) to any location from 0% to 100% (180 degree rotation)  

pantilt.cgi -  
executes the script pypantilt.py  

slider.html - main web page
installs pan and tilt sliders to control 180deg motion  
runs a sanity check of the pan and tilt servos   
displays a window for viewing the camera (needs motion software to be installed)  

Assumptions and modification to the script files:  
------------------------------------------------
Configured for local/LAN access only.
The file slider.html has been hard-coded to connect to a RPI with an IP=192.168.10.107    
You will need to modify it accordingly.  
The files pantilt.cgi, pt.sh and pypantilt.py are set up to use servo numbers 3,4  


Software for the rpi:
--------------------
Install the following prerequsite software: 
```bash
$ sudo apt-get install apache2 apache2-utils php5 libapache2-mod-php5   
```
Verify that apache is up and running as follows:  
```bash
$ ps -ef|grep apache2|grep -v grep  
www-data  4209 16856  0 Jun22 ?        00:00:00 /usr/sbin/apache2 -k start  
www-data 10604 16856  0 Jun22 ?        00:00:00 /usr/sbin/apache2 -k start  
www-data 10605 16856  0 Jun22 ?        00:00:00 /usr/sbin/apache2 -k start  
www-data 10606 16856  0 Jun22 ?        00:00:00 /usr/sbin/apache2 -k start  
www-data 10607 16856  0 Jun22 ?        00:00:00 /usr/sbin/apache2 -k start  
www-data 10608 16856  0 Jun22 ?        00:00:00 /usr/sbin/apache2 -k start  
root     16856     1  0 Jun18 ?        00:00:24 /usr/sbin/apache2 -k start  
```
 
Install the servoblaster driver into a suitable folder as follows:  
```bash
$ git clone https://github.com/richardghirst/PiBits.git
```

Build and install the userspace driver as follows:  
```bash
$ cd PiBits/ServoBlaster/user/  
$ make  
$ sudo make install
```

Verify that the userspace servo daemon is now up and running as follows:  
```bash
$ ps -ef|grep servod|grep -v grep  
root      9161     1  0 Jun22 ?        00:00:00 /usr/local/sbin/servod --idle-timeout=2000
```

Modify /etc/apache2/apache2.conf to include the following lines  
```apache
<Directory "/var/www/html/cgi-bin/">  
    Options +ExecCGI  
    AddHandler cgi-script .cgi .pl .sh  
</Directory>  
```

Restart apache to activate the cgi scripts in the folder cgi-bin as follows:  
```bash
$ sudo service apache2 restart  
```

Copy the support files pantilt.cgi  pt.sh  pypantilt.py into /usr/lib/cgi-bin  
To keep things in one place, make a separate directory under /var/www/html/pantilt
and copy slider.html into it

Optional:
========
Install motion as follows:  
```bash
$ sudo apt-get install motion  
```
Edit the following parameters in /etc/motion/motion.conf accordingly and consult the relevant documentation:  
```bash
daemon yes  
logfile /tmp/motion.log  
target_dir /tmp/motion  --> this must be writeable  
stream_port 8081  
stream_localhost off ---> allows access from the internet  
```

Testing it all out:
------------------
open a browser and navigate to the web page, slider.html
In my case, I use http://192.168.10.107/pantilt/slider.html

See a screenshot here:
![Image](../img/screenshot.png?raw=true)

 

TO DO list:
- configure for internet access











