# dell_me4_array_nagios_check

***CURRENTLY IN TESTING, NOT PRODUCTION READY, USE AT OWN RISK***

Nagios compatable check for Dell ME4 array via API, for use with various monitoring systems that understand nagios status

Some of the code is based on work by user Yogibaer75 found here:
https://github.com/Yogibaer75/Check_MK-Things/tree/master/check%20plugins%202.0/dell_powervault_me4


To run the script:

./check_dell_me.py   -u ME_array_username   -p ME_array_password   controllerA_ip   controllerB_ip 

Example output:

[(0, u'OK - System is OK - ME4084 MY_ARRAY MY_LOCATION')]
[(0, 'OK - All fans OK RPM: 7440 7500 7500 7440 7440 7440 7440 7440 7440 7440 ')]

