import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Load audio file
fs, signal = wavfile.read("heartbeat.wav")

# Convert to mono if stereo
if len(signal.shape) > 1:
    signal = signal[:, 0]

# Normalize
signal = signal / np.max(np.abs(signal))

# Zero crossing detection
zero_crossings = np.where(np.diff(np.sign(signal)) > 0)[0]

# Convert index to time
beat_times = zero_crossings / fs

# Calculate beats
total_beats = len(beat_times)

# Beats per minute
duration_sec = len(signal) / fs
bpm = (total_beats / duration_sec) * 60

print("Total beats detected:", total_beats)
print("Recording duration (sec):", round(duration_sec, 2))
print("Beats per minute (BPM):", round(bpm, 2))

# Plot waveform
plt.plot(signal)
plt.title("Heartbeat Audio Waveform")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()
