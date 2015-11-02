import scipy
import matplotlib.pyplot as plt
pi = scipy.pi

signal_length = 0.5     # [seconds]

sample_rate = 500       # sampling rate [Hz]
dt = 1.0/sample_rate    # time between two samples [s]
df = 1.0/signal_length  # frequency between points in
                        # in frequency domain [Hz]
t=scipy.arange(0,signal_length ,dt)     # the time vector

n_t=len(t)              # length of time vector i

# create signal
y= scipy.sin(2*pi*155*t+pi/3) + scipy.sin(2*pi*50*t) + scipy.sin(2*pi*70*t+pi/4)

# compute fourier transform
f=scipy.fft(y)

# work out meaningful frequencies in fourier transform
freqs=df*scipy.arange(0,(n_t-1)/2.,dtype='d')   # d=double precision float
n_freq=len(freqs)

# plot input data y against time
plt.subplot(2,1,1)
plt.plot(t,y,label='input data')
plt.xlabel('time [s]')
plt.ylabel('signal')

# plot frequency spectrum
plt.subplot(2,1,2)
plt.plot(freqs,abs(f[0:n_freq]),
             label='abs(fourier transform)')
plt.xlabel('frequency [Hz]')
plt.ylabel('abs(DFT(signal))')

# save plot to disk
plt.savefig('fft-results.pdf')
plt.show()      # and display plot on screen
