#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pdb
import sys
import socket
import fcntl
import struct
import array
import ctypes

drvlib = ctypes.CDLL('/usr/local/lib/libioc.so')

#
# SIOCGIFCONF = 0x8912    # from C lib sockios.h
# build and install ch3/drvlib, and then get value runtime
#
SIOCGIFCONF = drvlib.ioc_macro_value(
    ctypes.c_char_p(
        'sockios'.encode('utf-8')),
    ctypes.c_char_p(
        'SIOCGIFCONF'.encode('utf-8')))

STRUCT_SIZE_IFREQ = drvlib.ioc_struct_size(
    ctypes.c_char_p(
        'if'.encode('utf-8')),
    ctypes.c_char_p(
        'ifreq'.encode('utf-8')))

IFNAMSIZ = drvlib.ioc_struct_size(
    ctypes.c_char_p(
        'if'.encode('utf-8')),
    ctypes.c_char_p(
        'IFNAMSIZ'.encode('utf-8')))

STRUCT_SIZE_32 = 32
STRUCT_SIZE_64 = 64
PLATFORM_32_MAX_NUMBER = 2 ** 32
DEFAULT_INTERFACES = 8


def list_interfaces():
    interfaces = []
    max_interfaces = DEFAULT_INTERFACES
    is_64bits = sys.maxsize > PLATFORM_32_MAX_NUMBER
    struct_size = STRUCT_SIZE_64 if is_64bits else STRUCT_SIZE_32
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        bytes = max_interfaces * struct_size
        interface_names = array.array('B', [0] * bytes)
        '''
        Returns configuration information for all the interfaces that are
        configured on the system.

            ioctl(fd, SIOCGIFCONF, (caddr_t)&ifc);
            struct ifconf ifc;

            struct ifconf  {
                int	ifc_len;			/* size of buffer	*/
                union {
                    char __user *ifcu_buf;
                    struct ifreq __user *ifcu_req;
                } ifc_ifcu;
            };

        The configuration information is returned in a list of ifreq structures

            struct ifreq {
            #define IFHWADDRLEN	6
                union
                {
                    char	ifrn_name[IFNAMSIZ];		/* if name, e.g. "en0" */
                } ifr_ifrn;

                union {
                    struct	sockaddr ifru_addr;
                    struct	sockaddr ifru_dstaddr;
                    struct	sockaddr ifru_broadaddr;
                    struct	sockaddr ifru_netmask;
                    struct  sockaddr ifru_hwaddr;
                    short	ifru_flags;
                    int	ifru_ivalue;
                    int	ifru_mtu;
                    struct  ifmap ifru_map;
                    char	ifru_slave[IFNAMSIZ];	/* Just fits the size */
                    char	ifru_newname[IFNAMSIZ];
                    void __user *	ifru_data;
                    struct	if_settings ifru_settings;
                } ifr_ifru;
            };

        Note:
        pointed to by the ifc.ifc_req field, with one ifreq structure per interface
        The caller of the ioctl command must allocate sufficient space to store
        the configuration information, returned as a list of ifreq structures
        for all of the interfaces that are configured on the system. For example,
        if n interfaces are configured on the system, ifc.ifc_req must point to
        {n * sizeof (struct ifreq)} bytes of space allocated
        '''
        sock_info = fcntl.ioctl(
            sock.fileno(), SIOCGIFCONF, struct.pack(
                'iL', bytes, interface_names.buffer_info()[0]))
        outbytes = struct.unpack('iL', sock_info)[0]
        if outbytes == bytes:
            max_interfaces *= 2
        else:
            break
    '''
    import hexdump; hexdump.hexdump(interface_names)
    00000000: 6C 6F 00 00 00 00 00 00  00 00 00 00 00 00 00 00  lo..............
    00000010: 02 00 00 00 7F 00 00 01  00 00 00 00 00 00 00 00  ................
    00000020: 00 00 00 00 00 00 00 00  65 74 68 30 00 00 00 00  ........eth0....
    00000030: 00 00 00 00 00 00 00 00  02 00 00 00 AC 11 00 02  ................
    00000040: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
    ... omitted ...
    '''
    namestr = interface_names.tostring()
    for i in range(0, outbytes, STRUCT_SIZE_IFREQ):
        interfaces.append((namestr[i:i + IFNAMSIZ].split(b'\x00', 1)[0]))
    return interfaces


if __name__ == '__main__':
    interfaces = list_interfaces()
    print(
        'This machine has {} network interfaces: {}.'.format(
            len(interfaces),
            interfaces))
