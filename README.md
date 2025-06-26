# 🎹📡 Quick & Dirty MIDI UDP Streamer

This is a quick and dirty Python utility to stream MIDI events over your LAN. It was built for personal use as part of my Linux guitar/music recording rig, but you might find it useful for your own experiments or setups!

## What does it do?
- Opens a MIDI input port (tries to auto-select your Scarlett 6i6, or falls back to the first available port)
- Forwards all incoming MIDI messages as UDP packets to a configurable IP and port (default: `10.0.0.184:8321`)
- Lets you use remote MIDI controllers, pedalboards, or synths across your network

## Why?
- Needed a simple way to get MIDI pedal events from my studio pedalboard to my DAW box, with minimal fuss
- No fancy features, just works for my use case

## Usage

```sh
nix run
```

Or, if you want to run it directly:

```sh
python3 stream_midi_udp.py
```

## Requirements
- Python 3
- [python-rtmidi](https://pypi.org/project/python-rtmidi/)
- Linux (PipeWire/ALSA recommended)

## Notes
- This is a quick hack, not a polished product! No error handling, no config file, just edit the script if you need to change the IP/port or MIDI port selection logic.
- Part of my [Linux Guitar Recording Rig](../README.md) flake, but can be used standalone.

---

Feel free to fork, adapt, and improve! 🎶
