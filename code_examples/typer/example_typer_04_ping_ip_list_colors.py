import subprocess
from typing import List
import typer


def ping_ip(ip_address, count):
    """
    Ping IP_ADDRESS and return True/False
    """
    reply = subprocess.run(
        f"ping -c {count} -n {ip_address}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    if reply.returncode == 0:
        return True
    else:
        return False


def ping_ip_addresses(ip_addresses, count):
    reachable = []
    unreachable = []
    with typer.progressbar(ip_addresses, label="Пингую адреса") as bar:
        for ip in bar:
            if ping_ip(ip, count):
                reachable.append(ip)
            else:
                unreachable.append(ip)
    return reachable, unreachable


def main(ip_addresses: List[str], count: int):
    """
    Ping IP_ADDRESS
    """
    reachable, unreachable = ping_ip_addresses(ip_addresses, count)
    for ip in reachable:
        typer.secho(f"IP-адрес {ip:15} пингуется", fg="green", bold=True)
    for ip in unreachable:
        typer.secho(f"IP-адрес {ip:15} не пингуется", fg="red", bold=True)


if __name__ == "__main__":
    typer.run(main)

"""
$ python example_03_ping_ip_list_progress_bar.py 8.8.8.8 8.8.4.4 10.1.1.1 192.168.100.1
Пингую адреса  [####################################]  100%
IP-адрес 8.8.8.8         пингуется
IP-адрес 8.8.4.4         пингуется
IP-адрес 192.168.100.1   пингуется
IP-адрес 10.1.1.1        не пингуется

"""
