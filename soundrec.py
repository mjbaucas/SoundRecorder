import pyaudio
import wave


form = pyaudio.paInt16
channel_number = 1L
sampling_rate = 16000
chunk_size = 4096
record_length = 5
device_index = 2
wave_file_name = 'test.wav'

audio=pyaudio.PyAudio()
stream = audio.open(format=form, rate=sampling_rate, channels=channel_number, input_device_index=device_index, input=True, frames_per_buffer=chunk_size)

print('Recording')
frames = []

for ii in range(0, int((sampling_rate/chunk_size)*record_length)):
	data = stream.read(chunk_size)
	frames.append(data)
	
print('Finished Recording')

stream.stop_stream()
stream.close()
audio.terminate()

wavefile = wave.open(wave_file_name, 'wb')
wavefile.setnchannels(channel_number)
wavefile.setsampwidth(audio.get_sample_size(form))
wavefile.setframerate(sampling_rate)
wavefile.writeframes(b''.join(frames))
wavefile.close()
