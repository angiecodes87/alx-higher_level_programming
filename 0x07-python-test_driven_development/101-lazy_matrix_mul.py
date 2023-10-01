#include "Python.h"

/**
 * print_python_string - Displays information about Python strings.
 * @p: A PyObject representing a string.
 */
void print_python_string(PyObject *p)
{
    long int length;

    fflush(stdout);

    printf("[.] Information about the string object\n");
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
