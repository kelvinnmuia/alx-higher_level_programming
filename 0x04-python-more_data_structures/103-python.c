#include <Python.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - prints python bytes info
 * @p: PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char sz, i;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("{.} bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf(" size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		sz = 10;
	else
		sz = ((PyVarObject *)p)->ob_size + 1;

	printf(" first %d bytes: ", sz);
	for (i = 0; i < sz; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}

}

/**
 * print_python_list - prints info about python lists
 * @p: python list pointer
 */
void print_python_list(PyObject *p)
{
	int i, alloc, sz;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	sz = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < sz; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}
