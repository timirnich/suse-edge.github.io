# SUSE Telco Cloud Documentation Migration & Refactoring Matrix

This document maps the legacy, component-oriented AsciiDoc files of SUSE Telco Cloud 3.6 to the new, lifecycle-driven structure. Use this mapping schema to guide manual refactoring or to feed into Gemini Code Assist scripting tasks.

| Source File Path (Legacy 3.6) | New Target Path | New Target Header / Context | Refactoring Action Required |
| :--- | :--- | :--- | :--- |
| atip-architecture.adoc | architecture/high-level-architecture.adoc | Part I: Ch 1 - High-Level Architecture and Main Components | Move & Refactor: Remove edge-specific terminology, update architectural diagrams to show core-to-edge pathways. |
| N/A (New Concept) | architecture/paradigms-gitops-capi.adoc | Part I: Ch 2 - Key Paradigms: Declarative Infrastructure, GitOps, and Cluster API (CAPI) | Net New: Draft concepts focusing on Cluster API (CAPI) as the main IaC interface. |
| product/atip-automated-provision.adoc (Topologies snippet) | architecture/deployment-topologies.adoc | Part I: Ch 3 - Supported Deployment Topologies (Single-Node, Multi-Node HA, Air-Gapped) | Extract: Extract topological concepts from the legacy quickstart and consolidate here. |
| product/atip-requirements.adoc | requirements/hardware-network-prereqs.adoc | Part I: Ch 4 - Hardware & Network Prerequisites | Merge: Combine hardware, network, port, and systemd service files into a single guide. |
| product/atip-requirements.adoc | requirements/hardware-network-prereqs.adoc | Part I: Ch 4 | Merge: Combine into hardware-network-prereqs.adoc. |
| product/atip-requirements.adoc | requirements/hardware-network-prereqs.adoc | Part I: Ch 4 | Merge: Combine into hardware-network-prereqs.adoc. |
| product/atip-requirements.adoc | requirements/hardware-network-prereqs.adoc | Part I: Ch 4 | Merge: Combine into hardware-network-prereqs.adoc. |
| product/atip-requirements.adoc | requirements/hardware-network-prereqs.adoc | Part I: Ch 4 | Merge: Combine into hardware-network-prereqs.adoc. |
| atip-management-cluster.adoc (Intro) | management-plane/architecture.adoc | Part II: Ch 5 - Management Cluster Architecture | Extract: Separate the management architecture conceptual pages from the setup guide. |
| atip-management-cluster.adoc (Setup/Prep) | management-plane/deploying-management.adoc | Part II: Ch 6 - Deploying the Management Plane | Move & Clean: Clean up step-by-step installation logs and automate configuration updates. |
| components-rancher.adoc (RBAC configs) | management-plane/identity-iam.adoc | Part II: Ch 7 - Integrating Identity & Access Management (RBAC) | Extract: Move Rancher RBAC and user authorization rules into a dedicated IAM chapter. |
| components-fleet.adoc | ztp-fleet/gitops-architecture.adoc | Part III: Ch 8 - GitOps for Telco Infrastructure | Refactor: Reframe "Fleet" from a simple edge component to a core/edge distributed GitOps strategy. |
| components-edge-image-builder.adoc | ztp-fleet/edge-image-builder-concepts.adoc | Part III: Ch 9 - Building Bare-Metal OS Images (EIB) | Merge & Update: Incorporate elements from the old standalone builder guide here. |
| quickstart/eib.adoc | ztp-fleet/edge-image-builder-concepts.adoc | Part III: Ch 9 | Merge: Consolidate quickstart code examples into the primary EIB chapter. |
| components-metal3.adoc | ztp-fleet/metal3-automation.adoc | Part III: Ch 10 - Bare-Metal Infrastructure Automation | Move: Rename from edge focus to broader bare-metal infrastructure orchestration. |
| quickstart/metal3.adoc | ztp-fleet/metal3-automation.adoc | Part III: Ch 10 | Merge: Blend the BMC quickstart directly into the main Metal3 automation chapter. |
| product/atip-automated-provision.adoc (Single Node) | ztp-fleet/provisioning-connected-ztp.adoc | Part III: Ch 11 - Provisioning Connected Telco Clusters | Extract & Refactor: Re-orient downstream cluster setups as standard, connected ZTP patterns. |
| product/atip-automated-provision.adoc (Air-gapped specs) | ztp-fleet/provisioning-airgapped-ztp.adoc | Part III: Ch 12 - Provisioning Air-Gapped Telco Clusters | Extract: Focus purely on the seactl/air-gapped registry and disconnected workflow. |
| components/linux-micro.adoc | tuning-performance/realtime-kernel.adoc | Part IV: Ch 13 - Real-Time Kernel & OS Tuning (SLE Micro) | Refactor: Re-anchor SLE Micro as the real-time foundation of the telco stack. |
| N/A (Under-documented) | tuning-performance/numa-cpu-tuning.adoc | Part IV: Ch 14 - CPU Pinning, NUMA, and HugePages | Net New: Capture configurations from deployment whitepapers (such as Intel FlexRAN setups). |
| N/A (Missing capability) | tuning-performance/ptp-configuration.adoc | Part IV: Ch 15 - Precision Time Protocol (PTP) | Net New: Provide PTP configurations, clock synchronization, and verification commands. |
| components-edge-networking.adoc | telco-networking/advanced-multus.adoc | Part V: Ch 16 - Advanced Networking with Multus CNI | Rename & Refactor: Clean up NetworkManager guides and anchor around Multus CNI. |
| N/A (Under-documented) | telco-networking/sriov-dpdk-acceleration.adoc | Part V: Ch 17 - SR-IOV & DPDK Hardware Acceleration | Net New: Provide complete device-binding policies and virtual-function setups. |
| components-metallb.adoc | telco-networking/loadbalancing-sctp.adoc | Part V: Ch 18 - Load Balancing (MetalLB) & SCTP | Merge: Combine MetalLB settings with SCTP support protocols. |
| components-system-upgrade-controller.adoc | day-2-ops/declarative-upgrades.adoc | Part VI: Ch 19 - Declarative Cluster Upgrades | Merge: Combine System Upgrade Controller and general upgrade engine logic. |
| components-upgrade-controller.adoc | day-2-ops/declarative-upgrades.adoc | Part VI: Ch 19 | Merge: Combine into a unified upgrade mechanics overview. |
| product/atip-automated-provision.adoc (Scaling nodes) | day-2-ops/scaling-node-replacement.adoc | Part VI: Ch 20 - Scaling Clusters & Node Replacement | Extract: Create an operational playbook for horizontal scaling of the nodes. |
| N/A (Missing capability) | day-2-ops/backup-restore.adoc | Part VI: Ch 21 - Backup, Restore, and Disaster Recovery | Net New: Document disaster recovery patterns (etcd backups, Longhorn snapshots). |
| components-endpoint-copier-operator.adoc | day-2-ops/cert-management.adoc | Part VI: Ch 22 - Certificate Management & Rotation | Refactor: Focus on exposing APIs, keeping VIP certificates up to date, and rotated keys. |
| N/A (Missing capability) | observability-security/platform-telemetry.adoc | Part VII: Ch 23 - Platform Telemetry & Tracing | Net New: Document Prometheus exporter tuning for real-time kernels and logging. |
| components/neuvector.adoc | observability-security/infrastructure-hardening.adoc | Part VII: Ch 24 - Infrastructure Security Hardening | Refactor: Anchor around NeuVector capabilities and CIS benchmark profiles. |
| components-fleet.adoc (Debugging) | observability-security/troubleshooting-diagnostics.adoc | Part VII: Ch 25 - Troubleshooting & Diagnostics | Merge: Gather all distributed cluster diagnostics and log retrieval patterns. |
| N/A (Placeholder) | workloads/cnf-onboarding.adoc | Part VIII: Ch 26 - CNF Onboarding | Future-Ready Placeholder: Blank conceptual blueprint. |
| components-edge-virtualization.adoc | workloads/virtualized-network-functions.adoc | Part VIII: Ch 27 - Virtualized Network Functions (KubeVirt) | Refactor: Shift focus from general edge virtualization to core VM network function hosting. |
| components-rancher-dashboard-extensions.adoc | workloads/virtualized-network-functions.adoc | Part VIII: Ch 27 | Merge: Fold KubeVirt dashboard extensions directly into the VM provisioning guide. |
| N/A (Placeholder) | standards/oran-alliance-compliance.adoc | Part VIII: Ch 28 - O-RAN Alliance Compliance Framework | Future-Ready Placeholder: Blank conceptual blueprint. |