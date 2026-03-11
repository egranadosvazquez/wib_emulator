import zmq
import wib_pb2
from datetime import datetime
from google.protobuf.any_pb2 import Any
import random
def fill_repeated(field, value_list):
    field.clear()  # remove any previous values
    field.extend(value_list)

def assign_field(field, value, count=1):
    """Handles both repeated and scalar protobuf fields."""
    if hasattr(field, "extend"):
        field.extend([value] * count)
    else:
         # Directly assign if scalar
        return value

class WIBEmulator:
    def __init__(self):
        pass

    def update_state(self):
        # Optional periodic state update
        pass
    
    
    def handle_request(self, raw_msg: bytes):
        try:
            raw_str = raw_msg.decode("utf-8").strip().strip('"')
        except Exception:
            raw_str = ""
        msg_any = Any()
        try:
            msg_any.ParseFromString(raw_msg)
        except Exception as e:
            print(f"[!] Error parsing protobuf Any: {e}")
            return None

        print(f"[>] Got type_url = {msg_any.type_url}")

        #reply_any = Any()


        # --------- TIMESTAMP REQUEST ----------
        if msg_any.type_url.endswith("wib.GetTimestamp"):
            reply = wib_pb2.GetTimestamp.Timestamp()
            reply.timestamp = int(datetime.utcnow().timestamp())
            reply.day = datetime.utcnow().day
            reply.month = datetime.utcnow().month
            reply.year = datetime.utcnow().year
            reply.hour = datetime.utcnow().hour
            reply.min = datetime.utcnow().minute
            reply.sec = datetime.utcnow().second

            print("[OK] Sent timestamp")
            return reply.SerializeToString()

        # --------- SOFTWARE VERSION ----------
        elif msg_any.type_url.endswith("wib.GetSWVersion"):
            reply = wib_pb2.GetSWVersion.Version()
            reply.version = "v1.0.0-emulated"
            print("[OK] Sent software version")
            return reply.SerializeToString()

        # --------- SENSOR DATA ----------
        elif msg_any.type_url.endswith("wib.GetSensors"):
            reply = wib_pb2.GetSensors.Sensors()
            # Voltages 
            reply.ltc2990_4c_voltages.append(1.2+random.uniform(-0.05,0.05))# 4 sensorsv0
            reply.ltc2990_4c_voltages.append(1.2+random.uniform(-0.05,0.05))
            reply.ltc2990_4c_voltages.append(3.3+random.uniform(-0.05,0.05))
            reply.ltc2990_4c_voltages.append(3.3+random.uniform(-0.05,0.05))
            reply.ltc2990_4e_voltages.append(0.9+random.uniform(-0.05,0.05))# 4 sensors
            reply.ltc2990_4e_voltages.append(0.9+random.uniform(-0.05,0.05))
            reply.ltc2990_4e_voltages.append(1.2+random.uniform(-0.05,0.05))
            reply.ltc2990_4e_voltages.append(0.6+random.uniform(-0.05,0.05))
            reply.ltc2991_48_voltages.append(0.85+random.uniform(-0.05,0.05))#8 sensors
            reply.ltc2991_48_voltages.append(0.85+random.uniform(-0.05,0.05))
            reply.ltc2991_48_voltages.append(5.0+random.uniform(-0.05,0.05))
            reply.ltc2991_48_voltages.append(5.0+random.uniform(-0.05,0.05))
            reply.ltc2991_48_voltages.append(2.5+random.uniform(-0.05,0.05))
            reply.ltc2991_48_voltages.append(2.5+random.uniform(-0.05,0.05))
            reply.ltc2991_48_voltages.append(1.8+random.uniform(-0.05,0.05))
            reply.ltc2991_48_voltages.append(1.8+random.uniform(-0.05,0.05))
            reply.femb0_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) #8 sensors (nominal 4V)
            reply.femb0_dc2dc_ltc2991_voltages.append(reply.femb0_dc2dc_ltc2991_voltages[0] - (0.1*random.uniform(0.3,0.9)))
            reply.femb0_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) # (nominal 4)
            reply.femb0_dc2dc_ltc2991_voltages.append(reply.femb0_dc2dc_ltc2991_voltages[2] - (0.1*random.uniform(0.1,0.3))) 
            reply.femb0_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) # (nominal 4)
            reply.femb0_dc2dc_ltc2991_voltages.append(reply.femb0_dc2dc_ltc2991_voltages[4] - (0.1*random.uniform(1.4,1.9)))
            reply.femb0_dc2dc_ltc2991_voltages.append(4.6+random.uniform(0, 0.1)) 
            reply.femb0_dc2dc_ltc2991_voltages.append(4.7+random.uniform(0, 0.1)) 
            reply.femb1_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) #8 sensors (nominal 4V)
            reply.femb1_dc2dc_ltc2991_voltages.append(reply.femb1_dc2dc_ltc2991_voltages[0] - (0.1*random.uniform(0.3,0.9)))
            reply.femb1_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) # (nominal 4)
            reply.femb1_dc2dc_ltc2991_voltages.append(reply.femb1_dc2dc_ltc2991_voltages[2] - (0.1*random.uniform(0.1,0.3)))
            reply.femb1_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) # (nominal 4)
            reply.femb1_dc2dc_ltc2991_voltages.append(reply.femb1_dc2dc_ltc2991_voltages[4] - (0.1*random.uniform(1.4,1.9)))
            reply.femb1_dc2dc_ltc2991_voltages.append(5.6+random.uniform(0, 0.1)) 
            reply.femb1_dc2dc_ltc2991_voltages.append(5.7+random.uniform(0, 0.1)) 
            reply.femb2_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) #8 sensors (nominal 4V)
            reply.femb2_dc2dc_ltc2991_voltages.append(reply.femb2_dc2dc_ltc2991_voltages[0] - (0.1*random.uniform(0.3,0.9)))
            reply.femb2_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) # (nominal 4)
            reply.femb2_dc2dc_ltc2991_voltages.append(reply.femb2_dc2dc_ltc2991_voltages[2] - (0.1*random.uniform(0.1,0.3)))
            reply.femb2_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) # (nominal 4)
            reply.femb2_dc2dc_ltc2991_voltages.append(reply.femb2_dc2dc_ltc2991_voltages[4] - (0.1*random.uniform(1.4,1.9)))
            reply.femb2_dc2dc_ltc2991_voltages.append(6.6+random.uniform(0, 0.1)) 
            reply.femb2_dc2dc_ltc2991_voltages.append(6.7+random.uniform(0, 0.1)) 
            reply.femb3_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) #8 sensors (nominal 4V)
            reply.femb3_dc2dc_ltc2991_voltages.append(reply.femb3_dc2dc_ltc2991_voltages[0] - (0.1*random.uniform(0.3,0.9)))
            reply.femb3_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) # (nominal 4)
            reply.femb3_dc2dc_ltc2991_voltages.append(reply.femb3_dc2dc_ltc2991_voltages[2] - (0.1*random.uniform(0.1,0.3)))
            reply.femb3_dc2dc_ltc2991_voltages.append(random.uniform(2.5, 4.5)) # (nominal 4)
            reply.femb3_dc2dc_ltc2991_voltages.append(reply.femb3_dc2dc_ltc2991_voltages[4] - (0.1*random.uniform(1.4,1.9)))
            reply.femb3_dc2dc_ltc2991_voltages.append(7.6+random.uniform(0, 0.1)) 
            reply.femb3_dc2dc_ltc2991_voltages.append(7.7+random.uniform(0, 0.1)) 
            reply.femb_ldo_a0_ltc2991_voltages.append(8.0+random.uniform(0, 0.1)) # 8 sensors
            reply.femb_ldo_a0_ltc2991_voltages.append(8.1+random.uniform(0, 0.1)) 
            reply.femb_ldo_a0_ltc2991_voltages.append(8.2+random.uniform(0, 0.1)) 
            reply.femb_ldo_a0_ltc2991_voltages.append(8.3+random.uniform(0, 0.1)) 
            reply.femb_ldo_a0_ltc2991_voltages.append(8.4+random.uniform(0, 0.1)) 
            reply.femb_ldo_a0_ltc2991_voltages.append(8.5+random.uniform(0, 0.1)) 
            reply.femb_ldo_a0_ltc2991_voltages.append(8.6+random.uniform(0, 0.1)) 
            reply.femb_ldo_a0_ltc2991_voltages.append(8.7+random.uniform(0, 0.1)) 
            reply.femb_ldo_a1_ltc2991_voltages.append(9.0+random.uniform(0, 0.1)) # 8 sensors
            reply.femb_ldo_a1_ltc2991_voltages.append(9.1+random.uniform(0, 0.1)) 
            reply.femb_ldo_a1_ltc2991_voltages.append(9.2+random.uniform(0, 0.1)) 
            reply.femb_ldo_a1_ltc2991_voltages.append(9.3+random.uniform(0, 0.1)) 
            reply.femb_ldo_a1_ltc2991_voltages.append(9.4+random.uniform(0, 0.1)) 
            reply.femb_ldo_a1_ltc2991_voltages.append(9.5+random.uniform(0, 0.1)) 
            reply.femb_ldo_a1_ltc2991_voltages.append(9.6+random.uniform(0, 0.1)) 
            reply.femb_ldo_a1_ltc2991_voltages.append(9.7+random.uniform(0, 0.1)) 
            reply.femb_bias_ltc2991_voltages.append(4.95+random.uniform(0, 0.1)) #8 sensors
            reply.femb_bias_ltc2991_voltages.append(reply.femb_bias_ltc2991_voltages[0]-(1e-4*random.uniform(0, 10))) 
            reply.femb_bias_ltc2991_voltages.append(5.0+random.uniform(0, 0.1)) 
            reply.femb_bias_ltc2991_voltages.append(reply.femb_bias_ltc2991_voltages[2]-(1e-4*random.uniform(0, 10))) 
            reply.femb_bias_ltc2991_voltages.append(5.0+random.uniform(0, 0.1)) 
            reply.femb_bias_ltc2991_voltages.append(reply.femb_bias_ltc2991_voltages[4]-(1e-4*random.uniform(0, 10))) 
            reply.femb_bias_ltc2991_voltages.append(5.0+random.uniform(0, 0.1)) 
            reply.femb_bias_ltc2991_voltages.append(reply.femb_bias_ltc2991_voltages[6]-(1e-4*random.uniform(0, 10))) 
            # 0x15 LTC2499 temperature sensor inputs from LTM4644 for FEMB 0 - 3 and WIB 1 - 3
            reply.ltc2499_15_temps.append(5.0+random.uniform(0, 0.1)) # 7 sensors
            reply.ltc2499_15_temps.append(5.1+random.uniform(0, 0.1)) 
            reply.ltc2499_15_temps.append(5.2+random.uniform(0, 0.1)) 
            reply.ltc2499_15_temps.append(5.3+random.uniform(0, 0.1)) 
            reply.ltc2499_15_temps.append(5.4+random.uniform(0, 0.1)) 
            reply.ltc2499_15_temps.append(5.5+random.uniform(0, 0.1)) 
            reply.ltc2499_15_temps.append(5.6+random.uniform(0, 0.1)) 
            print (reply.femb0_dc2dc_ltc2991_voltages)
            # Onboard temperature sensors
            reply.ad7414_49_temp = 22+random.uniform(0, 1.) 
            reply.ad7414_4d_temp = 23+random.uniform(0, 1.) 
            reply.ad7414_4a_temp = 24+random.uniform(0, 1.)
            print("[OK] Sent sensor readings")
            return reply.SerializeToString()

#        elif msg_any.type_url.endswith("wib.Peak"):
#            reply = wib_pb2.
#            
#            return reply.SerializeToString()

        elif msg_any.type_url.endswith("wib.GetTimingStatus"):
            reply = wib_pb2.GetTimingStatus.TimingStatus()
            #SI5344 status register values
            reply.lol_val = 1
            reply.lol_flg_val = 2
            reply.los_val = 3
            reply.los_flg_val = 4
            #Firmware timing endpoint status register
            reply.ept_status = 5
            print("[OK] Timing Status")
            return reply.SerializeToString()

        # --------- UNKNOWN MESSAGE ----------
        else:
            print(f"[!] Unknown request type: {msg_any.type_url}")
            return None
        #return reply_any.SerializeToString()

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("WIB Emulator running at tcp://*:5555")

    wib = WIBEmulator()

    while True:
        try:
            raw = socket.recv()
            print(f"\n[<] Received {len(raw)} bytes")
            reply = wib.handle_request(raw)
            if reply:
                #print(f"Sending something {reply}")
                socket.send(reply)
            else:
                print ("Wrong message, the reply is empty")
                socket.send(b"")
        except Exception as e:
            print(f"[!] Runtime error: {e}")
            socket.send(b"")

if __name__ == "__main__":
    main()





