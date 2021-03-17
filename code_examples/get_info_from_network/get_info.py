from itertools import repeat
import yaml
import csv
import netmiko
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

from netmiko import ConnectHandler


def ping_ip(ip):
    result = subprocess.run(["ping", "-c", "3", "-n", ip], stdout=subprocess.DEVNULL)
    ip_is_reachable = result.returncode == 0
    return ip_is_reachable


def ping_ip_addresses(ip_list, limit=5):
    reachable = []
    unreachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(ping_ip, ip_list)
    for ip, status in zip(ip_list, results):
        if status:
            reachable.append(ip)
        else:
            unreachable.append(ip)
    return reachable, unreachable


def cisco_get_hostname_sn(device):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        output = ssh.send_command("sh version")
        match_sn = re.search(r"Processor board ID (\S+)", output)
        if match_sn:
            sn = match_sn.group(1)
        else:
            sn = None
        prompt = ssh.find_prompt()
        hostname = re.search(r"(\S+)[>#]", prompt).group(1)
    return (device["host"], hostname, sn)


def get_host_sn_write_to_file(devices, filename, limit=10):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        results = executor.map(cisco_get_hostname_sn, devices)
        with open(filename, "w") as f:
            wr = csv.writer(f)
            wr.writerow("ip hostname serialnumber".split())
            for output in results:
                wr.writerow(output)


def main():
    # vendor_device_type_map = {
    #     "Cisco": "cisco_ios"
    # }
    command = "sh ip int br"
    with open("devices.csv") as f:
        reader = csv.DictReader(f)
        cisco_only = [row["ip"] for row in reader if row["vendor"] == "Cisco"]

    base_params = {
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
        "device_type": "cisco_ios",
        "timeout": 10,
    }
    devices = [{**base_params, "host": ip} for ip in cisco_only]
    get_host_sn_write_to_file(devices, "cisco_params_results.csv")

if __name__ == "__main__":
    main()
