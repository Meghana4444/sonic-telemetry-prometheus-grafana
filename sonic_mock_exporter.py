import time
from prometheus_client import start_http_server, Gauge

tx_metric = Gauge(
    'sonic_interface_tx',
    'SONiC Interface TX Packets',
    ['interface']
)

interfaces = ['Ethernet0', 'Ethernet4']
counter = {i: 0 for i in interfaces}

start_http_server(8001)
print("SONiC Mock Exporter running at http://localhost:8001/metrics")

while True:
    for iface in interfaces:
        counter[iface] += 100
        tx_metric.labels(interface=iface).set(counter[iface])
    time.sleep(5)
