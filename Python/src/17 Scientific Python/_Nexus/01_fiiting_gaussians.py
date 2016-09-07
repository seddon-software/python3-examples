import scisoftpy as dnp

hdf5FileName = '/Users/seddon/home/workspace/Python/Python/src/Scientific Python/HDF5/14763.dat'
hdf5FileName = '14763.dat'

data = dnp.io.load(hdf5FileName)
print data
print data.keys()

dnp.plot.setdefname('Gaussian Fit')
x = data['gonx'][200:-201]
y = data['i_pin'][200:-200]
dy = dnp.diff(y)
dnp.plot.line(x, dy)

g = dnp.fit.function.gaussian
peak = -1.3
fwhm = 0.05
area = 0.001
initial_guess = (peak, fwhm, area)
# fitResult = dnp.fit.fit(g, x, dy, initial_guess, optimizer='local')
# fitResult.plot()

peakMin = -1.3
peakMax = -0.8
fwhmMin = 0.02
fwhmMax = 2.0
areaMin = 0.001
areaMax = 0.01
mybounds = [(peakMin,peakMax),(fwhmMin,fwhmMax),(areaMin,areaMax)]
fitResult = dnp.fit.fit(g, x, dy, initial_guess, bounds=mybounds, optimizer='global')
fitResult.plot()
print fitResult.parameters

print dnp.fit.fit.__doc__
