def check_me4_disks(data):
    #disk_states
    #0: "OK"
    #1: "Degraded"
    #2: "Fault"
    #3: "Unknown"

    disk_data=data

    message_list=[]
    disks_faulty=[]
    disks_faulty_numeric=[]

    for i in disk_data:
     disk_health=(i.get("health-numeric"))
     disk_temp=(i.get("temperature"))

     #if any disks are faulty store these
     if disk_health != 0:
       #store faulty disk(s)
       disks_faulty.append(i)

    if len(disks_faulty) > 0:
     for k in disks_faulty:
       disks_faulty_numeric.append(k.get("health-numeric"))
       if k.get("health-numeric") == 1:
         message_list.append("Degraded - Disk is degraded: ")
         disks_faulty_numeric.append(1)
         message_list.append(" enclosure-id - ")
         message_list.append(str(k.get("enclosure-id")))
         message_list.append(" slot - ")
         message_list.append(str(k.get("slot")))
         message_list.append(" s/n - ")
         message_list.append(k.get("serial-number"))
         message_list.append(" model - ")
         message_list.append(k.get("model"))
         message_list.append(" size - ")
         message_list.append(k.get("size"))
         message_list.append(" health - ")
         message_list.append(k.get("health"))
         message_list.append(" ")
         message_list.append(" | ")
       elif k.get("health-numeric") == 2:
         message_list.append("Fault - Disk has fault: ")
         disks_faulty_numeric.append(2)
         message_list.append(" enclosure-id - ")
         message_list.append(str(k.get("enclosure-id")))
         message_list.append(" slot - ")
         message_list.append(str(k.get("slot")))
         message_list.append(" s/n - ")
         message_list.append(k.get("serial-number"))
         message_list.append(" model - ")
         message_list.append(k.get("model"))
         message_list.append(" size - ")
         message_list.append(k.get("size"))
         message_list.append(" health - ")
         message_list.append(k.get("health"))
         message_list.append(" ")
         message_list.append(" | ")
       elif k.get("health-numeric") == 3:
         message_list.append("UNKNOWN - Disk is UNKNOWN ")
         disks_faulty_numeric.append(3)
         message_list.append(" ")
         message_list.append(" | ")

    else:
      #perf data
      #perf_data_str=""
      #perf_data_str=(perf_data_str.join([str(element) for element in perf_list]))
      #message_list.append(perf_data_str)
      message_list.append("OK - All disks OK")       
      #all disks are ok so set status 0
      disks_faulty_numeric.append(0)

    #find the most severe numeric status for report, which will be 0 if ok
    status_num=max(disks_faulty_numeric)

    message=""
    message=(message.join(message_list))

    return status_num, message
