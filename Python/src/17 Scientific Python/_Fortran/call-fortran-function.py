
print "importing Fortran shared object ..."
import fortran_lib

print "calling Fortran library function ..."
print fortran_lib.square(12)
