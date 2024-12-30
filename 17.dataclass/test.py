from dataclasses import dataclass, field
from typing import List, Optional

# import random

@dataclass
class ImportRT:
    import_rt: str

@dataclass
class ExportRT:
    export_rt: str

@dataclass
class Interface:
    name: str = 'dummy'
    ipv4_address_mask: List[str] = field(default_factory=[])
    # ipv6_address_mask: List[str] = ['dummy']
    # ipv4_ospf_enabled: bool


@dataclass
class OspfNbr:
    ospf_nbr: str

@dataclass
class BgpNbr:
    bgp_nbr: str

@dataclass
class Vrf:
    name: str
    rd: str
    # import_rts: List [ImportRT]
    # export_rts: List [ExportRT]
    interfaces: List [Interface]
    # bgp_nbrs: List [BgpNbr]
    # total_interfaces: int
    # total_subnets: int
    # total_arp_entries: int
    # total_connected_routes: int
    # total_ce_learned_routes: int
    # total_core_leared_routes: int
    # total_ospf_nbrs: int
    # total_bgp_nbrs: int

vrf_names: list = ['vrf1', 'vrf2', 'vrf3']

vrf_object_list: list = []


for item in vrf_names:
    ###
    interface_object_list: list = []
    for _ in range(1,3):
        interface_object = Interface(name=f"Gig14.5623", ipv4_address_mask=['1.1.1.1 255.255.255.0', '2.2.2.2 255.255.255.255'])
        interface_object_list.append(interface_object)
    ###     

    vrf_object = Vrf(name=item,
                     rd='345345:2235',
                     interfaces=interface_object_list)
    vrf_object_list.append(vrf_object)

###
for item in vrf_object_list:
    print(len(item.interfaces))

print (vrf_object_list)
print('-' * 50)
print(vrf_object_list[0].name)
vrf_object_list[0].name = 'vrf100'
print(vrf_object_list[0].name)
print(vrf_object_list[0].interfaces[1].name)



