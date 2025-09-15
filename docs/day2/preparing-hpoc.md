


# Preparing HPOC for NAI Workshop

This section provides a guide for preparing a Hosted POC (HPOC) for delivering the Nutanix Enterprise AI workshop. This will ensure that you have a consistent and reliable environment for your workshop participants.

## HPOC Configuration

To prepare your HPOC for the NAI workshop, you will need to perform the following tasks:

1.  **Create a new project**: Create a new project in Nutanix Prism Central for the workshop.
2.  **Create a new user**: Create a new user in Nutanix Prism Central for the workshop participants.
3.  **Assign the user to the project**: Assign the user to the project with the appropriate permissions.
4.  **Create a new virtual machine**: Create a new virtual machine for the jumphost.
5.  **Install Docker on the jumphost**: Install Docker on the jumphost.
6.  **Install the `nkp` binary on the jumphost**: Install the `nkp` binary on the jumphost.
7.  **Reserve IP addresses**: Reserve the necessary IP addresses for the NKP control plane and MetalLB.
8.  **Create a base image for NKP**: Create a base image for the NKP nodes.

## Workshop Cleanup

After the workshop is complete, you will need to clean up the HPOC environment. This will ensure that the environment is ready for the next workshop.

1.  **Delete the NKP cluster**: Delete the NKP cluster.
2.  **Delete the base image**: Delete the base image.
3.  **Delete the jumphost**: Delete the jumphost.
4.  **Delete the project**: Delete the project.
5.  **Delete the user**: Delete the user.

By following these steps, you can ensure that you have a consistent and reliable environment for delivering the Nutanix Enterprise AI workshop.


