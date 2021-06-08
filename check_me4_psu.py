def check_me4_psu(data):

  payload=(data['power-supplies'])
  power_supply_data=(payload['power-supplies'])

  PSU1_state=(power_supply_data[0]['health-numeric'])
  PSU2_state=(power_supply_data[1]['health-numeric'])

  if PSU1_state == 0 and PSU2_state == 0:
       message="OK - All PSUs OK"
       status_num=0       
  elif PSU1_state == 1 or PSU2_state == 1:
       message="Degraded - PSU is degraded"
       status_num=1
  elif PSU1_state == 2 or PSU2_state == 2:
       message="Fault - PSU has fault"
       status_num=2 
  elif PSU1_state == 3 or PSU2_state == 3:
       message="Unknown - PSU is unknown"
       status_num=3

  return status_num, message
