# Hi team IOET.

The proposed test was developed with Python and its estándar library, Using Camel Case notation also I did trying to use the pattern chain of responsability however the algorithm was short the implementation have some limits.

# The Project contains the following folders:
####1 Constant  - it has 3 files:
######1.1	weekdays.py, This file save homologation information of days of the Week and its abbreviations, so that its used like enum method or similar. 

![](https://github.com/jefvasquezg/acme/blob/master/images/1.png)

######1.2	default.py, This file save workdays information  (work week and work weekend) and schedules ( morning from ’00:01’ to ’09:00’, noon ’09:01’ to ’18:00’, nights from ’18:01’ to ’00:00’ ), we can send the arguments like start hours, end hours and value amount hours, this file require the timezone class because this declaration declaration will be used to define the working days, their hours and values. 
![](https://github.com/jefvasquezg/acme/blob/master/images/2.png)

######1.3	days_info.py, the file has an array, this array build and save information ( days, hours ranges, value amount hours) for all weekdays, this array require import weekdays, defaults and day class of file day.py
![](https://github.com/jefvasquezg/acme/blob/master/images/3.png)
