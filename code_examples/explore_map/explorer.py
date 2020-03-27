import re
from pprint import pprint
from queue import Queue

import yaml
from netmiko import (
    ConnectHandler,
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)


visited_hosts = set()
failed_hosts_error_map = {}
params = {
    'device_type': 'cisco_ios',
    'password': 'cisco',
    'secret': 'cisco',
    'username': 'cisco'
}
total = {}


def parse_cdp(output):
    regex = (
        r"IP address: (?P<ip>\S+)\n"
        r".*?"
        r"Interface: (?P<local_port>\S+), +"
        r"Port ID \(outgoing port\): (?P<remote_port>\S+)"
    )

    result = {}

    match_iter = re.finditer(regex, output, re.DOTALL)
    for match in match_iter:
        ip = match.group("ip")
        groupdict = match.groupdict()
        del groupdict["ip"]
        result[ip] = groupdict
    return result


def connect_ssh(params, command):
    try:
        with ConnectHandler(**params) as ssh:
            ssh.enable()
            prompt = ssh.find_prompt()
            return f"{prompt}\n{ssh.send_command(command)}"
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as error:
        print(error)


def topology_bfs(start_device):
    q = Queue()
    q.put(start_device)
    while q.qsize() > 0:
        current = q.get()
        params["host"] = current
        connections = parse_cdp(connect_ssh(params, "sh cdp neig det"))
        total[current] = connections
        for neighbor, n_data in connections.items():
            if neighbor not in visited_hosts:
                q.put(neighbor)
        visited_hosts.add(current)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    #for device in devices:
    #    pprint(parse_cdp(connect_ssh(device, "sh cdp neig det")))
    topology_bfs("192.168.100.1")
    print(visited_hosts)
    pprint(total)
