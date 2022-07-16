#include <stdio.h>
#include <linux/sockios.h>
#include <linux/if.h>
#include "ioc.h"

int
main (int argc, char *argv[])
{
    printf("SIOCADDRT 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCADDRT"), 0x890B);
    printf("SIOCDELRT 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCDELRT"), 0x890C);
    printf("SIOCRTMSG 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCRTMSG"), 0x890D);
    printf("SIOCGIFNAME 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFNAME"), 0x8910);
    printf("SIOCSIFLINK 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFLINK"), 0x8911);
    printf("SIOCGIFCONF 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFCONF"), 0x8912);
    printf("SIOCGIFFLAGS 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFFLAGS"), 0x8913);
    printf("SIOCSIFFLAGS 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFFLAGS"), 0x8914);
    printf("SIOCGIFADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFADDR"), 0x8915);
    printf("SIOCSIFADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFADDR"), 0x8916);
    printf("SIOCGIFDSTADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFDSTADDR"), 0x8917);
    printf("SIOCSIFDSTADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFDSTADDR"), 0x8918);
    printf("SIOCGIFBRDADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFBRDADDR"), 0x8919);
    printf("SIOCSIFBRDADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFBRDADDR"), 0x891a);
    printf("SIOCGIFNETMASK 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFNETMASK"), 0x891b);
    printf("SIOCSIFNETMASK 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFNETMASK"), 0x891c);
    printf("SIOCGIFMETRIC 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFMETRIC"), 0x891d);
    printf("SIOCSIFMETRIC 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFMETRIC"), 0x891e);
    printf("SIOCGIFMEM 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFMEM"), 0x891f);
    printf("SIOCSIFMEM 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFMEM"), 0x8920);
    printf("SIOCGIFMTU 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFMTU"), 0x8921);
    printf("SIOCSIFMTU 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFMTU"), 0x8922);
    printf("SIOCSIFNAME 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFNAME"), 0x8923);
    printf("SIOCSIFHWADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFHWADDR"), 0x8924);
    printf("SIOCGIFENCAP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFENCAP"), 0x8925);
    printf("SIOCSIFENCAP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFENCAP"), 0x8926);
    printf("SIOCGIFHWADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFHWADDR"), 0x8927);
    printf("SIOCGIFSLAVE 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFSLAVE"), 0x8929);
    printf("SIOCSIFSLAVE 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFSLAVE"), 0x8930);
    printf("SIOCADDMULTI 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCADDMULTI"), 0x8931);
    printf("SIOCDELMULTI 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCDELMULTI"), 0x8932);
    printf("SIOCGIFINDEX 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFINDEX"), 0x8933);
    printf("SIOGIFINDEX 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOGIFINDEX"), SIOCGIFINDEX);
    printf("SIOCSIFPFLAGS 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFPFLAGS"), 0x8934);
    printf("SIOCGIFPFLAGS 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFPFLAGS"), 0x8935);
    printf("SIOCDIFADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCDIFADDR"), 0x8936);
    printf("SIOCSIFHWBROADCAST 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFHWBROADCAST"), 0x8937);
    printf("SIOCGIFCOUNT 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFCOUNT"), 0x8938);
    printf("SIOCGIFBR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFBR"), 0x8940);
    printf("SIOCSIFBR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFBR"), 0x8941);
    printf("SIOCGIFTXQLEN 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFTXQLEN"), 0x8942);
    printf("SIOCSIFTXQLEN 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFTXQLEN"), 0x8943);
    printf("SIOCETHTOOL 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCETHTOOL"), 0x8946);
    printf("SIOCGMIIPHY 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGMIIPHY"), 0x8947);
    printf("SIOCGMIIREG 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGMIIREG"), 0x8948);
    printf("SIOCSMIIREG 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSMIIREG"), 0x8949);
    printf("SIOCWANDEV 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCWANDEV"), 0x894A);
    printf("SIOCOUTQNSD 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCOUTQNSD"), 0x894B);
    printf("SIOCGSKNS 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGSKNS"), 0x894C);
    printf("SIOCDARP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCDARP"), 0x8953);
    printf("SIOCGARP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGARP"), 0x8954);
    printf("SIOCSARP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSARP"), 0x8955);
    printf("SIOCDRARP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCDRARP"), 0x8960);
    printf("SIOCGRARP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGRARP"), 0x8961);
    printf("SIOCSRARP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSRARP"), 0x8962);
    printf("SIOCGIFMAP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFMAP"), 0x8970);
    printf("SIOCSIFMAP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFMAP"), 0x8971);
    printf("SIOCADDDLCI 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCADDDLCI"), 0x8980);
    printf("SIOCDELDLCI 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCDELDLCI"), 0x8981);
    printf("SIOCGIFVLAN 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGIFVLAN"), 0x8982);
    printf("SIOCSIFVLAN 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSIFVLAN"), 0x8983);
    printf("SIOCBONDENSLAVE 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBONDENSLAVE"), 0x8990);
    printf("SIOCBONDRELEASE 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBONDRELEASE"), 0x8991);
    printf("SIOCBONDSETHWADDR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBONDSETHWADDR"), 0x8992);
    printf("SIOCBONDSLAVEINFOQUERY 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBONDSLAVEINFOQUERY"), 0x8993);
    printf("SIOCBONDINFOQUERY 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBONDINFOQUERY"), 0x8994);
    printf("SIOCBONDCHANGEACTIVE 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBONDCHANGEACTIVE"), 0x8995);
    printf("SIOCBRADDBR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBRADDBR"), 0x89a0);
    printf("SIOCBRDELBR 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBRDELBR"), 0x89a1);
    printf("SIOCBRADDIF 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBRADDIF"), 0x89a2);
    printf("SIOCBRDELIF 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCBRDELIF"), 0x89a3);
    printf("SIOCSHWTSTAMP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCSHWTSTAMP"), 0x89b0);
    printf("SIOCGHWTSTAMP 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCGHWTSTAMP"), 0x89b1);
    printf("SIOCDEVPRIVATE 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCDEVPRIVATE"), 0x89F0);
    printf("SIOCPROTOPRIVATE 0x%x == 0x%x\n", ioc_macro_value("sockios", "SIOCPROTOPRIVATE"), 0x89E0);

    printf("sizeof(ifreq) %d == %d\n", ioc_struct_size("if", "ifreq"), sizeof(struct ifreq));
}
