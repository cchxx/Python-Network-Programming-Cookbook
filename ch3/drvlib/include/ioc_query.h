#ifndef __IOC_QUERY_H__
#define __IOC_QUERY_H__

struct ioc_map {
    char * name;
    int code;
};

extern int ioc_query_sockios(char *sioc_name);

#endif  /* __IOC_QUERY_H__ */