


# Lab Environment

This workshop will be conducted in a dedicated lab environment designed to provide you with a hands-on experience with Nutanix Enterprise AI. The lab environment consists of the following components:


## Lab Architecture

The lab environment is designed to mirror a real-world deployment of Nutanix Enterprise AI. The following diagram illustrates the high-level architecture of our lab:

```mermaid
graph TD
    A[Your Laptop] --> B{HPOC or Corporate VPN};
    B --> C[Shared GPU Pre-Configured Cluster];
    B --> D[Lab non-GPU Clusters];
    C --> F[https://demo.lab.ntnx.pro]
    D --> G[DM3]
    G --> H[DM3-POC100 https://10.54.28.7:9440/]
    G --> I[DM3-POC101 https://10.54.29.7:9440/]
    D --> J[PHX]
    J --> K[PHX-POC169 https://10.42.169.7:9440/]
    K --> L[PHX-POC287 https://10.38.59.7:9440/]
    J --> M[PHX-POC252 https://10.38.252.7:9440/]
    M --> N[PHX-POC255 https://10.42.153.7:9440/]
```

## POC Details

For detailed information about the lab environment, please refer to the POC detail sheet:

[POC Detail Sheet](https://docs.google.com/spreadsheets/d/17cVonaeUtIgAknOf8mUVkzwVG4BWZxwI6LtU5jMmTr8/edit?usp=sharing)

## Default Credentials

The default credentials for the GPU clusters are:

- **Username**: `admin`
- **Password**: `nx2Tech911!`


