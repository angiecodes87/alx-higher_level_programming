#include "Python.h"

/**
 * print_python_string_info - Prints information about a Python string object.
 * @p: A PyObject representing a string.
 */
void print_python_string_info(PyObject *p)
{
    long int length;

    fflush(stdout);

    printf("[.] String Object Info\n");
    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = ((PyASCIIObject *)(p))->length;

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  Type: Compact ASCII\n");
    else
        printf("  Type: Compact Unicode Object\n");
    
    printf("  Length: %ld\n", length);
    printf("  Value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
