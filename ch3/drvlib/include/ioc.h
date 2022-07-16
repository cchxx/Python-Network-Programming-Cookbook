#ifndef __IOC_H__
#define __IOC_H__

#include <string.h>

struct ioc_map {
    char * name;
    int value;
};

static inline int
query_map (struct ioc_map *map, char *name)
{
    while ((map != NULL) && (map->name != NULL)) {
        if (0 == strncmp(name, map->name, strlen(map->name))) {
            return map->value;
        }
        map++;
    }
    return -1;
}

extern int ioc_macro_value_sockios(char *sioc_name);
extern int ioc_macro_value_if(char *macro_name);
extern int ioc_struct_size_if(char *struct_name);

extern int ioc_macro_value(char *module_name, char *macro_name);
extern int ioc_struct_size(char *module_name, char *struct_name);


#endif  /* __IOC_H__ */