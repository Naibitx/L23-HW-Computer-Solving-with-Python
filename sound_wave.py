import numpy as np
import matplotlib.pyplot as mpt

def plot_sine_wave(frequency=1, amplitude=1, phase=0, duration=1, sampling_rate=1000):

    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)#generate time values

    
    y = amplitude * np.sin(2 * np.pi * frequency * t + phase)#generate sine wave values

    
    #plot the sine wave
    mpt.figure(figsize=(10, 4))
    mpt.plot(t, y, label=f'{frequency} Hz Sine Wave')
    mpt.title("Sine Wave")
    mpt.xlabel("Time (s)")
    mpt.ylabel("Amplitude")
    mpt.grid(True)
    mpt.legend()
    mpt.show()

if __name__ == "__main__":
    plot_sine_wave() #plot a sine wave with default parameters
