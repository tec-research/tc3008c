#!/usr/bin/env python3
from mininet.net import Mininet
from mininet.node import Node, OVSSwitch, OVSController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info


class LinuxRouter(Node):
    def config(self, **params):
        super().config(**params)
        self.cmd("sysctl -qw net.ipv4.ip_forward=1")

    def terminate(self):
        self.cmd("sysctl -qw net.ipv4.ip_forward=0")
        super().terminate()


def build_network():
    net = Mininet(controller=OVSController, switch=OVSSwitch, link=TCLink,
                  build=False, autoSetMacs=True)
    net.addController("c0")
    r1 = net.addHost("r1", cls=LinuxRouter, ip=None)
    switches = {name: net.addSwitch(name)
                for name in ("sExt", "sUsr", "sDmz", "sAdm")}

    specs = [
        ("attacker", "10.0.0.10/24", "10.0.0.1", "sExt", 20, "8ms"),
        ("client1", "10.0.10.11/24", "10.0.10.1", "sUsr", 50, "3ms"),
        ("client2", "10.0.10.12/24", "10.0.10.1", "sUsr", 50, "3ms"),
        ("web", "10.0.20.20/24", "10.0.20.1", "sDmz", 30, "5ms"),
        ("dns", "10.0.20.53/24", "10.0.20.1", "sDmz", 30, "5ms"),
        ("admin", "10.0.30.10/24", "10.0.30.1", "sAdm", 50, "2ms"),
    ]
    for name, ip, gateway, switch, bw, delay in specs:
        host = net.addHost(name, ip=ip, defaultRoute=f"via {gateway}")
        net.addLink(host, switches[switch], bw=bw, delay=delay)

    router_links = [
        ("sExt", "r1-ext", "10.0.0.1/24"),
        ("sUsr", "r1-usr", "10.0.10.1/24"),
        ("sDmz", "r1-dmz", "10.0.20.1/24"),
        ("sAdm", "r1-adm", "10.0.30.1/24"),
    ]
    for switch, interface, ip in router_links:
        net.addLink(r1, switches[switch], intfName1=interface,
                    params1={"ip": ip})
    return net


if __name__ == "__main__":
    setLogLevel("info")
    network = build_network()
    network.build()
    network.start()
    info("\nLAB_READY: use net, dump y pingall.\n")
    try:
        CLI(network)
    finally:
        network.stop()
