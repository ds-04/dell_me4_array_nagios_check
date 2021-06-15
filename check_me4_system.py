def check_me4_system(data):

    message_list=[]
    
    system_data=data

    #index on 1
    for i in system_data:
      system_health=(i.get("health-numeric"))
      system_model=(i.get("product-id"))
      system_contA=(i.get("controller-a-serial-number"))
      system_contB=(i.get("controller-b-serial-number"))
      system_loc=(i.get("system-location"))
      system_name=(i.get("system-name"))

    if system_health == 0:
      message="OK - System is OK"
      status_num=0
    elif system_health == 1:
      message="Degraded - System is degraded"
      status_num=1
    elif system_health == 2:
      message="Fault - System has fault"
      status_num=2
    elif system_health == 3:
      message="Unknown - System state is unknown"
      status_num=3

    #build the message
    message_list.append(message)
    message_list.append(" - ")
    message_list.append(system_model)
    message_list.append(" ")
    message_list.append(system_name)
    message_list.append(" ")
    message_list.append(system_loc)

    final_message=""
    final_message=(final_message.join(message_list))

    return status_num, final_message
