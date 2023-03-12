from mavlink import mavutil
import time


master = mavutil.mavlink_connection('udpout:192.168.2.1:14550') 

f_speed = 0.5 
msg = master.mav.set_position_target_local_ned_encode(
    0, # time_boot_ms
    mavutil.mavlink.MAV_FRAME_LOCAL_NED, # coordinate frame
    0b0000111111000111, # type_mask (only set velocity values)
    0, 0, 0, # x, y, z positions (not used)
    0, 0, 0, # x, y, z velocity
    0, 0, 0, # x, y, z acceleration (not used)
    0, 0) # yaw, yaw_rate (not used)
msg.velocity.x = f_speed 
msg.velocity.y = 0 # set lateral velocity to 0
msg.velocity.z = 0 # set vertical velocity to 0
master.mav.send(msg)

time.sleep(5)

msg.velocity.x = 0 
master.mav.send(msg)
