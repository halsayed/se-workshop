


# Deploying NKP and NAI

This section will guide you through the process of deploying the Nutanix Kubernetes Platform (NKP) and Nutanix Enterprise AI (NAI) on a Hosted POC (HPOC). We will be following the best practices and procedures outlined in the [NAI on NKP Tutorial](https://nai.howntnx.win/iep/).

## NKP High-Level Cluster Design

The `nkpdev` cluster will be hosting the LLM model serving endpoints and AI application stack. This cluster and will require a dedicated GPU node pool.

### Sizing Requirements

Below are the sizing requirements needed to successfully deploy NAI on a NKP Cluster (labeled as `nkpdev`) and subsequently deploying single LLM inferencing endpoint on NAI using the `meta-llama/Meta-Llama-3-8B-Instruct` LLM model.

| Role | No. of Nodes (VM) | vCPU per Node | Memory per Node | Storage per Node | Total vCPU | Total Memory |
| --- | --- | --- | --- | --- | --- | --- |
| Control plane | 3 | 4 | 16 GB | 150 GB | 12 | 48 GB |
| Worker | 4 | 8 | 32 GB | 150 GB | 32 | 128 GB |
| GPU | 1 | 16 | 40 GB | 300 GB | 16 | 40 GB |
| **Totals** | **8** | **60** | **216 GB** | | | |

### GPU Resource Calculations

*   To host a 8b(illion) parameter model, multiply the parameter number by 2 to get minimum GPU memory requirments. e.g. 16GB of GPU memory is required for 8b parameter model.

> So in the case of the `meta-llama/Meta-Llama-3-8B-Instruct` model, you'll need a min. 16 GiB GPU vRAM available

Below are additional sizing consideration "Rule of Thumb" for further calculating min. GPU node resources:

*   For each GPU node will have 8 CPU cores, 24 GB of memory, and 300 GB of disk space.
*   For each GPU attached to the node, add 16 GiB of memory.
*   For each endpoint attached to the node, add 8 CPU cores.
*   If a model needs multiple GPUs, ensure all GPUs are attached to the same worker node
*   For resiliency, while running multiple instances of the same endpoint, ensure that the GPUs are on different worker nodes.

Since we will be testing with the `meta-llama/Meta-Llama-3-8B-Instruct` HuggingFace model, we will require a GPU with a min. of 24 GiB GPU vRAM available to support this demo.

## Pre-requisites for NKP Deployment

1.  Existing Ubuntu Linux jumphost VM.
2.  Docker or Podman installed on the jumphost VM
3.  Nutanix PC is at least `2024.3`
4.  Nutanix AOS is at least `6.8+`, `6.10`
5.  Download and install `nkp` binary from Nutanix Portal
6.  Find and reserve 3 IPs for control plane and MetalLB access from AHV network
7.  Find GPU details from Nutanix cluster
8.  Create a base image to use with NKP nodes using `nkp` command

## Deployment Steps

We will now walk through the high-level steps for deploying NKP and NAI. Detailed instructions will be provided in the hands-on lab.

1.  **Install NKP Binaries**: Download and install the `nkp` binary on your jumphost.
2.  **Setup Docker on Jumphost**: Ensure Docker is installed and running on your jumphost.
3.  **Reserve Control Plane and MetalLB IP**: Reserve the necessary IP addresses for the NKP control plane and MetalLB.
4.  **Create Base Image for NKP**: Create a base image for the NKP nodes using the `nkp` command.
5.  **Create NKP Workload Cluster**: Create the NKP workload cluster using the `nkp` command.
6.  **Licensing**: Generate and apply the NKP Pro license to the cluster.
7.  **Add NKP GPU Workload Pool**: Add a GPU workload pool to the cluster to support our AI workloads.
8.  **Enable GPU Operator**: Enable the GPU operator on the cluster to manage the GPU resources.
9.  **Deploy NAI**: Deploy Nutanix Enterprise AI on the NKP cluster using Helm.
10. **Test NAI**: Test the NAI deployment by importing and deploying an LLM.


