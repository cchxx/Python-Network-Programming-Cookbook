#include <linux/if.h>
#include "ioc.h"

static struct ioc_map struct_map[] = {
    { "ifreq",  sizeof(struct ifreq) },
    { NULL,     0                    }
};

static struct ioc_map macro_map[] = {
    { "IFNAMSIZ", IFNAMSIZ },
    { NULL,       0        }
};

int
ioc_struct_size_if (char *struct_name)
{
    return query_map(struct_map, struct_name);
}


int
ioc_macro_value_if (char *macro_name)
{
    return query_map(macro_map, macro_name);
}
