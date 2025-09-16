


# Hands-on Lab: Deploying NKP + NAI

## Workshop Resources

### Presentation Slides
- [05_SE_NAI_NAI_Hands-on_workshop_v1_02-06-2025.pptx](https://nutanixinc-my.sharepoint.com/:p:/r/personal/husain_ebrahim_nutanix_com/Documents/workshops/se_nai_workshop/slides/05_SE_NAI_NAI_Hands-on_workshop_v1_02-06-2025.pptx?d=w00c4654901584f1b995a78c21dd25aa0&csf=1&web=1&e=7GD1Q4)

### Deployment Summary Documents
- [nai_full_deployment_nai2.3_v1.docx](https://nutanixinc-my.sharepoint.com/:w:/r/personal/husain_ebrahim_nutanix_com/Documents/workshops/se_nai_workshop/assets/nai_full_deployment_nai2.3_v1.docx?d=wd86810758dbe48af98915108c3102a18&csf=1&web=1&e=3I1E3D)
- [nai_full_deployment_nai2.4_v2.docx](https://nutanixinc-my.sharepoint.com/:w:/r/personal/husain_ebrahim_nutanix_com/Documents/workshops/se_nai_workshop/assets/nai_full_deployment_nai2.4_v2.docx?d=wf755d704ae724b11a4486a7297a26d5c&csf=1&web=1&e=44hr5v)

---

This hands-on lab will guide you through the process of deploying the Nutanix Kubernetes Platform (NKP) and Nutanix Enterprise AI (NAI). We will be following the detailed instructions provided in the [NAI on NKP Tutorial](https://nai.howntnx.win/iep/).

## Lab Objectives

By the end of this lab, you will have:

*   Deployed a Nutanix Kubernetes Platform (NKP) cluster.
*   Installed and configured Nutanix Enterprise AI (NAI) on the NKP cluster.
*   Imported and deployed a Large Language Model (LLM).
*   Created and tested an inference endpoint.

## Lab Instructions

We will be following the instructions in the [NAI on NKP Tutorial](https://nai.howntnx.win/iep/). Please open the tutorial in a new browser tab and follow the steps outlined in the following sections:

1.  **Setup NKP Cluster**: This section will guide you through the process of deploying the NKP cluster.
    *   [Setup NKP Cluster](https://nai.howntnx.win/infra/infra_nkp/)

2.  **Pre-requisites NAI**: This section covers the prerequisites for installing NAI.
    *   [Pre-requisites NAI](https://nai.howntnx.win/iep/nai_pre_reqs/)

3.  **Deploy NAI**: This section will guide you through the process of deploying NAI on the NKP cluster.
    *   [Deploy NAI](https://nai.howntnx.win/iep/deploy_nai/)

4.  **Test NAI**: This section will guide you through the process of testing the NAI deployment.
    *   [Test NAI](https://nai.howntnx.win/iep/test_nai/)

## Key Commands and Configurations

Throughout the lab, you will be using a variety of commands and configurations. Here are some of the key commands and configurations that you will be using:

### NKP Cluster Creation

```bash
# Create the NKP workload cluster
nkp create cluster -f nkp-workload-cluster.yaml
```

### NAI Helm Chart Installation

```bash
# Add the Nutanix Helm repository
helm repo add nutanix https://nutanix.github.io/helm/

# Update the Helm repository
helm repo update

# Install the NAI Helm chart
helm install nai nutanix/nai -n nai --create-namespace -f values.yaml
```

### LLM Import

```bash
# Import the Llama 3 8B Instruct model
ai-cli model import --name llama3-8b-instruct --from-huggingface meta-llama/Llama-3-8B-Instruct
```

### Inference Endpoint Creation

```bash
# Create an inference endpoint for the Llama 3 model
ai-cli endpoint create --name llama3-8b-instruct --model llama3-8b-instruct --gpus 1
```

Good luck with the lab! Ask your instructor if you have any questions.


