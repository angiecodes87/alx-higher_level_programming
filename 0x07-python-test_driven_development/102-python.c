#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    PyUnicodeObject *str = (PyUnicodeObject *)p;
    Py_ssize_t length = PyUnicode_GET_LENGTH(str);
    const char *value = PyUnicode_AsUTF8(str);

    printf("[.] string object info\n");
    if (PyUnicode_IS_COMPACT_ASCII(str))
    {
        printf("  type: compact ascii\n");
    }
    else
    {
        printf("  type: compact unicode object\n");
    }

    printf("  length: %ld\n", length);
    printf("  value: %s\n", value);
}
