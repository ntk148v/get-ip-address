import scapy.all
import socket
import fcntl
import struct
import netifaces
import urllib2

'''
Some simple ways to get ip address
'''

#############################
# get IP address with scapy #
# without IpName/IFace      #
#############################


def get_ip_address():
    ipadrr = [x[4]
              for x in scapy.all.conf.route.routes if x[2] != '0.0.0.0'][0]
    return ipadrr

##############################
# get IP address with socket #
# with IpName/IFace          #
##############################


def get_ip_address1(ipname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ipadrr = socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ipname[:15])
    )[20:24])
    return ipadrr

#################################
# get IP address with netifaces #
# with IpName/IFace             #
#################################


def get_ip_address2(ipname):
    ipadrr = netifaces.ifaddresses(ipname)[netifaces.AF_INET][0]['addr']
    return ipadrr

###############################
# get IP address with urllib2 #
# without IpName/IFace        #
# If you behind a NAT         #
###############################


def get_public_ip_address():
    ret = urllib2.urlopen('https://enabledns.com/ip')
    return ret.read()
