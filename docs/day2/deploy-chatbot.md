


# Deploy Your First Chatbot

In this section, you will deploy your first chatbot using the skills you have acquired so far. We will be using the [Nutanix AI Demo GitHub repository](https://github.com/halsayed/nai-demo) to deploy a simple chatbot that integrates with the Nutanix Enterprise AI platform.

## Prerequisites

Before you begin, please ensure that you have completed the following prerequisites:

*   You have a running Nutanix Enterprise AI instance.
*   You have imported and deployed a Large Language Model (LLM).
*   You have created an inference endpoint for the LLM.
*   You have an API key for the inference endpoint.

## Deployment Instructions

We will be following the instructions in the [Nutanix AI Demo GitHub repository](https://github.com/halsayed/nai-demo). Please open the repository in a new browser tab and follow the instructions for your operating system.

### macOS Instructions

1.  Open your terminal.
2.  Clone the repository:
    ```shell
    git clone https://github.com/halsayed/nai-demo.git
    ```
3.  Navigate to the project directory:
    ```shell
    cd nai-demo
    ```
4.  Build the Docker containers:
    ```shell
    docker compose build
    ```
5.  Start the application:
    ```shell
    docker compose up
    ```
6.  Open your web browser and navigate to:
    ```
    http://localhost:8000
    ```
7.  To stop the application, press `Control + C`.

### Linux (Ubuntu) Instructions

*   Follow the [macOS instructions](#macos-instructions) to run the application.

### Windows Instructions

1.  Install WSL from an admin command/Powershell prompt by running `wsl --install`.
2.  Once installed and rebooted, open WSL and follow the instructions for [installing Docker on Linux](https://docs.docker.com/engine/install/ubuntu/).
3.  Exit WSL to allow the group change to take effect.
4.  Open WSL and continue with the [macOS instructions](#macos-instructions) to run the application.

## Configuration

Once the application is running, you will need to configure it to use your Nutanix Enterprise AI instance. To do this, you will need to update the following environment variables in the `docker-compose.yaml` file:

*   `NAI_API_ENDPOINT`: The URL of your Nutanix Enterprise AI inference endpoint.
*   `NAI_MODEL_NAME`: The name of your deployed LLM.
*   `NAI_API_KEY`: Your Nutanix Enterprise AI API key.

Once you have updated these environment variables, you will need to restart the application for the changes to take effect.

## Testing

Once the application is running and configured, you can test it by opening your web browser and navigating to `http://localhost:8000`. You should see a simple chatbot interface. You can now start chatting with your chatbot!


