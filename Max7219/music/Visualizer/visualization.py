import sounddevice as sd
import numpy as np
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas

# Constants for audio processing
CHUNK = 1024
CHANNELS = 1
RATE = 44100

# Initialize sounddevice for capturing audio
def audio_callback(indata, frames, time, status):
    """Callback function for handling audio input in real-time."""
    if status:
        print(status)
    magnitudes = audio_fft(indata)
    update_led_matrix(magnitudes)

# Initialize MAX7219 LED matrix
serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1)

def audio_fft(data):
    """Perform FFT on audio data and return frequency magnitudes."""
    samples = np.squeeze(data)  # Remove single-dimensional entries
    fft_output = np.fft.fft(samples)
    magnitudes = np.abs(fft_output[:CHUNK // 2])
    return magnitudes

def update_led_matrix(magnitudes):
    """Update the LED matrix based on the frequency magnitudes."""
    levels = np.interp(magnitudes[:8], [0, np.max(magnitudes)], [0, 8])
    with canvas(device) as draw:
        for i in range(8):
            level = int(levels[i])
            for j in range(level):
                draw.point((i, 7 - j), fill="white")

try:
    print("Music visualizer running... Press Ctrl+C to stop.")
    
    # Start the audio stream, using the callback function to process audio in real-time
    with sd.InputStream(channels=CHANNELS, callback=audio_callback, blocksize=CHUNK, samplerate=RATE):
        while True:
            pass  # Keep the stream running

except KeyboardInterrupt:
    print("Stopping visualizer...")
