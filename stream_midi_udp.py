#!/usr/bin/env python3
import socket
import rtmidi

UDP_IP = "10.0.0.184"
UDP_PORT = 8321

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

midiin = rtmidi.MidiIn()
ports = midiin.get_ports()

# Try to open the Scarlett 6i6 port if available
scarlett_port = None
for i, port in enumerate(ports):
    if "Scarlett 6i6" in port:
        scarlett_port = i
        break

if scarlett_port is not None:
    print(f"Opening MIDI port: {ports[scarlett_port]}")
    midiin.open_port(scarlett_port)
else:
    print("Scarlett 6i6 port not found, falling back to first available port.")
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
