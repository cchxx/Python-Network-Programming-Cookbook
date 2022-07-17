#include <stdlib.h>
#include "ioc.h"

int debug_flag = 0;

static void
load_debug_config ()
{
    if (NULL != getenv("DEBUG_IOC")) {
        debug_flag = 1;
    } else {
        debug_flag = 0;
    }
}
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
            DBG("\t%s ( %s, %s ), hit\n", __func__, module, target);
            return table->func(target);
        }
        table++;
    }
    return -1;
}

int
ioc_struct_size (char *module_name, char *struct_name)
{
    load_debug_config();
    DBG("%s ( %s, %s )\n", __func__, module_name, struct_name);
    return run_module_function(struct_funcs, module_name, struct_name);
}

int
ioc_macro_value (char *module_name, char *macro_name)
{
    load_debug_config();
    DBG("%s ( %s, %s )\n", __func__, module_name, macro_name);
    return run_module_function(macro_funcs, module_name, macro_name);
}
