import sounddevice as sd
import numpy as np
import wavio

def record_audio(filename, duration=5, sample_rate=44100):
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()
    print("Recording complete.")

    print("Saving audio...")
    wavio.write(filename, audio_data, sample_rate, sampwidth=3)
    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    output_file = "recorded_audio.wav"
    record_duration = 5  # in seconds

    record_audio(output_file, duration=record_duration)
