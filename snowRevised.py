import numpy as np
from matplotlib import pyplot as plt
from numpy.fft import ifft, fft

import util

def applyfft(signal, Fs):
    # Fs = fs
    # N = fftSize
    # N = 64
    N = len(signal)
    # fStep = Fs / N
    fStep = Fs / N
    # fStep = 400000
    # tStep = 1 / Fs
    f = np.linspace(0, (N - 1) * fStep, N)
    X = np.fft.fft(signal, N)
    Xphase = np.angle(X)
    Xmag = np.abs(X) / N

    freq = np.fft.fftfreq(64)

    fRealized = f[0: int(N / 2 + 1)]
    #fRealized = f
    XmagRealized = 2 * Xmag[0: int(N / 2 + 1)]
    XmagRealized[0] = Xmag[0] / 2
    magnitude = np.amax(XmagRealized)
    magnitudeIndex = np.argmax(XmagRealized)
    phase = Xphase[magnitudeIndex]
    # frequency = fRealized[int(magnitudeIndex)]



    plt.plot(fRealized, XmagRealized)
    plt.show()





def applyCarrier(data, fc, fs):
    # N = fftSize  # Number of symbols to be sent.
    N = len(data)  # Number of symbols to be sent.
    Fc = fc  # Carrier frequency.
    Fs = fs  # Sampling frequency.
    # tStep = 1 / Fs  # Width of each symbol (in sec).
    tStep = 1 / Fs  # Width of each symbol (in sec).

    t = np.linspace(0, (N - 1) * tStep, N)
    carrier = np.cos(2 * np.pi * Fc * t)
    modData = np.multiply(data, carrier)
    return modData


def getCarrierFrequencyList(numberOfCarriers):
    global numberOfCarriersUtil
    numberOfCarriersUtil = numberOfCarriers
    carrierFrequencyList = []

    startFrequency =   100
    subcarrierSpacing = 50


    for i in range(numberOfCarriers):
        frequency = startFrequency + subcarrierSpacing * (i+1)
        # frequency = startFrequency + 10000000 * (i + 1) + bandWidth * (i + 1)
        carrierFrequencyList.append(frequency)

    return carrierFrequencyList


numberOfNodes = 1
numberOfSubcarriers = 3
subCarrierBinary40ByteDataList = []
subCarrierSpreadedDataList = []
compositeSignal = []
carrierFrequencyList = util.getCarrierFrequencyList(numberOfSubcarriers)
for i in range(numberOfSubcarriers):
    subCarrierBinary40ByteDataList.append(util.getBinary40byteDataList(numberOfNodes)[0])

for i in range(numberOfSubcarriers):
    subCarrierSpreadedDataList.append(applyCarrier(subCarrierBinary40ByteDataList[i], carrierFrequencyList[i], carrierFrequencyList[i]*2))

for i in range(len(subCarrierSpreadedDataList)):
    compositeSignal.extend(subCarrierSpreadedDataList[i])

print(list(subCarrierBinary40ByteDataList))



#applyfft(subCarrierSpreadedDataList[0], carrierFrequencyList[0]*2)
# applyfft(compositeSignal, 740000000*2)

carrierFrequencyList = util.getCarrierFrequencyList2(numberOfSubcarriers)
subCarrierBinary40ByteDataList = []
for i in range(numberOfSubcarriers):
    subCarrierBinary40ByteDataList.append(util.getBinary40byteDataList(numberOfNodes))

def buildSignal():
    # sampling rate
    #sr = 2000
    sr = 320
    # sampling interval
    ts = 1.0 / sr
    t = np.arange(0, 1, ts)
    compositeBit = []
    for i in range(len(carrierFrequencyList)):
        carrierFrequency = carrierFrequencyList[i]
        subcarrierNodesData = subCarrierBinary40ByteDataList[i]
        for j in range(len(subcarrierNodesData)):
            nodeData = subcarrierNodesData[j]
            nodeCarrierSignal = 1 * np.sin(2 * np.pi * carrierFrequency * t)
            for k in range(len(nodeData)):
                # compositeBit.append() = np.multipl(nodeData[i], nodeCarrierSignal)
                compositeBit.append(np.multipl(nodeData[i], nodeCarrierSignal))

    freq = 2
    # x = 3 * np.sin(2 * np.pi * freq * t)
    x = 1 * np.sin(2 * np.pi * freq * t)
    composite = np.multiply(subCarrierBinary40ByteDataList[0][0], x)

    freq = 4
    # x += np.sin(2 * np.pi * freq * t)
    x = np.sin(2 * np.pi * freq * t)
    composite += np.multiply(subCarrierBinary40ByteDataList[1][0], x)

    freq = 6
    # x += 0.5 * np.sin(2 * np.pi * freq * t)
    x = 1 * np.sin(2 * np.pi * freq * t)
    composite += np.multiply(subCarrierBinary40ByteDataList[2][0], x)

    plt.figure(figsize=(8, 6))
    # plt.plot(t, x, 'r')
    plt.plot(t, composite, 'r')
    plt.ylabel('Amplitude')

    plt.show()
    # return x
    return composite

def performFFT(x):
    sr = 320
    X = fft(x)
    N = len(X)
    n = np.arange(N)
    T = N / sr
    freq = n / T

    # sampling interval
    ts = 1.0 / sr
    t = np.arange(0, 1, ts)

    plt.figure(figsize=(12, 6))
    plt.subplot(121)

    plt.stem(freq, np.abs(X), 'b', markerfmt=" ", basefmt="-b")
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude |X(freq)|')
    plt.xlim(0, 10)

    plt.subplot(122)
    plt.plot(t, ifft(X), 'r')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

def fft2():
    # Python example - Fourier transform using numpy.fft method
    import numpy as np
    import matplotlib.pyplot as plotter

    # How many time points are needed i,e., Sampling Frequency
    # samplingFrequency = 100
    # samplingFrequency = 32
    # samplingFrequency = 13
    # samplingFrequency = 1200
    samplingFrequency = 1100

    # At what intervals time points are sampled
    samplingInterval = 1 / samplingFrequency

    # Begin time period of the signals
    beginTime = 0

    # End time period of the signals
    # endTime = 10
    endTime = 24.6

    # Frequency of the signals
    # signal1Frequency = 3
    signal1Frequency = 400

    # signal2Frequency = 4
    signal2Frequency = 500

    # Time points
    # time = np.arange(beginTime, endTime, samplingInterval)
    time = np.arange(beginTime, samplingInterval * len(subCarrierBinary40ByteDataList[0][0]) + beginTime,
                     samplingInterval)

    # Create two sine waves
    amplitude1 = np.sin(2 * np.pi * signal1Frequency * time)
    amplitude1 = np.multiply(subCarrierBinary40ByteDataList[1][0], amplitude1)
    # d1 = subCarrierBinary40ByteDataList[1][0]
    # d1 = [i * 2 - 1 for i in d1]
    # amplitude1 = np.multiply(d1, amplitude1)

    amplitude2 = np.sin(2 * np.pi * signal2Frequency * time)
    amplitude2 = np.multiply(subCarrierBinary40ByteDataList[0][0], amplitude2)

    # Create subplot
    figure, axis = plotter.subplots(4, 1)
    plotter.subplots_adjust(hspace=1)

    # Time domain representation for sine wave 1
    axis[0].set_title('Sine wave with a frequency of 4 Hz')
    axis[0].plot(time, amplitude1)
    axis[0].set_xlabel('Time')
    axis[0].set_ylabel('Amplitude')

    # Time domain representation for sine wave 2

    axis[1].set_title('Sine wave with a frequency of 7 Hz')
    axis[1].plot(time, amplitude2)
    axis[1].set_xlabel('Time')
    axis[1].set_ylabel('Amplitude')

    # Add the sine waves
    amplitude = amplitude1 + amplitude2
    # amplitude = amplitude1

    # Time domain representation of the resultant sine wave
    axis[2].set_title('Sine wave with multiple frequencies')
    axis[2].plot(time, amplitude)
    axis[2].set_xlabel('Time')
    axis[2].set_ylabel('Amplitude')

    # Frequency domain representation
    fourierTransform = np.fft.fft(amplitude) / len(amplitude)  # Normalize amplitude
    # fourierTransform = np.fft.fft(amplitude) / 64 # Normalize amplitude

    fourierTransform = fourierTransform[range(int(len(amplitude) / 2))]  # Exclude sampling frequency

    tpCount = len(amplitude)
    tpCountHalf = int(tpCount / 2)

    values = np.arange(int(tpCount / 2))

    # if tpCountHalf <= 208:  # (541 - 528)/0.040625
    #     tpCountHalf = 208
    # values = np.arange(tpCountHalf)
    timePeriod = tpCount / samplingFrequency
    # timePeriod = tpCountHalf / samplingFrequency

    frequencies = values / timePeriod
    frequencies2 = frequencies + 528

    axis[3].set_title('Fourier transform depicting the frequency components')
    axis[3].plot(frequencies, abs(fourierTransform))
    axis[3].set_xlabel('Frequency')
    axis[3].set_ylabel('Amplitude')
    plotter.show()


# forGlobal = np.zeros(320)
# signal = buildSignal()
# forGlobal[2] = signal[2]
# performFFT(signal)
# # performFFT(forGlobal)

fft2()