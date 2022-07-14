#include <stdio.h>
#include <linux/sockios.h>
#include "ioc_query.h"

int
main (int argc, char *argv[])
{
    printf("SIOCADDRT 0x%x == 0x%x\n", ioc_query_sockios("SIOCADDRT"), 0x890B);
    printf("SIOCDELRT 0x%x == 0x%x\n", ioc_query_sockios("SIOCDELRT"), 0x890C);
    printf("SIOCRTMSG 0x%x == 0x%x\n", ioc_query_sockios("SIOCRTMSG"), 0x890D);
    printf("SIOCGIFNAME 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFNAME"), 0x8910);
    printf("SIOCSIFLINK 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFLINK"), 0x8911);
    printf("SIOCGIFCONF 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFCONF"), 0x8912);
    printf("SIOCGIFFLAGS 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFFLAGS"), 0x8913);
    printf("SIOCSIFFLAGS 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFFLAGS"), 0x8914);
    printf("SIOCGIFADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFADDR"), 0x8915);
    printf("SIOCSIFADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFADDR"), 0x8916);
    printf("SIOCGIFDSTADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFDSTADDR"), 0x8917);
    printf("SIOCSIFDSTADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFDSTADDR"), 0x8918);
    printf("SIOCGIFBRDADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFBRDADDR"), 0x8919);
    printf("SIOCSIFBRDADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFBRDADDR"), 0x891a);
    printf("SIOCGIFNETMASK 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFNETMASK"), 0x891b);
    printf("SIOCSIFNETMASK 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFNETMASK"), 0x891c);
    printf("SIOCGIFMETRIC 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFMETRIC"), 0x891d);
    printf("SIOCSIFMETRIC 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFMETRIC"), 0x891e);
    printf("SIOCGIFMEM 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFMEM"), 0x891f);
    printf("SIOCSIFMEM 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFMEM"), 0x8920);
    printf("SIOCGIFMTU 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFMTU"), 0x8921);
    printf("SIOCSIFMTU 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFMTU"), 0x8922);
    printf("SIOCSIFNAME 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFNAME"), 0x8923);
    printf("SIOCSIFHWADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFHWADDR"), 0x8924);
    printf("SIOCGIFENCAP 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFENCAP"), 0x8925);
    printf("SIOCSIFENCAP 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFENCAP"), 0x8926);
    printf("SIOCGIFHWADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFHWADDR"), 0x8927);
    printf("SIOCGIFSLAVE 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFSLAVE"), 0x8929);
    printf("SIOCSIFSLAVE 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFSLAVE"), 0x8930);
    printf("SIOCADDMULTI 0x%x == 0x%x\n", ioc_query_sockios("SIOCADDMULTI"), 0x8931);
    printf("SIOCDELMULTI 0x%x == 0x%x\n", ioc_query_sockios("SIOCDELMULTI"), 0x8932);
    printf("SIOCGIFINDEX 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFINDEX"), 0x8933);
    printf("SIOGIFINDEX 0x%x == 0x%x\n", ioc_query_sockios("SIOGIFINDEX"), SIOCGIFINDEX);
    printf("SIOCSIFPFLAGS 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFPFLAGS"), 0x8934);
    printf("SIOCGIFPFLAGS 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFPFLAGS"), 0x8935);
    printf("SIOCDIFADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCDIFADDR"), 0x8936);
    printf("SIOCSIFHWBROADCAST 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFHWBROADCAST"), 0x8937);
    printf("SIOCGIFCOUNT 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFCOUNT"), 0x8938);
    printf("SIOCGIFBR 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFBR"), 0x8940);
    printf("SIOCSIFBR 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFBR"), 0x8941);
    printf("SIOCGIFTXQLEN 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFTXQLEN"), 0x8942);
    printf("SIOCSIFTXQLEN 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFTXQLEN"), 0x8943);
    printf("SIOCETHTOOL 0x%x == 0x%x\n", ioc_query_sockios("SIOCETHTOOL"), 0x8946);
    printf("SIOCGMIIPHY 0x%x == 0x%x\n", ioc_query_sockios("SIOCGMIIPHY"), 0x8947);
    printf("SIOCGMIIREG 0x%x == 0x%x\n", ioc_query_sockios("SIOCGMIIREG"), 0x8948);
    printf("SIOCSMIIREG 0x%x == 0x%x\n", ioc_query_sockios("SIOCSMIIREG"), 0x8949);
    printf("SIOCWANDEV 0x%x == 0x%x\n", ioc_query_sockios("SIOCWANDEV"), 0x894A);
    printf("SIOCOUTQNSD 0x%x == 0x%x\n", ioc_query_sockios("SIOCOUTQNSD"), 0x894B);
    printf("SIOCGSKNS 0x%x == 0x%x\n", ioc_query_sockios("SIOCGSKNS"), 0x894C);
    printf("SIOCDARP 0x%x == 0x%x\n", ioc_query_sockios("SIOCDARP"), 0x8953);
    printf("SIOCGARP 0x%x == 0x%x\n", ioc_query_sockios("SIOCGARP"), 0x8954);
    printf("SIOCSARP 0x%x == 0x%x\n", ioc_query_sockios("SIOCSARP"), 0x8955);
    printf("SIOCDRARP 0x%x == 0x%x\n", ioc_query_sockios("SIOCDRARP"), 0x8960);
    printf("SIOCGRARP 0x%x == 0x%x\n", ioc_query_sockios("SIOCGRARP"), 0x8961);
    printf("SIOCSRARP 0x%x == 0x%x\n", ioc_query_sockios("SIOCSRARP"), 0x8962);
    printf("SIOCGIFMAP 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFMAP"), 0x8970);
    printf("SIOCSIFMAP 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFMAP"), 0x8971);
    printf("SIOCADDDLCI 0x%x == 0x%x\n", ioc_query_sockios("SIOCADDDLCI"), 0x8980);
    printf("SIOCDELDLCI 0x%x == 0x%x\n", ioc_query_sockios("SIOCDELDLCI"), 0x8981);
    printf("SIOCGIFVLAN 0x%x == 0x%x\n", ioc_query_sockios("SIOCGIFVLAN"), 0x8982);
    printf("SIOCSIFVLAN 0x%x == 0x%x\n", ioc_query_sockios("SIOCSIFVLAN"), 0x8983);
    printf("SIOCBONDENSLAVE 0x%x == 0x%x\n", ioc_query_sockios("SIOCBONDENSLAVE"), 0x8990);
    printf("SIOCBONDRELEASE 0x%x == 0x%x\n", ioc_query_sockios("SIOCBONDRELEASE"), 0x8991);
    printf("SIOCBONDSETHWADDR 0x%x == 0x%x\n", ioc_query_sockios("SIOCBONDSETHWADDR"), 0x8992);
    printf("SIOCBONDSLAVEINFOQUERY 0x%x == 0x%x\n", ioc_query_sockios("SIOCBONDSLAVEINFOQUERY"), 0x8993);
    printf("SIOCBONDINFOQUERY 0x%x == 0x%x\n", ioc_query_sockios("SIOCBONDINFOQUERY"), 0x8994);
    printf("SIOCBONDCHANGEACTIVE 0x%x == 0x%x\n", ioc_query_sockios("SIOCBONDCHANGEACTIVE"), 0x8995);
    printf("SIOCBRADDBR 0x%x == 0x%x\n", ioc_query_sockios("SIOCBRADDBR"), 0x89a0);
    printf("SIOCBRDELBR 0x%x == 0x%x\n", ioc_query_sockios("SIOCBRDELBR"), 0x89a1);
    printf("SIOCBRADDIF 0x%x == 0x%x\n", ioc_query_sockios("SIOCBRADDIF"), 0x89a2);
    printf("SIOCBRDELIF 0x%x == 0x%x\n", ioc_query_sockios("SIOCBRDELIF"), 0x89a3);
    printf("SIOCSHWTSTAMP 0x%x == 0x%x\n", ioc_query_sockios("SIOCSHWTSTAMP"), 0x89b0);
    printf("SIOCGHWTSTAMP 0x%x == 0x%x\n", ioc_query_sockios("SIOCGHWTSTAMP"), 0x89b1);
    printf("SIOCDEVPRIVATE 0x%x == 0x%x\n", ioc_query_sockios("SIOCDEVPRIVATE"), 0x89F0);
    printf("SIOCPROTOPRIVATE 0x%x == 0x%x\n", ioc_query_sockios("SIOCPROTOPRIVATE"), 0x89E0);
}
