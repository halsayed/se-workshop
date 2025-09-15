


# Troubleshooting

This page provides solutions to common issues that you may encounter during the workshop.

## NKP Deployment Issues

### Issue: NKP cluster creation fails

**Symptoms**: The `nkp create cluster` command fails with an error.

**Solution**: 
1. Check that you have the correct permissions to create resources in the Nutanix cluster.
2. Verify that the base image has been created successfully.
3. Check that the IP addresses have been reserved correctly.

### Issue: GPU node is not recognized

**Symptoms**: The GPU node is not showing up in the cluster or the GPU operator is not working.

**Solution**:
1. Verify that the GPU node has been created with the correct GPU configuration.
2. Check that the GPU operator has been installed and is running.
3. Verify that the GPU drivers are installed on the node.

## NAI Deployment Issues

### Issue: NAI Helm chart installation fails

**Symptoms**: The `helm install` command fails with an error.

**Solution**:
1. Check that the Helm repository has been added correctly.
2. Verify that the values.yaml file is configured correctly.
3. Check that the namespace exists or use the `--create-namespace` flag.

### Issue: Model import fails

**Symptoms**: The model import process fails or gets stuck.

**Solution**:
1. Check that you have the correct permissions to access the Hugging Face model.
2. Verify that the model is supported by Nutanix Enterprise AI.
3. Check the network connectivity to the Hugging Face repository.

## Chatbot Deployment Issues

### Issue: Docker containers fail to start

**Symptoms**: The `docker compose up` command fails or the containers exit immediately.

**Solution**:
1. Check that Docker is installed and running.
2. Verify that the docker-compose.yaml file is configured correctly.
3. Check the Docker logs for error messages.

### Issue: Chatbot cannot connect to NAI

**Symptoms**: The chatbot interface loads but cannot connect to the NAI endpoint.

**Solution**:
1. Verify that the NAI endpoint URL is correct.
2. Check that the API key is valid and has the correct permissions.
3. Verify that the model name is correct.

## General Issues

### Issue: Network connectivity problems

**Symptoms**: Cannot access external resources or services.

**Solution**:
1. Check the network configuration of the jumphost.
2. Verify that the firewall rules are configured correctly.
3. Check the DNS configuration.

### Issue: Permission denied errors

**Symptoms**: Commands fail with permission denied errors.

**Solution**:
1. Check that you are running the commands with the correct user.
2. Verify that the user has the necessary permissions.
3. Use `sudo` if necessary.

If you encounter an issue that is not covered here, please ask your instructor for assistance.

