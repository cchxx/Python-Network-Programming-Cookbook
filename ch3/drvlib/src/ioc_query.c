#include <stdio.h>
#include <linux/sockios.h>
#include <string.h>
#include "ioc_query.h"


static struct ioc_map sockios_maps[] = {
    { "SIOCADDRT",              SIOCADDRT              },
    { "SIOCDELRT",              SIOCDELRT              },
    { "SIOCRTMSG",              SIOCRTMSG              },
    { "SIOCGIFNAME",            SIOCGIFNAME            },
    { "SIOCSIFLINK",            SIOCSIFLINK            },
    { "SIOCGIFCONF",            SIOCGIFCONF            },
    { "SIOCGIFFLAGS",           SIOCGIFFLAGS           },
    { "SIOCSIFFLAGS",           SIOCSIFFLAGS           },
    { "SIOCGIFADDR",            SIOCGIFADDR            },
    { "SIOCSIFADDR",            SIOCSIFADDR            },
    { "SIOCGIFDSTADDR",         SIOCGIFDSTADDR         },
    { "SIOCSIFDSTADDR",         SIOCSIFDSTADDR         },
    { "SIOCGIFBRDADDR",         SIOCGIFBRDADDR         },
    { "SIOCSIFBRDADDR",         SIOCSIFBRDADDR         },
    { "SIOCGIFNETMASK",         SIOCGIFNETMASK         },
    { "SIOCSIFNETMASK",         SIOCSIFNETMASK         },
    { "SIOCGIFMETRIC",          SIOCGIFMETRIC          },
    { "SIOCSIFMETRIC",          SIOCSIFMETRIC          },
    { "SIOCGIFMEM",             SIOCGIFMEM             },
    { "SIOCSIFMEM",             SIOCSIFMEM             },
    { "SIOCGIFMTU",             SIOCGIFMTU             },
    { "SIOCSIFMTU",             SIOCSIFMTU             },
    { "SIOCSIFNAME",            SIOCSIFNAME            },
    { "SIOCSIFHWADDR",          SIOCSIFHWADDR          },
    { "SIOCGIFENCAP",           SIOCGIFENCAP           },
    { "SIOCSIFENCAP",           SIOCSIFENCAP           },
    { "SIOCGIFHWADDR",          SIOCGIFHWADDR          },
    { "SIOCGIFSLAVE",           SIOCGIFSLAVE           },
    { "SIOCSIFSLAVE",           SIOCSIFSLAVE           },
    { "SIOCADDMULTI",           SIOCADDMULTI           },
    { "SIOCDELMULTI",           SIOCDELMULTI           },
    { "SIOCGIFINDEX",           SIOCGIFINDEX           },
    { "SIOGIFINDEX",            SIOGIFINDEX            },
    { "SIOCSIFPFLAGS",          SIOCSIFPFLAGS          },
    { "SIOCGIFPFLAGS",          SIOCGIFPFLAGS          },
    { "SIOCDIFADDR",            SIOCDIFADDR            },
    { "SIOCSIFHWBROADCAST",     SIOCSIFHWBROADCAST     },
    { "SIOCGIFCOUNT",           SIOCGIFCOUNT           },
    { "SIOCGIFBR",              SIOCGIFBR              },
    { "SIOCSIFBR",              SIOCSIFBR              },
    { "SIOCGIFTXQLEN",          SIOCGIFTXQLEN          },
    { "SIOCSIFTXQLEN",          SIOCSIFTXQLEN          },
    { "SIOCETHTOOL",            SIOCETHTOOL            },
    { "SIOCGMIIPHY",            SIOCGMIIPHY            },
    { "SIOCGMIIREG",            SIOCGMIIREG            },
    { "SIOCSMIIREG",            SIOCSMIIREG            },
    { "SIOCWANDEV",             SIOCWANDEV             },
    { "SIOCOUTQNSD",            SIOCOUTQNSD            },
    { "SIOCGSKNS",              SIOCGSKNS              },
    { "SIOCDARP",               SIOCDARP               },
    { "SIOCGARP",               SIOCGARP               },
    { "SIOCSARP",               SIOCSARP               },
    { "SIOCDRARP",              SIOCDRARP              },
    { "SIOCGRARP",              SIOCGRARP              },
    { "SIOCSRARP",              SIOCSRARP              },
    { "SIOCGIFMAP",             SIOCGIFMAP             },
    { "SIOCSIFMAP",             SIOCSIFMAP             },
    { "SIOCADDDLCI",            SIOCADDDLCI            },
    { "SIOCDELDLCI",            SIOCDELDLCI            },
    { "SIOCGIFVLAN",            SIOCGIFVLAN            },
    { "SIOCSIFVLAN",            SIOCSIFVLAN            },
    { "SIOCBONDENSLAVE",        SIOCBONDENSLAVE        },
    { "SIOCBONDRELEASE",        SIOCBONDRELEASE        },
    { "SIOCBONDSETHWADDR",      SIOCBONDSETHWADDR      },
    { "SIOCBONDSLAVEINFOQUERY", SIOCBONDSLAVEINFOQUERY },
    { "SIOCBONDINFOQUERY",      SIOCBONDINFOQUERY      },
    { "SIOCBONDCHANGEACTIVE",   SIOCBONDCHANGEACTIVE   },
    { "SIOCBRADDBR",            SIOCBRADDBR            },
    { "SIOCBRDELBR",            SIOCBRDELBR            },
    { "SIOCBRADDIF",            SIOCBRADDIF            },
    { "SIOCBRDELIF",            SIOCBRDELIF            },
    { "SIOCSHWTSTAMP",          SIOCSHWTSTAMP          },
    { "SIOCGHWTSTAMP",          SIOCGHWTSTAMP          },
    { "SIOCDEVPRIVATE",         SIOCDEVPRIVATE         },
    { "SIOCPROTOPRIVATE",       SIOCPROTOPRIVATE       },
    { NULL,                     (int)NULL              }
};


int
ioc_query_sockios (char *sioc_name)
{
    struct ioc_map *map = sockios_maps;
    while ((map != NULL) && (map->name != NULL)) {
        if (0 == strncmp(sioc_name, map->name, strlen(map->name))) {
            return map->code;
        }
        map++;
    }
    return -1;
}
