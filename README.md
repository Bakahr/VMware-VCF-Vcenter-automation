# VMware-VCF-Vcenter-automation

This repository serves as a **Toolkit** for automating the lifecycle, health, and configuration of VMware Cloud Foundation (VCF) and vSphere environments. 

In modern SDDC (Software-Defined Data Center) environments, manual configuration is a risk. This project focuses on **Infrastructure as Code (IaC)** and **API-driven validation** to ensure "Cloud-Ready" deployments.


### 1. VCF Pre-Flight Validator (Python)
Automated checks for common VCF deployment "show-stoppers":
* **MTU 9000 (Jumbo Frames)** validation across Distributed Virtual Switches.
* **NTP/DNS Consistency**: Ensuring time sync and resolution across all ESXi hosts and management components.
* **VLAN Tagging**: Verification of port group configurations against the VCF planning guide.

### 2. vCenter Health & Security Audit (C#)
A structured approach to environment hardening:
* Audit of SSH status and Shell timeouts across the cluster.
* Password policy enforcement checks.
* Identification of orphaned VMDKs and snapshots to optimize storage before VCF migration.
