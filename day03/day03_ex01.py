# -*- coding: utf-8 -*-
# Python 2.7.14
IP=  0xc0a80164  # IP:192.168.1.100
MASK=0xffffff00  # 子网掩码:255.255.255.0
Network_address=IP&MASK  # 网段地址:192.168.1.0
Broadcast_address=IP|~MASK  # 广播地址:192.168.1.255
print 'IP:%d.%d.%d.%d' %((IP&0xff000000)>>24,
                         (IP&0x00ff0000)>>16,
                         (IP&0x0000ff00)>>8,
                          IP&0xff)
print 'MASK:%d.%d.%d.%d' %((MASK&0xff000000)>>24,
                           (MASK&0x00ff0000)>>16,
                           (MASK&0x0000ff00)>>8,
                            MASK&0xff)
print 'Network_address:%d.%d.%d.%d' %((Network_address&0xff000000)>>24,
                                      (Network_address&0x00ff0000)>>16,
                                      (Network_address&0x0000ff00)>>8,
                                       Network_address&0x00)

print 'Broadcast_address:%d.%d.%d.%d' %((Broadcast_address&0xff000000)>>24,
                                        (Broadcast_address&0x00ff0000)>>16,
                                        (Broadcast_address&0x0000ff00)>>8,
                                         Broadcast_address&0xff)


