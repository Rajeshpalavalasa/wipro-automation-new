
import can

bus = can.interface.Bus(
    channel='can0',
    interface='socketcan'
)

msg = can.Message(
    arbitration_id=0x123,
    data=[10, 20, 30, 40],
    is_extended_id=False
)

bus.send(msg)
print("Message sent")
