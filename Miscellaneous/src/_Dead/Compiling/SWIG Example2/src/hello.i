%module example
%{
#include "example.h"
%}

%include "std_vector.i"
// Instantiate templates used by example
namespace std {
   %template(IntVector) vector<int>;
   %template(DoubleVector) vector<double>;
}

// Include the header file with above prototypes
%include "example.h"
