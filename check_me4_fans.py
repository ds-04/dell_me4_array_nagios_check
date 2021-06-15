def check_me4_fans(data):
   #overall dict -> fans dictionary -> list of all fans -> a fan dictionary .. this is already passed to this function
   fans_data=data

   #create lists
   fans_faulty=[]
   fans_faulty_numeric=[]
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
       if k.get("health-numeric") == 1:
         message_list.append("Degraded - Fan is degraded: ")
         fans_faulty_numeric.append(1)

       elif k.get("health-numeric") == 2:
         message_list.append("Fault - fan has fault: ")
         fans_faulty_numeric.append(2)

       elif k.get("health-numeric") == 3:
         message_list.append("UNKNOWN - fan is UNKNOWN ")
         fans_faulty_numeric.append(3)

     message_list.append(k.get("location", "Unknown"))
     message_list.append(" ")
     message_list.append(k.get("name", "Unknown"))
     message_list.append(" | ")
      
   else:
     perf_data_str=""
     perf_data_str=(perf_data_str.join([str(element) for element in perf_list]))
     message_list.append("OK - All fans OK")
     message_list.append(perf_data_str)
     fans_faulty_numeric.append(0)


   #find the most severe numeric status for report, which will be 0 if ok
   status_num=max(fans_faulty_numeric)

   message=""
   message=(message.join(message_list))

   return status_num, message
