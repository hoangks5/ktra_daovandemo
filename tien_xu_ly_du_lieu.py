import os
from nltk import sent_tokenize
import re
import json

from nltk.data import load
def __read_forlder__(): # Hàm đọc tên file trong thư mục
    os.chdir('data') # Tên thư mục chứa file txt original
    list = os.listdir() # Trả về list các file trong thư mục
    return list
    # print(list)
    # Kết quả : ['3D printing original.txt', 'Accelerated graphics original.txt', 'Active user original.txt', 'ADSL original.txt', 'Agile software development original.txt', 
    # 'Analog computer original.txt', 'Analytical engine original.txt', 'Antic original.txt', 'Arinc original.txt', 'Aritificial Intelligence original.txt', 
    # 'Asymmetric digital subscriber line original.txt', 'Big data original.txt', 'Bluetooth lower energy beacon original.txt', 'Bluetooth lower energy original.txt', 'Bluetooth original.txt',
    #  'Canonicalization original .txt', 'Capitalization of Internet .txt', 'Clariion original.txt', 'Client to client protocol original.txt', 'Clone original.txt', '
    # Color graphic adapter original .txt', 'Commodore datasette original.txt', 'Computer display standard original.txt', 'Computer_hardware1.txt', 'Computer_programming1.txt', 
    # 'Computer_security1.txt', 'Computer_virus1.txt', 'Cost_per_mille1.txt', 'Crowdfunding1.txt', 'CTIA and GTIA original.txt', 'Custom_software1.txt', 'Cyber-collection1.txt', 
    # 'Cyberstalking1.txt', 'Cyberwarfare1.txt', 'Dark_web1.txt', 'Data_stream1.txt', 'Dell_EMC_Unity1.txt', 'Digital_Revolution1.txt', 'Direct-access_storage_device1.txt', 
    # 'Direct_Client-to-Client1.txt', 'Discoverability1.txt', 'Domain_Name_System-based_blackhole_list1.txt', 'Enterprise_resource_planning.txt', 'Ethernet original.txt', 
    # 'Fibre channel original.txt', 'Firewall.txt', 'Fixed mobile convergence original.txt', 'Graphics display resolution original.txt', 'Group_coded.txt', 'HAcker.txt', '
    # Hardware.txt', 'HDMI original.txt', 'High_per.txt', 'Host_signal.txt', 'HPE_XP.txt', 'HP_7935.txt', 'HP_dc100.txt', 'HP_media.txt', 'HP_media_vault.txt', 'HP_memory.txt', 
    # 'HP_Storage.txt', 'HTML_email.txt', 'HTTP_404.txt', 'Hybird.txt', 'IBM_2361_large.txt', 'IBM_2395.txt', 'IBM_3480_Family.txt', 'IBM_data_Cell.txt', 'IBM_eServer.txt', 
    # 'IBM_Magstart.txt', 'IBM_storage.txt', 'Infomation_tech.txt', 'Inline_linking.txt', 'INM_2365_Processor.txt', 'Input_queue.txt', 'Internet_intermediaryw.txt', 'Internet_leakw.txt', 
    # 'Internet_of_thingsw.txt', 'Internet_Plusw.txt', 'Interpreter_directivew.txt', 'JavaScrip original.txt', 'Jaz_drivew.txt', 'Landing_pagew.txt', 'Link aggregation original.txt', 
    # 'Linked_dataw.txt', 'List_of_computer_system_manufacturersw.txt', 'Lt._Kernalw.txt', 'Machine-readable_mediumw.txt', 'Machine_learningw.txt', 'Main_Pagew.txt', 'Map_matchingw.txt', 
    # 'Memory_geometryw.txt', 'Microprocessorw.txt', 'Multiprocessingw.txt', 'National_Information_Infrastructurew.txt', 'Online_and_offlinew.txt', 'Online_shoppingw.txt', 'Pay-per-click.txt', 
    # 'Phishingw.txt', 'PHPw.txt', 'PocketZipw.txt', 'Power_userw.txt', 'Preboot execution environment original .txt', 'Print_Screenw.txt', 'Programmerw.txt', 'Programming_languagew.txt',
    #  'Programw.txt', 'Real_lifew.txt', 'Robotics.txt', 'Salesforce.txt', 'Search_enginew.txt', 'Superhighway.txt', 'UEFI original.txt', 'Virtualization.txt', 'Web 2.0 original .txt', 
    # 'Webiste_spoofing.txt', 'Websocket.txt', 'Web_Call_back.txt', 'WEb_widget.txt', 'WeedTuber.txt', 'Wifi original.txt', 'Word_Processor.txt', 'Zip_drive.txt']

def __read_file__(name_file): # Hàm đọc file txt
    f = open(name_file,'rb')
    text = f.read()
    f.close()
    return text
# print(__read_file__('List_of_computer_system_manufacturersw.txt'))
# Kết quả: 
""" List of computer system manufacturers
The following is a list of notable computer system manufacturers.
Current
Companies that have ceased production
See also
References
External links
ABS Computer Technologies (Parent:
Newegg)
Acer
AG Neovo
Alphabet Inc.
Google
Amiga, Inc.
ACube Systems Srl
Hyperion Entertainment
Aigo
AMD
Aleutia
Alienware (Parent: Dell)
AMAX Information Technologies
AOpen
Apple
ASRock
Asus
AVADirect
AXIOO International
BenQ
Biostar
Brother Industries
Burroughs Corporation
Corona Data Systems
Chassis Plans
Chip PC
Cisco Systems
Clevo
Crystal Group
Compal
Cooler Master
CyberPowerPC
Dai-Tech
Data General
Dell
Wyse Technology
DFI
Digital Storm
Elitegroup Computer Systems (ECS)
Eagle Computer
Epson
Evans & Sutherland
Everex
EVGA
Falcon Northwest
FIC
Fujitsu
Foxconn
Founder Technology
Gigabyte
Aorus
GoPro
Gradiente
Contents
Current
Groupe Bull
Grundig (Parent: Arçelik)
Hasee
HCL
Hewlett Packard Enterprise
Cray
Silicon Graphics International
HP Inc. (formerly Hewlett-Packard)
Fortify Software
HP Autonomy
Compaq
Digital Equipment Corporation
Hitachi
HTC
Huawei
Hyundai
IBM
Intel
Inventec
Itautec
IGEL
Jetta International
Kohjinsha
Kontron AG
Lanix
Lanner Electronics
LanSlide Gaming PCs
Lenovo
Medion
LG
LiteOn
Maingear
Meebox
Mesh Computers
Microsoft
Micro-Star International (MSI)
Micro Center
Myria
MiTAC
Motion Computing
Monel
Motorola
NComputing
NCR
NEC
Nvidia
NZXT
Olidata
Oracle
Origin PC
Panasonic
Positivo Informática
Puget Systems
Quanta Computer
RCA
Razer
Samsung
Sapphire Technology
Shuttle
Síragon
Sony
Supermicro
SupernovaGaming
Systemax
System76
T-Platforms
TabletKiosk
Tadpole Computer
Tatung
Toshiba
Tyan
Unisys
V3 Gaming PC
Vaio
Velocity Micro
Vestel
VIA Technologies
ViewSonic
Viglen
Vizio
Valve
Walton Group
Wistron
Wortmann
Xiaomi
Zelybron
Zoostorm
Zotac
zSpace
Acorn Computers - Bought by Morgan Stanley and renamed as Element 14 in 1999.
Alliant Computer Systems - Ceased operations in 1992.
Altos Computer Systems - Acquired by Acer in 1990.
Amdahl Corporation - A wholly owned subsidiary of Fujitsu since 1997.
Amstrad
Apollo Computer - Acquired by Hewlett-Packard in 1989.
Apricot Computers - Ceased operations in 1999.
Ardent Computer - Merged with Stellar Computer to form Stardent in 1989.
AST Computers, LLC - Exited the computer market in 2001.
Atari Corporation
Bell & Howell
Burroughs - Merged with Sperry to form Unisys in 1986.
Celerity Computing - Acquired by Floating Point Systems in 1988.
Commodore International - Declared bankruptcy in 1994.
Compaq - Acquired by Hewlett-Packard in 2002. Defunct as a subsidiary as of 2013.
CompuAdd - Filed for bankruptcy in 1993.
Computer Automation
Control Data Corporation (CDC) - Shrank as units were spun off from 1988 to 1992;
remainder is now Ceridian.
Convergent Technologies - Acquired by Unisys in 1988.
Convex Computer - Purchased by The Hewlett-Packard Company in 1995.
Corona Data Systems - among the original "IBM PC Compatible" clone makers
Cromemco
Data General - was one of the first minicomputer firms from the late 1960s, purchased by
EMC in 1999 for its innovative RAID array storage.
Datapoint
Digital Equipment Corporation - Acquired by Compaq in 1998.
Durango Systems Corporation - Merged with Molecular Systems in 1982 which went
bankrupt in 1984
Eagle Computer - Ceased operations in 1986.
Eckert–Mauchly Computer - Acquired by Remington Rand in 1950.
Egenera
Elonex — Sells tablets (as of 2011)
EMCC
Encore Computer - Acquired by Gores Technology Group in 1998 and renamed to Encore
Real Time Computing.
English Electric - Merged into International Computers Limited.
eMachines - Discontinued by its current owner Acer in 2012.
Escom - Declared bankruptcy on July 15, 1996.
Everex - US subsidiary closed in 2009.
Evesham - Merged into TIME Computers.
Franklin Computer Corporation - Exited computer hardware business and reorganized into
Franklin Electronic Publishers.
Gateway - Acquired by Acer in October 2007.
Companies that have ceased production
General Electric - Sold its computer division to Honeywell in 1970.
Gericom - Acquired by Quanmax then merged with S&T.
Gould Electronics - Sold its computer division to Nippon Mining in 1988, who in turn sold it
to Encore Computer later that year.
Hewlett-Packard - Spun off into Hewlett Packard Enterprise and renamed as HP Inc. in 2015
Honeywell - Sold its computer division to Groupe Bull in 1991.
International Computers and Tabulators (ICT) - Merged into International Computers Limited.
International Computers Limited (ICL) - Now part of Fujitsu.
Kaypro - Filed for bankruptcy in 1992.
Leading Edge - Mid '80s leader in PC clone for the masses - Manufacturing done first by
Mitsubishi then Daewoo.
LEO Computers - Lyons Electronic Office. In 1963 merged with English Electric, then
Marconi and eventually merged into International Computers Limited (ICL) in 1968.
Luxor AB - Ended in 1986 after being acquired by Nokia the previous year.
Magnavox - Philips PCs rebadged for the USA and Canada.[1]
Magnuson Computer Systems - Filed for bankruptcy in the early 1980s.
Maxdata (Germany) - Insolvent in 2008; warranty for existing products taken over by then the
Swiss Belinea AG (see Belinea), now owned by Bluechip Computer. Warranty for Belinea
products purchased before 1 November 2008 is not serviced anymore by Bluechip
Computer.[2]
Micron Technology -
Mitsubishi Electronics - Closed computer systems division in 1990; Manufactured systems
for Leading Edge and Sperry-Unisys
MPC (formerly MicronPC) - Filed Chapter 11 bankruptcy on November 7, 2008. Efforts at
reorganization failed.
Multiflow Computer - Ceased operations in 1990.
NeXT - Acquired by Apple Computer in 1997.
Nixdorf Computer - Acquired by Siemens in 1991, renamed Siemens Nixdorf
Informationssysteme AG.
Northgate Computer Systems - Acquired by Lan Plus in 1997, after filing for Chapter 11
bankruptcy in 1994.
Osborne Computer - Ceased operations in 1985; rights to the Osborne brand were sold to
Mikrolog.
Olivetti
Packard Bell - Subsidiary of Acer.
Philco-Ford
Philips - Sold their PC division to Digital Equipment Corporation.
Prime Computer - Acquired by Parametric Technology Corporation in 1998.
Processor Technology - Ceased operations in 1979.
Psystar - Under 2009 permanent injunction to stop selling computers with Apple's Mac OS X
operating system. Psystar's web site has since disappeared.
Pyramid Technology - Acquired by Siemens in 1995.
Quantex Microsystems - Bankrupt in 2000.
Radio Shack
RCA - Exited the computer business in 1971; Sperry Rand took over RCA's installed base in
1972.
Research Machines - Exited manufacturing in late 2013. Brand continues as a services
company.
Remington Rand - Acquired by Sperry to form Sperry Rand in 1955.
Sanyo - Bought out by Panasonic.
Scientific Data Systems - Acquired by Xerox in 1969.
Sequent Computer Systems - Acquired by IBM in 1999.
Siemens - Computer division (Siemens Nixdorf Informationssysteme AG) merged 50/50 with
Fujitsu into Fujitsu Siemens Computers in 1999, then Siemens half bought by Fujitsu in
2009.
Silicon Graphics - Acquired by Rackable Systems in 2009, when Rackable then re-branded
to SGI, and later acquired by Hewlett Packard Enterprise in November 2016.
Sinclair Research - Acquired by Amstrad in 1986.
Solbourne Computer - Acquired by Deloitte Consulting in 2008.
Soyo
Sperry - Merged with Burroughs to form Unisys in 1986.
Sperry Rand - Dropped "Rand" from its name in 1978 and continued as Sperry.
Stardent - Ceased operations in 1992.
Stratus Computer
Sun Microsystems - Acquired by Oracle Corporation in 2010.
Systems Engineering Laboratories - Acquired by Gould Electronics in 1981 and became
Gould's computer division.
Systime Computers Ltd – Once Britain's second largest, acquired by Control Data
Corporation in 1985, broken up in 1989.
Tandon Corporation
Tandy Corporation - Previous parent company of RadioShack, produced the TRS-80 and
Tandy 1000 and 2000 IBM PC compatible computers. Sold their computer division to AST
Research in 1993.
Tiny Computers - Merged into TIME Computers.
Texas Instruments
Averatec - Averatec subsidiary goes out of business in 2012.
Tulip Computers - Changed its name to Nedfield NV in 2008, pronounced bankrupt on 3
September 2009.
Vigor Gaming (USA) - Disappeared in March 2010.
VoodooPC
VTech - Ceased PC manufacturing.
Walton
Wang Laboratories - Acquired by Getronics in 1999.
Wipro - Ceased PC manufacturing.
Xerox - Exited the computer business.
Zenith Data Systems - Merged With Packard Bell and NEC in 1996.
Zeos - Merged into MPC Corporation in 1996, which in turn filed for Chapter 11 bankruptcy
in 2008.
List of computer hardware manufacturers
List of laptop brands and manufacturers
List of touch-solution manufacturers
Market share of personal computer vendors
See also
1. "IBM ValuePoint Collection" (http://ibmvaluepoint.blogspot.com/).
ibmvaluepoint.blogspot.com.
2. "Wie becomme ich Service oder Informationen zu alten Belinea Produkten?" (https://web.arc
hive.org/web/20110413164735/http://www.belinea.de/belinea/cms/index.php?article_id=55).
FAQs (in German). Belinea. Archived from the original (http://www.belinea.de/belinea/cms/in
dex.php?article_id=55) on 2011-04-13. Retrieved 2011-11-12.
epocalc's List of Computer Manufacturers (http://www.epocalc.net/php/liste_comp.php)
Retrieved from "https://en.wikipedia.org/w/index.php?
title=List_of_computer_system_manufacturers&oldid=1039961346"
This page was last edited on 21 August 2021, at 20:39 (UTC).
Text is available under the Creative Commons Attribution-ShareAlike License; additional terms may apply. By using
this site, you agree to the Terms of Use and Privacy Policy. Wikipedia® is a registered trademark of the Wikimedia
Foundation, Inc., a non-profit organization.
References
External links """

def __dell__(sentence): # Tiền xử lý văn bản
    sentence = sentence.decode('ISO-8859-1')
    entence = sentence.lower() # Chuyển thành văn bản viết thường
    sentence = re.sub(r'[~!@#$%\^&*\(\)\[\]\\|:;\'"]+', ' ', sentence) # Xóa các ký tự đặc biệt không liên quan đến câu
    sentence = re.sub(r'\s+', ' ', sentence).strip() # Xóa khoảng trăng thừa cuối văn bản
    sentence = sent_tokenize(sentence) # Tách 1 đoạn văn bản thành các câu
    return sentence



# print(__dell__(__read_file__('Link aggregation original.txt')))

# Kết quả: ['in computer networking, link aggregation is the combining aggregating of multiple network connections in parallel by any of several methods, in order to increase throughput beyond what a single connection could sustain, to provide redundancy in case one of the links should fail, or both.', 'a link aggregation group lag is the combined collection of physical ports.', 'other umbrella terms used to describe the concept include trunking, 1 bundling, 2 bonding, 1 channeling 3 or teaming.', 'implementation methods encompass not only vendor-independent standards such as link aggregation control protocol lacp for ethernet, defined in ieee 802.1ax or the previous ieee 802.3ad, but also various proprietary solutions.', 'motivation link aggregation increases the bandwidth and resilience of ethernet connections.', 'bandwidth requirements do not scale linearly.', 'ethernet bandwidths historically have increased tenfold each generation 10 megabit/s, 100 mbit/s, 1000 mbit/s, 10,000 mbit/s.', 'if one started to bump into bandwidth ceilings, then the only option was to move to the next generation, which could be cost prohibitive.', 'an alternative solution, introduced by many of the network manufacturers in the early 1990s, is to use link aggregation to combine two physical ethernet links into one logical link.', 'most of these early solutions required manual configuration and identical equipment on both sides of 
""" the connection.', '4 there are three single points of failure inherent to a typical port-cable-port connection, in either a computer- to-switch or a switch-to-switch configuration the cable itself or either of the ports the cable is plugged into can fail.', 'multiple logical connections can be made, but many of the higher level protocols were not designed to fail over completely seamlessly.', 'combining multiple physical connections into one logical connection using link aggregation provides more resilient communications.', 'architecture network architects can implement aggregation at any of the lowest three layers of the osi model.', 'examples of aggregation at layer 1 physical layer include power line e.g.', 'ieee 1901 and wireless e.g.', 'ieee 802.11 network devices that combine multiple frequency bands.', 'osi layer 2 data link layer, e.g.', 'ethernet frame in lans or multi-link ppp in wans, ethernet mac address aggregation typically occurs across switch ports, which can be either physical ports or virtual ones managed by an operating system.', 'aggregation at layer 3 network layer in the osi model can use round-robin scheduling, hash values computed from fields 
in the packet header, or a combination of these two methods.', 'regardless of the layer on which aggregation occurs, it is possible to balance the network load across all links.', 'however, in order to avoid out-of-order delivery, not all implementations take advantage of this.', 'most methods provide failover as well.', 'combining can either occur such that multiple interfaces share one logical address i.e.', 'ip or one physical address i.e.', 'mac address , or it allows each interface to have its own address.', 'the former requires that both ends of a link use the same aggregation method, but has performance advantages over the latter.', 'channel bonding is differentiated from load balancing in that 
load balancing divides traffic between network interfaces on per network socket layer 4 basis, while channel bonding implies a division of traffic between physical interfaces at a lower level, either per packet layer 3 or a data link layer 2 basis.', 'ieee link aggregation standardization process by the mid 1990s, most network switch manufacturers had included aggregation capability as a proprietary extension to increase bandwidth between their switches.', 'each manufacturer developed its own method, which led to compatibility problems.', 'the ieee 802.3 working group took up a study group to create an interoperable link layer standard i.e.', 'encompassing the physical and data-link layers both in a november 1997 meeting.', '4 the group quickly agreed to include an automatic configuration feature which would add in redundancy as well.', 'this became known as link aggregation control protocol lacp .', '802.3ad as of 2000, most gigabit 
channel-bonding schemes use the ieee standard of link aggregation which was formerly clause 43 of the ieee 802.3 standard added in march 2000 by the ieee 802.3ad task force.', '5 nearly every network equipment manufacturer quickly adopted this joint standard over their proprietary standards.', '802.1ax the 802.3 maintenance task force report for the 9th revision project in november 2006 noted that certain 802.1 layers such as 802.1x security were positioned in the protocol stack below link aggregation which was defined as an 802.3 sublayer.', '6 to resolve this discrepancy, the 802.3ax 802.1ax task force was formed, 7 resulting in the formal transfer of the protocol to the 802.1 group with the publication of ieee 802.1ax-2008 on 3 november 2008.', '8 link aggregation control protocol within the ieee ethernet standards, the link aggregation control protocol lacp provides a method to control the bundling of several physical links together to form a single logical link.', 'lacp allows a network device to negotiate an automatic bundling of links by sending lacp packets to their peer, a directly connected device that also implements lacp.', 'lacp features and practical examples 1. maximum number of bundled ports allowed in the port channel valid values are usually from 1 to 8.', '2. lacp packets are sent with multicast group mac address 01 80 c2 00 00 02 3. during lacp detection period lacp packets are transmitted every second keep-alive mechanism for link member default slow = 30s, fast=1s 4. selectable load-balancing mode is available in some implementations 9 5. lacp mode 6. active enables lacp unconditionally.', '7. passive enables 
lacp only when an lacp device is detected.', 'this is the default state 8. advantages over static configuration 9. failover occurs automatically when a link has an intermediate failure, for example in a media converter between the devices, a peer system may not perceive any connectivity problems.', 'with static link aggregation, the peer would continue sending traffic down the link causing the connection to fail.', '10. dynamic configuration the device can confirm that 
the configuration at the other end can handle link aggregation.', 'with static link aggregation, a cabling or configuration mistake could go undetected and cause undesirable network behavior.', '10 11. practical notes 12. lacp works by sending frames lacpdus down all links that have the protocol enabled.', 'if it finds a device on the other end of a link that also has lacp enabled, that device will independently send frames along the same links in the opposite direction enabling the two units to detect multiple links between themselves and then combine them into a single logical link.', 'lacp can be configured in one of two modes active or passive.', 'in active mode, lacpdus are sent 1 per second along the configured links.', 'in passive mode, lacpdus are not sent until one is received from the other side, a speak-when-spoken-to protocol.', '13. proprietary link aggregation 14. in addition to the ieee link aggregation substandards, there are a number of proprietary aggregation schemes including cisco s etherchannel and port aggregation protocol, juniper s aggregated ethernet, avaya s multi-link trunking, split multi-link trunking, routed split multi-link trunking and distributed split multi-link trunking, zte s smartgroup , huawei s eth-trunk , or connectify s speedify.', '11 most high-end network devices support some kind of link aggregation, and software-based implementations – such as the bsd lagg package, linux bonding driver, solaris dladm aggr, etc.', '– also exist for many operating systems.', '15. linux bonding driver 16. the linux bonding driver 12 provides a method for aggregating multiple network interface controllers nics into a single logical bonded interface of two or more so-called nic slaves.', 'the majority of modern linux distributions come with a linux kernel which has the linux bonding driver integrated as a loadable kernel module and the ifenslave if = network interface user-level control program pre-installed.', 'donald becker programmed the original linux bonding driver.', 'it came into use with the beowulf cluster patches for the linux kernel 2.0.', '17. driver modes 18. modes for the linux bonding driver 12 network interface aggregation modes are supplied as parameters to the kernel bonding module at load time.', 'they may be given as command-line arguments to the insmod or modprobe command, but are usually specified in a linux distribution-specific configuration file.', 'the 19. behavior of the single logical bonded interface depends upon its specified bonding driver mode.', 'the default parameter is balance-rr.', '20. round-robin balance-rr 21. transmit network packets in sequential order from the first available network interface nic slave through the last.', 'this mode provides load balancing and fault tolerance.', '13 it can sometimes cause contention because packets may be reordered on the way to the destination, though remedies exist.', '14 22. active-backup active-backup 23. only one nic slave in the bond is active.', 'a different slave becomes active if, and only if, the active slave fails.', 'the single logical bonded interface s mac address is externally visible on only one nic port to avoid distortion in the network switch.', 'this mode provides fault tolerance.', '24. xor balance-xor 25. transmit network packets based on a hash of the packet s source and destination.', 'the default algorithm only considers mac addresses layer2 .', 'newer versions allow selection of additional policies based on ip addresses layer2+3 and tcp/udp port numbers layer3+4 .', 
'this selects the same nic slave for each destination mac address, ip address, or ip address and port combination, respectively.', 'single connections will have guaranteed in order packet delivery and will transmit at the speed of a single nic.', '15 this mode provides load balancing and fault tolerance.', '26. broadcast broadcast 27. transmit network packets on all slave network interfaces.', 'this mode provides fault 28. tolerance.', '29. ieee 802.3ad dynamic link aggregation 802.3ad, lacp 30. creates aggregation groups that share the same speed and duplex settings.', 'utilizes all slave network interfaces in the active aggregator group according to the 802.3ad specification.', 'this mode is similar 
to the xor mode above and supports the same balancing policies.', 'the link is set up dynamically between two lacp-supporting peers.', '31. adaptive transmit load balancing balance-tlb 32. linux bonding driver mode that does not require 
any special network-switch support.', 'the outgoing network packet traffic is distributed according to the current load computed relative to the speed on each network interface slave.', 'incoming traffic is received by one currently designated slave network interface.', 'if this receiving slave fails, another slave takes over the mac address of the failed receiving slave.', '33. adaptive load balancing balance-alb 34. includes balance-tlb plus receive load balancing rlb for ipv4 traffic, and does not require any special network switch support.', 'the receive load balancing is achieved by arp negotiation.', 'the bonding driver intercepts the arp replies sent by the local system on their way out and overwrites the source hardware address with the unique hardware address of one of the nic slaves in the single logical bonded interface such that different network-peers use different mac addresses for their network packet traffic.', '35. linux team driver 36. the linux team driver 16 provides an alternative to bonding driver.', 'the main difference is that team driver kernel part contains only essential code and the rest of the code link validation, lacp implementation, decision making, etc.', 'is run in userspace as a part of teamd daemon.', '37. usage 38.', '39. network backbone 40. link aggregation offers an inexpensive way to set up a high-speed backbone network that transfers much more data than any 
single port or device can deliver.', 'link aggregation also allows the network s backbone speed to grow incrementally as demand on the network increases, without having to replace everything and deploy new hardware.', '41. most backbone 
installations install more cabling or fiber optic pairs than is initially necessary, even if they have no immediate need for the additional cabling.', 'this is done because labor costs are higher than the cost of the cable, and running extra cable reduces future labor costs if networking needs change.', 'link aggregation can allow the use of these extra cables to increase backbone speeds for little or no extra cost if ports are available.', '42. order of frames 43. when balancing traffic, network administrators often wish to avoid reordering ethernet frames.', 'for example, tcp suffers additional overhead when dealing with out-of-order packets.', 'this goal is approximated by sending all frames associated with a particular session across the same link.', '17 common implementations use l2 or l3 hashes i.e.', 'based on the mac or the ip addresses , ensuring that the same flow is always sent via the same physical link.', '18 44. however, this may not provide even distribution across the links in the trunk when only a single or very few pairs of hosts communicate with each other, i.e.', 'when the hashes provide too little variation.', 'it effectively limits the client bandwidth in aggregate to its single member s maximum bandwidth per communication partner.', 'in extreme, one link is fully loaded while the others are completely idle.', 'for this reason, an even load balancing and full utilization of all trunked links is almost never reached in real-life implementations.', 'more advanced switches can employ an l4 hash i.e.', 'using tcp/udp port numbers , which may increase the traffic variation across the links – depending on whether the ports vary – and bring the balance closer to an even distribution.', '45. maximum throughput 46. multiple switches may be utilized to optimize for maximum throughput in a multiple network switch topology, 12 when the switches are configured in parallel as part of an isolated network between two or more systems.', 'in this configuration, the switches are isolated from one another.', 'one reason to employ a topology such as this is for an isolated network with many hosts a cluster configured for high performance, for example , using multiple smaller switches can be more cost effective than a single larger switch.', 'if access beyond the network is required, an individual host can be equipped with an additional network device connected to an external network this host then additionally acts as a gateway.', 'the network interfaces 1 through 3 of computer cluster node a, for example, are connected via separate network switches 1 through 
3 with network interfaces 1 through 3 of computer cluster node b there are no inter- connections between the network switches 1 through 3. the linux bonding driver mode typically employed in configurations of this type is balance-rr the 
balance-rr mode allows individual connections between two hosts to effectively utilize greater than one interface s bandwidth.', '47. use on network interface cards 48. nics trunked together can also provide network links beyond the throughput of any one single nic.', 'for example, this allows a central file server to establish an aggregate 2-gigabit connection using two 1-gigabit nics teamed together.', 'note the data signaling rate will still be 1gbit/s, which can be 
misleading depending on methodologies used to test throughput after link aggregation is employed.', '49. microsoft windows 50. microsoft windows server 2012 supports link aggregation natively.', 'previous windows server versions relied on manufacturer support of the feature within their device driver software.', 'intel, for example, released advanced networking services ans to bond intel fast ethernet and gigabit cards.', '19 nvidia also supports teaming with their nvidia network access manager/firewall tool.', 'hp also has a teaming tool for hp branded nics which will allow for non-etherchanneled nic teaming or which will support several modes of etherchannel port aggregation including 802.3ad with lacp.', 'in addition, there is a basic layer-3 aggregation available at least from windows xp sp3 , 20 that allows servers with multiple ip interfaces on the same network to perform load balancing, and home users with more than one internet connection, to increase connection speed by sharing the load on all interfaces.', '21 51. broadcom offers advanced functions via broadcom advanced control suite bacs , via which the teaming functionality of basp broadcom advanced server program is available, offering 802.3ad static lags, lacp, and smart teaming which doesn t require any configuration on the switches to work.', 'it is possible to configure teaming with bacs with a mix of nics from different vendors as 
long as at least one of them is broadcom and the other nics have the required capabilities to create teaming.', '22 52. linux and unix 53. linux, freebsd, netbsd, openbsd, macos, opensolaris and commercial unix distributions such as aix 
implement ethernet bonding trunking at a higher level, and can hence deal with nics from different manufacturers or drivers, as long as the nic is supported by the kernel.', '12 54. virtualization platforms 55. citrix xenserver and vmware esx have native support for link-aggregation.', 'xenserver offers both static lags as well as lacp.', 'vsphere 5.1 esxi supports both static lags and lacp natively with their virtual distributed switch.', '23 for microsoft s hyper-v, bonding or teaming isn t offered from the hyper-visor or os-level, but the above- mentioned methods for teaming under windows applies to hyper-v as well.', '56. limitations 57. single switch 58. with the modes balance-rr, balance-xor, broadcast and 802.3ad, all physical ports in the link aggregation group must reside on the same logical switch, which, in most common scenarios, will leave a single point of failure when the physical switch to which all links are connected 
goes offline.', 'the modes active-backup, balance-tlb, and balance-alb can also be set up with two or more switches.', 'but after failover like all other modes , in some cases, active sessions may fail due to arp problems and have to be 
restarted.', '59. however, almost all vendors have proprietary extensions that resolve some of this issue they aggregate multiple physical switches into one logical switch.', 'the split multi-link trunking smlt protocol allows multiple ethernet links to be split across multiple switches in a stack, preventing any single point of failure and additionally allowing all switches to be load balanced across multiple aggregation switches from the single access stack.', 'these 
devices synchronize state across an inter-switch trunk ist such that they appear to the connecting access device to be a single device switch block and prevent any packet 60. duplication.', 'smlt provides enhanced resiliency with sub-second failover and sub-second recovery for all speed trunks 10 mbit/s, 100 mbit/s, 1,000 mbit/s, and 10 gbit/s while operating transparently to end- devices.', '61. same link speed 62. in most implementations, all the ports used in an aggregation consist of the same physical type, such as all copper ports 10/100/1000base‐t , all multi-mode fiber ports, or all single-mode fiber ports.', 'however, all the ieee standard requires is that each link be full duplex and all of them have an identical speed 10, 100, 1,000 or 10,000 mbit/s .', '63. many switches are phy independent, meaning that a switch could have a mixture of copper, sx, lx, lx10 or other gbics.', 'while maintaining the same phy is the usual approach, it is possible to aggregate a 1000base-sx fiber for one link and a 1000base-lx longer, diverse path for the second link, but the important thing is that the speed will be 1 gbit/s full duplex for both links.', 'one path may have a 
slightly longer propagation time but the standard has been engineered so this will not cause an issue.', '64. ethernet aggregation mismatch 65. aggregation mismatch refers to not matching the aggregation type on both ends of the link.', 
'some switches do not implement the 802.1ax standard but support static configuration of link aggregation.', 'therefore, link aggregation between similarly statically configured switches will work but will fail between a statically configured switch and a device that is configured for lacp.', '66. examples 67. ethernet 68. on ethernet interfaces, channel bonding requires assistance from both the ethernet switch and the host computer s operating system, which must stripe the delivery of frames across the network interfaces in the same manner that i/o is striped across disks in a raid 0 array.', 'for this reason, some discussions of channel bonding also refer to redundant array of inexpensive nodes rain 
or to redundant array of independent network interfaces .', '24 69. modems 70. in analog modems, multiple dial-up links over pots may be bonded.', 'throughput over such bonded connections can come closer to the aggregate bandwidth of the bonded links than can throughput under routing schemes which simply load-balance outgoing network connections over the links.', '71. dsl 72. similarly, multiple dsl lines can be bonded to give higher bandwidth in the united kingdom, adsl is sometimes bonded https //evolving.net.uk/bonded-adsl-guide/how-does-bonded-adsl-work/ to give for example 512kbit/s upload bandwidth and 4 megabit/s download bandwidth, in areas that only have access to 2 megabit/s bandwidth.', '73. docsis 74. under the docsis 3.0 25 and 3.1 26 specifications for data over cable tv catv systems, multiple channels may be bonded.', 'under docsis 3.0, up to 32 downstream and 8 upstream channels may be bonded.', 'these are typically 6 
or 8 mhz wide.', 'docsis 3.1 defines more complicated arrangements involving aggregation at the level subcarriers and larger notional channels.', '75. wireless broadband 76. broadband bonding is a type of channel bonding that refers to aggregation of multiple channels at osi layers at level four or above.', 'channels bonded can be wired links such as a t-1 or dsl line.', 'additionally, it is possible to bond multiple cellular links for an aggregated wireless bonded link.', '77. previous bonding methodologies resided at lower osi layers, requiring coordination with telecommunications companies for implementation.', 'broadband bonding, because it is implemented at higher layers, can be done without this 
coordination.', '27 78. commercial implementations of broadband channel bonding include 79. wistron aiedge corporation s u-bonding technology 28 mushroom networks broadband bonding service 29 80. connectify s speedify fast bonding vpn - 
software app for multiple platforms pc, mac, ios and android 30 81. peplink s speedfusion bonding technology 31 viprinet s multichannel vpn bonding technology 32 elsight s multichannel secure data link 33 synopi s natiply internet bonding technology 34 82. wi-fi 83. on 802.11 wi-fi , channel bonding is used in super g technology, referred to as 108mbit/s.', 'it bonds two channels of standard 802.11g, which has 54mbit/s data signaling rate.', '84. on ieee 802.11n, a mode with a channel width of 40 mhz is specified.', 'this is not channel bonding, but a single channel with double the older 20 mhz channel width, thus using two adjacent 20 mhz bands.', 'this allows direct doubling of the phy data rate from a single 20 mhz channel, but the mac and user-level throughput also depends on other factors so may not double.'] """

def update_json(s):  # Lưu dữ liệu xử lỹ vào một tệp tin để training. Sử dụng tệp .json thay vì .txt để dễ truy vấn
    with open("training.json",'r', encoding='ISO-8859-1') as fp:
        information1 = json.load(fp)
    information1["intents"].append({
        "title": s,
        "text": __dell__(__read_file__(s))  # Đoạn này là list các câu được tách ra của một văn bản
    })
    with open("training.json",'w',encoding='utf-8') as fp: # Thêm dữ liệu vào tệp JSON
        json.dump(information1, fp, indent=2,)

def main(): # Chương trình chính
    list = __read_forlder__() # Đọc và ghi vào list các văn bản cần train
    for files in list: # Dùng for để đọc và thêm tất cả văn bản trong list
        update_json(files) # Thêm và lưu tất cả dữ liệu vào file training.json
    

main() # Chạy hàm này dữ liệu sẽ được tự thêm vào file training.json trong forlder data
