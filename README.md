# dell_me4_array_nagios_check

<h1>Background</h1>

***CURRENTLY IN TESTING, NOT PRODUCTION READY, USE AT OWN RISK***

Nagios compatible check for Dell ME4 storage array via API, for use with various monitoring systems that understand nagios status

Developed with the motivation of use with the LibreNMS monitoring system.

Some of the code is based on work by user Yogibaer75 (for the CheckMK monitoring system) found here:
https://github.com/Yogibaer75/Check_MK-Things/tree/master/check%20plugins%202.0/dell_powervault_me4


To run the script:

./check_dell_me.py   -u ME_array_username   -p ME_array_password   controllerA_ip   controllerB_ip 

Example output:
```
[(0, u'OK - System is OK - ME4084 MY_ARRAY MY_LOCATION')]
[(0, 'OK - All fans OK RPM: 7440 7500 7500 7440 7440 7440 7440 7440 7440 7440 ')]
```

<h2>Usage</h2>

Ideally you plumb into your monitoring system.

Otherwise you can use this crude script and adapt for cron.

```
check_MYARR1=`/path/to/dell_me4_array_nagios_check/check_dell_me4.py -u user -p 'password' IP1 IP2`
check_MYARR1_res=`echo ${check_MYARR1} | head -c1`

if [ ${check_MYARR1_res} == 0 ];
then
	:
else
        echo "PLEASE CHECK MYARR1 ME4084...";
        echo " ";
        echo "${check_MYARR1}"
fi
```
