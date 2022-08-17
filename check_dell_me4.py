#!/usr/bin/env python

#D Simpson 2021 & 2022, ds-04

#Credit to user Yogibaer75 Andreas Doehler
#<andreas.doehler@bechtle.com/andreas.doehler@gmail.com> who's code upnon which much of this code is based upon.

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

#SYNOPSIS: Script to query Dell ME array, return a dictionary and check components using functions. Ultimately returning a nagios compatible status.

import argparse
import hashlib
import json
import os
import requests
import sys

from check_me4_controllers import check_me4_controllers
from  check_me4_disks import check_me4_disks
from check_me4_fans import check_me4_fans
from check_me4_psu import check_me4_psu
from check_me4_system import check_me4_system


from requests.packages import urllib3
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

commands = (
   "controllers",
   "disks",
   "fans",
   "power-supplies",
   "system",
)
   #todo:
   #"frus"
   #"sensor-status"
   #"volumes"
   #"pools"
   #"controller-statistics"
   #"volume-statistics"
   #"ports"


def parse_arguments(argv):
    parser = argparse.ArgumentParser(description=__doc__)

    # flags
    parser.add_argument("-v", "--verbose", action="count", help="""Increase verbosity""")
    parser.add_argument("--debug",
                        action="store_true",
                        help="""Debug mode: let Python exceptions come through""")
    parser.add_argument("controller_A_ip", help="ME array controller A ip")
    parser.add_argument("controller_B_ip", help="ME array controller B ip")
    parser.add_argument("-u", "--username", required=True, help="ME array user name")
    parser.add_argument("-p", "--password", required=True, help="ME array user password")

    args = parser.parse_args(argv)
    return args


#Checks/functions called from main after fetching data
def main(argv=None):
    args = parse_arguments(argv or sys.argv[1:])
    opt_timeout = 10

    #init var as 1 uncontactable, until we know we can contact
    pingstatus = 1
    #use controller A unless we can't ping
    primary_monitor_IP = args.controller_A_ip

    #try pinging controllers, then try A then B
    hostnameA = args.controller_A_ip
    hostnameB = args.controller_B_ip
    responseA = os.system("ping -q -c 1 " + hostnameA + "> /dev/null 2>&1")
    responseB = os.system("ping -q -c 1 " + hostnameB + "> /dev/null 2>&1")
    if responseA == 0:
       pingstatus = 0
       #stay with A
       #primary_monitor_IP = args.controller_A_ip - unchanged
    elif responseA != 0 and responseB == 0:
       #use B
       pingstatus = 0
       primary_monitor_IP = args.controller_B_ip
    elif responseA != 0 and responseB != 0:
       #if neither controller pings, quit
       pingstatus = 1
       sys.exit("FATAL ERROR - Can't ping ME Array storage controllers")


    url = "https://" + primary_monitor_IP
    auth_string = hashlib.sha256("{}_{}".format(args.username, args.password).encode("utf-8")).hexdigest()

    s = requests.session()
    s.headers.update({"datatype":"json"})
    r = s.get(url + "/api/login/" + auth_string, verify=False)
    sessionKey = r.json()["status"][0]["response"]
    s.headers.update({"sessionKey": sessionKey})

    #Create a global state dictionary, use command names as keys
    ME_array_state_dict={}
    for element in commands:
        response = s.get(url + "/api/show/"+ element)
        resp_dict=json.loads(response.content)
        ME_array_state_dict[element]=resp_dict

    #PERFORM CHECKS
    #create dictionary to contain components with faults (nagios code, message)
    fault_dict={}
    #create dictionary to contain results from functions (nagios code, message)
    report_dict={}

    #initialise each and only pass to the function what is needed
    report_dict["system"] = []
    report_dict["system"].append(check_me4_system((ME_array_state_dict['system'])['system']))
    report_dict["controllers"] = []
    report_dict["controllers"].append(check_me4_controllers((ME_array_state_dict['controllers'])['controllers']))
    report_dict["disks"] = []
    report_dict["disks"].append(check_me4_disks((ME_array_state_dict['disks'])['drives']))
    report_dict["psu"] = []
    report_dict["psu"].append(check_me4_psu((ME_array_state_dict['power-supplies'])['power-supplies']))
    report_dict["fans"] = []
    report_dict["fans"].append(check_me4_fans((ME_array_state_dict['fans'])['fan']))

    
    number_of_faults=0
    fault_code_list=[]
    fault_status_list=[]
    
    for component_type in report_dict.values():
       if (component_type[0][0]) != 0:
         this_components_code=component_type[0][0]
         fault_code_list.append(this_components_code)
         fault_status_list.append(component_type)

    number_of_faults=len(fault_code_list)
    if number_of_faults > 0:
        max_fault=max(fault_code_list)        
        print(max_fault)
        print(fault_status_list)
        sys.exit(max_fault)

    elif number_of_faults == 0:
      #if healthy print system info first and include component with perf data - omit other components
      print(0)
      print(report_dict["system"])
      print(report_dict["fans"])
    
if __name__ == "__main__":
    sys.exit(main())

