# Get free dynamic / registered ports 


### Tested against Windows 10 / Python 3.10 / Anaconda

### pip install get-free-port


from https://www.techtarget.com/searchnetworking/definition/dynamic-port-numbers

The registries for these protocols are divided into three categories,
 based on the available range of numbers (0 to 65535):

System ports, also known as well-known ports, include ports 0 to 1023 and 
support commonly used services.
User ports, also known as registered ports, include ports 1024 to 49151 and 
are assigned to specific services, based on service applications submitted to IANA.
Dynamic ports, also known as private or ephemeral ports, include 
ports 49152 to 65535 and are never assigned.

```python
from get_free_port import get_dynamic_ports, get_registered_ports
print(get_dynamic_ports(3))
print(get_registered_ports(3))
[49152, 49153, 49154]
[1025, 1026, 1027]
```