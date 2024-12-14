import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, StringVar

# Constants
CARRIER_FREQ_1 = 5  # Hz for binary 1 (FSK)
CARRIER_FREQ_0 = 2  # Hz for binary 0 (FSK)
CARRIER_AMPLITUDE_1 = 1  # Amplitude for binary 1 (ASK)
CARRIER_AMPLITUDE_0 = 0.5  # Amplitude for binary 0 (ASK)
PHASE_SHIFT_1 = 0  # Phase for binary 1 (PSK)
PHASE_SHIFT_0 = np.pi  # Phase for binary 0 (PSK)
TIME = np.linspace(0, 1, 1000)  # Time array

# Modulation Functions
def ask_modulation(data):
    signal = np.array([])
    for bit in data:
        amplitude = CARRIER_AMPLITUDE_1 if bit == 1 else CARRIER_AMPLITUDE_0
        modulated_bit = amplitude * np.sin(2 * np.pi * CARRIER_FREQ_1 * TIME)
        signal = np.concatenate((signal, modulated_bit))
    return signal

def fsk_modulation(data):
    signal = np.array([])
    for bit in data:
        freq = CARRIER_FREQ_1 if bit == 1 else CARRIER_FREQ_0
        modulated_bit = np.sin(2 * np.pi * freq * TIME)
        signal = np.concatenate((signal, modulated_bit))
    return signal

def psk_modulation(data):
    signal = np.array([])
    for bit in data:
        phase = PHASE_SHIFT_1 if bit == 1 else PHASE_SHIFT_0
        modulated_bit = np.sin(2 * np.pi * CARRIER_FREQ_1 * TIME + phase)
        signal = np.concatenate((signal, modulated_bit))
    return signal

# GUI Application
def simulate_modulation():
    try:
        data = [int(bit) for bit in input_var.get()]
        
        # Validate input
        if not all(bit in [0, 1] for bit in data):
            raise ValueError("Input must contain only 0s and 1s.")
        
        # Generate modulated signals
        ask_signal = ask_modulation(data)
        fsk_signal = fsk_modulation(data)
        psk_signal = psk_modulation(data)

        # Plot the signals
        plt.figure(figsize=(10, 8))

        plt.subplot(3, 1, 1)
        plt.title("Amplitude Shift Keying (ASK)")
        plt.plot(ask_signal)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")

        plt.subplot(3, 1, 2)
        plt.title("Frequency Shift Keying (FSK)")
        plt.plot(fsk_signal)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")

        plt.subplot(3, 1, 3)
        plt.title("Phase Shift Keying (PSK)")
        plt.plot(psk_signal)
        plt.xlabel("Time")
        plt.ylabel("Amplitude")

        plt.tight_layout()
        plt.show()

    except ValueError as e:
        error_label.config(text=f"Error: {e}")

# Main GUI setup
root = Tk()
root.title("Digital to Analog Modulation")

Label(root, text="Enter Digital Data Stream :").pack(pady=10)
input_var = StringVar()
Entry(root, textvariable=input_var, width=30).pack(pady=5)

Button(root, text="Simulate Modulation", command=simulate_modulation).pack(pady=10)
error_label = Label(root, text="", fg="red")
error_label.pack()

root.mainloop()
