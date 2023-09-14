#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_bytes - python function to print python bytes
 * @p: print python bytes
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *byte_obj;
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	byte_obj = (PyBytesObject *)p;
	size = PyBytes_GET_SIZE(byte_obj);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", byte_obj->ob_sval);

	printf("  first %ld bytes: ", (size < 10 ? size : 10));
	for (i = 0; i < (size < 10 ? size : 10); i++)
		printf("%02x%c", byte_obj->ob_sval[i], i == 9 ? '\n' : ' ');
}
/**
 * print_python_list - python function to print python list
 * @p: print python list pointer
 */

void print_python_list(PyObject *p)
{
	PyListObject *list_obj;
	Py_ssize_t size, i;

	printf("[*] Python list info\n");

	if (!PyList_CheckExact(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	list_obj = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list_obj->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_CheckExact(item))
			print_python_bytes(item);
	}
}
