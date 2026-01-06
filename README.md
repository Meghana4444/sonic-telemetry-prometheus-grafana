# Next-Gen SONiC Telemetry using Prometheus and Grafana

## Abstract
Modern data centers and cloud networks require continuous visibility into network performance to ensure reliability, scalability, and low latency. Traditional monitoring techniques are reactive and fail to provide real-time insights.

This project presents a real-time telemetry monitoring system inspired by SONiC, using a lightweight Python exporter to expose network interface metrics. These metrics are collected by Prometheus and visualized through Grafana dashboards, enabling proactive monitoring and faster decision-making.

The solution demonstrates an industry-grade, cloud-native telemetry pipeline in a simplified and extensible form, making it suitable for education, rapid prototyping, and future large-scale deployment.

## Problem Statement
Traditional network monitoring systems are reactive and slow.

## Objective
To build a scalable and real-time telemetry monitoring system.

## Architecture Diagram
Network Telemetry Source -> Exporter → Prometheus → Grafana → User ![Architecture](screenshots/architecture.png)
- Python-based telemetry exporter
- Prometheus for metric collection
- Grafana for visualization

## Metrics Used
- sonic_interface_tx

## Results
Real-time interface traffic visualization using Prometheus and Grafana.

## Future Scope
- Integration with real SONiC Redis DB
- AI-based anomaly detection
- Alerting using Alertmanager





