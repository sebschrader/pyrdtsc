#include <Python.h>

#if defined(__i386__)

static __inline__ unsigned long long _rdtsc(void)
{
    unsigned long long int x;
    __asm__ volatile (".byte 0x0f, 0x31" : "=A" (x));
    return x;
}

#elif defined(__x86_64__)

static __inline__ unsigned long long _rdtsc(void)
{
    unsigned hi, lo;
    __asm__ __volatile__ ("rdtsc" : "=a"(lo), "=d"(hi));
    return ( (unsigned long long)lo)|( ((unsigned long long)hi)<<32 );
}

#endif

static PyObject *
rdtsc(PyObject *self, PyObject *args)
{
    assert(args == NULL);
    return PyLong_FromUnsignedLongLong(_rdtsc());
}


static PyMethodDef arpreq_methods[] = {
    {"rdtsc", rdtsc, METH_NOARGS, "Read the cycle count with the rdtsc instruction"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT,
        "rdtsc",
        "Read the cycle count with rdtsc instruction",
        0,
        arpreq_methods,
        NULL,
        NULL,
        NULL,
        NULL,
};


PyMODINIT_FUNC
PyInit_rdtsc(void)
{
    return PyModuleDef_Init(&moduledef);
}
