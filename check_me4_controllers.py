def check_me4_controllers(data):

    controller_data=data

    controllerA_state=(controller_data[0]['health-numeric'])
    controllerB_state=(controller_data[1]['health-numeric'])

    if controllerA_state == 0 and controllerB_state == 0:
       message="OK - All Controllers OK"
       status_num=0       
    elif controllerA_state == 1 or controllerB_state == 1:
       message="Degraded - Controller is degraded"
       status_num=1
    elif controllerA_state == 2 or controllerB_state == 2:
       message="Fault - Controller has fault"
       status_num=2 
    elif controllerA_state == 3 or controllerB_state == 3:
       message="Unknown - Controller is unknown"
       status_num=3

    return status_num, message
