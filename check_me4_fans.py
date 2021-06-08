def check_me4_fans(data):
   #overall dict -> fans dictionary -> list of all fans -> a fan dictionary

   payload=(data['fans'])
   fans_data=(payload['fan'])

   #create lists
   fans_faulty=[]
   message_list=[]
   perf_list=[ " RPM: "]

   for i in fans_data:
     fan_health=(i.get("health-numeric"))
     fan_perf=(i.get("speed"))
     perf_list.append(fan_perf)
     perf_list.append(" ")

     #if any fans are faulty store location/index
     if fan_health != 0:
       #store index of faulty fans
       fans_faulty.append(i)
       
   if len(fans_faulty) > 0:
     for k in fans_faulty:
       message_list.append("Fault - fan has fault: ")
       message_list.append(k.get("location", "Unknown"))
       message_list.append(" ")
       message_list.append(k.get("name"))
       message_list.append(" | ")
       status_num=2
      
   else:
       perf_data_str=""
       perf_data_str=(perf_data_str.join([str(element) for element in perf_list]))
       message_list.append("OK - All fans OK")
       message_list.append(perf_data_str)
       status_num=0

   message=""
   message=(message.join(message_list))

   return status_num, message
