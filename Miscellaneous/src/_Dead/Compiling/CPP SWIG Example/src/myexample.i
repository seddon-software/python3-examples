%module myexample



%include "std_vector.i"
namespace std {
   %template(IntVector) vector<int>;
   %template(DoubleVector) vector<double>;
};

%{
#define SWIG_FILE_WITH_INIT
#include "hello.h"
#include "average.hpp"
%}

int average(std::vector<int> v);
double average2(std::vector<double> v);


//void say_hello(const char* name);
//void say_goodbye(const char* name);

%include "hello.h"
%include "average.hpp"
