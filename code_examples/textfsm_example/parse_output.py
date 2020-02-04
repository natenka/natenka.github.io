import sys
import textfsm
from tabulate import tabulate
from pprint import pprint

template = sys.argv[1]
output_file = sys.argv[2]

with open(template) as f, open(output_file) as output:
    re_table = textfsm.TextFSM(f)
    header = re_table.header
    result = re_table.ParseText(output.read())
    print(tabulate(result, headers=header), end='\n\n')

# create dict
results = [dict(zip(header, row)) for row in result]
pprint(results)

'''
$ python parse_output.py template_example.txt data_example.txt
Name        Type       Binding                                               Description
----------  ---------  ----------------------------------------------------  -------------
EVERFLOW    MIRROR     ['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4']  EVERFLOW
SNMP_ACL    CTRLPLANE  ['SNMP']                                              SNMP_ACL
SSH_ONLY    CTRLPLANE  ['SSH']                                               SSH_ONLY
EVERFLOWV6  MIRRORV6   ['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4']  EVERFLOWV6

[{'Binding': ['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4'],
  'Description': 'EVERFLOW',
  'Name': 'EVERFLOW',
  'Type': 'MIRROR'},
 {'Binding': ['SNMP'],
  'Description': 'SNMP_ACL',
  'Name': 'SNMP_ACL',
  'Type': 'CTRLPLANE'},
 {'Binding': ['SSH'],
  'Description': 'SSH_ONLY',
  'Name': 'SSH_ONLY',
  'Type': 'CTRLPLANE'},
 {'Binding': ['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4'],
  'Description': 'EVERFLOWV6',
  'Name': 'EVERFLOWV6',
  'Type': 'MIRRORV6'}]
'''
