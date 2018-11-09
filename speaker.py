import socket
import pyaudio
import wave

#record
CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 40


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("*recording")

frames = []

for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
    data  = stream.read(CHUNK)
    frames.append(data)
    udp_header = struct.pack('---------1---------', sport, dport, length, checksum)

    server.sendto(udp_header+data, ('255.255.255.255', 12345))

print("*done recording")

stream.stop_stream()
stream.close()
p.terminate()
server.close()

print("*closed")
