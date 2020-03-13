## Структура каталога

```
my_scripts/
├── general
│   ├── __init__.py
│   └── parse_data.py
├── __init__.py
└── network
    ├── connect_ssh.py
    ├── connect_telnet.py
    └── __init__.py

```

## Пример использования

```python
In [1]: from my_scripts import send_command_and_parse_data

In [2]: device_dict = {
   ...:     'device_type': 'cisco_ios',
   ...:     'host': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'
   ...:     }

In [3]: template_path = "/home/vagrant/repos/pyneng-8/pyneng-online-jan-apr-2020/examples/22_textfsm/templates/sh_ip_int_br.template"

In [4]: send_command_and_parse_data(device_dict, "sh ip int br", template_path)
Out[4]:
[{'interface': 'Ethernet0/0',
  'ip': '192.168.100.1',
  'status': 'up',
  'protocol': 'up'},
 {'interface': 'Ethernet0/1',
  'ip': '192.168.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'interface': 'Ethernet0/2',
  'ip': '19.1.1.1',
  'status': 'up',
  'protocol': 'up'},
 {'interface': 'Ethernet0/3',
  'ip': '192.168.230.1',
  'status': 'up',
  'protocol': 'up'},
 {'interface': 'Loopback0', 'ip': '4.4.4.4', 'status': 'up', 'protocol': 'up'},
 {'interface': 'Loopback90',
  'ip': '90.1.1.1',
  'status': 'up',
  'protocol': 'up'}]

```
