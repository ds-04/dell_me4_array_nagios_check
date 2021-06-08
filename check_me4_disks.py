def check_me4_disks(data):
    #disk_states
    #0: "OK"
    #1: "Degraded"
    #2: "Fault"
    #3: "Unknown"

    payload=(data['disks'])
    disk_data=(payload['drives'])

    message_list=[]
    disks_faulty=[]

    for i in disk_data:
     disk_health=(i.get("health-numeric"))
     disk_temp=(i.get("temperature"))

     #if any disks are faulty store location/index
     if disk_health != 0:
       #store index of faulty disk(s)
       disks_faulty.append(i)

    if len(disks_faulty) > 0:
     for k in disks_faulty:
       message_list.append("Fault - Disk has fault: ")
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
       status_num=2

    else:
       #perf_data_str=""
       #perf_data_str=(perf_data_str.join([str(element) for element in perf_list]))
       message_list.append("OK - All disks OK")
       #message_list.append(perf_data_str)
       status_num=0

    message=""
    message=(message.join(message_list))

    return status_num, message
