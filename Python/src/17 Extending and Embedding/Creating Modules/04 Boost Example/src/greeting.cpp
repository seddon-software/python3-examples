char const* greet()
{
   return "hello Chris";
}

double Average(double x, double y)
{
	return (x + y)/2.0;
}

#include <boost/python.hpp>

BOOST_PYTHON_MODULE(greeting)
{
    using namespace boost::python;
    def("greet", greet);
    def("average", Average);
}
