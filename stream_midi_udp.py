#!/usr/bin/env python3
import socket
import rtmidi

UDP_IP = "10.0.0.184"
UDP_PORT = 8321

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

midiin = rtmidi.MidiIn()
ports = midiin.get_ports()
if ports:
    midiin.open_port(0)
else:
    midiin.open_virtual_port("Python MIDI Input")

print(f"Listening for MIDI and sending to {UDP_IP}:{UDP_PORT}...")

try:
    while True:
        msg = midiin.get_message()
        if msg:
            message, delta_time = msg
            print(f"Sending MIDI: {message}")
            sock.sendto(bytes(message), (UDP_IP, UDP_PORT))
except KeyboardInterrupt:
    print("Exiting...")

midiin.close_port()
sock.close()
