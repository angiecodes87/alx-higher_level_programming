#include "Python.h"

/**
 * print_python_string_info - Prints information about a Python string object.
 * @p: A PyObject representing a string.
 */
void print_python_string_info(PyObject *p)
{
    long int length;

    fflush(stdout);

    // Print information about the Python string object
    printf("[.] String Object Info\n");

    // Check if the object is a valid string
    if (strcmp(p->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    // Get the length of the string
    length = PyUnicode_GET_LENGTH(p);

    // Determine the type of the string (compact ASCII or Unicode)
    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        printf("  Type: Compact ASCII\n");
    }
    else
    {
        printf("  Type: Compact Unicode Object\n");
    }

    // Print the length and value of the string
    printf("  Length: %ld\n", length);
    printf("  Value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
