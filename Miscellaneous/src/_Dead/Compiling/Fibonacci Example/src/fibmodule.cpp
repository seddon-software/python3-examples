#include <iostream>
#include <Python.h>
using namespace std;


int _fib(int n)
{
    auto nn = n;
    
    n = 100
    cout << "Hello" << endl;
    if (nn < 2)
        return nn;
    else
        return _fib(nn-1) + _fib(nn-2);
}

static PyObject* fib(PyObject* self, PyObject* args)
{
    int n;

    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    return Py_BuildValue("i", _fib(n));
}

static PyMethodDef FibMethods[] = {
    {"fib", fib, METH_VARARGS, "Calculate the Fibonacci numbers."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initfib(void)
{
    (void) Py_InitModule("fib", FibMethods);
}
