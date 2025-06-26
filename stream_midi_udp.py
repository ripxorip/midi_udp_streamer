#!/usr/bin/env python3
import socket
import rtmidi
import sys
import signal

# Suppress BrokenPipeError on stdout (e.g., when piped through sed and killed)
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

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
    print(f"Opening MIDI port: {ports[scarlett_port]}", flush=True)
    midiin.open_port(scarlett_port)
else:
    print("Scarlett 6i6 port not found, falling back to first available port.", flush=True)
    if ports:
        midiin.open_port(0)
    else:
        midiin.open_virtual_port("Python MIDI Input")

print(f"Listening for MIDI and sending to {UDP_IP}:{UDP_PORT}...", flush=True)

try:
    while True:
        msg = midiin.get_message()
        if msg:
            message, delta_time = msg
            try:
                print(f"Sending MIDI: {message}", flush=True)
            except BrokenPipeError:
                pass
            sock.sendto(bytes(message), (UDP_IP, UDP_PORT))
except KeyboardInterrupt:
    print("Exiting...", flush=True)

midiin.close_port()
sock.close()
