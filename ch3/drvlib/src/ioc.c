#include "ioc.h"


struct module_func_tbl {
    char * mod;
    int (*func)(char *);
};

static struct module_func_tbl macro_funcs[] = {
    { "sockios", ioc_macro_value_sockios },
    { "if",      ioc_macro_value_if      },
    { NULL,      NULL                    }
};

static struct module_func_tbl struct_funcs[] = {
    { "if",      ioc_struct_size_if },
    { NULL,      NULL               }
};

static inline int
run_module_function (struct module_func_tbl *table, char *module, char *target)
{
    while ((table != NULL) && (table->mod != NULL)) {
        if (0 == strncmp(module, table->mod, strlen(table->mod))) {
            return table->func(target);
        }
        table++;
    }
    return -1;
}

int
ioc_struct_size (char *module_name, char *struct_name)
{
    return run_module_function(struct_funcs, module_name, struct_name);
}

int
ioc_macro_value (char *module_name, char *macro_name)
{
    return run_module_function(macro_funcs, module_name, macro_name);
}
