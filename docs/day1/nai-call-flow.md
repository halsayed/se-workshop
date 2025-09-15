





# Typical NAI Call Flow

This section provides a step-by-step guide to using Nutanix Enterprise AI, from logging in to deploying and testing a Large Language Model (LLM). This workflow is based on the NAI demo video and will be the basis for our hands-on lab.

### 1. Logging In and Dashboard Overview

First, connect to your corporate VPN and navigate to the Nutanix Enterprise AI portal to log in.

*   **URL:** `ai.nutanix.com`

![NAI Login](assets/nai_demo_login_animation.gif)

Once logged in, you will see the main **Dashboard**. This provides a comprehensive overview of your AI environment, including:
*   **Endpoints Summary:** Shows the status of your deployed models (Active, Failed, Pending).
*   **Infrastructure Summary:** Displays the health and resource utilization (Memory, CPU, Disk, GPUs) of the underlying Kubernetes cluster.
*   **API Requests Summary & Trends:** Tracks the number of successful and failed API calls to your models over time.

### 2. Monitoring Infrastructure Health

For a deeper look into your resource usage, you can inspect the infrastructure details. This is especially useful for administrators who need to monitor GPU performance and overall cluster health.

1.  On the main **Dashboard**, under the **Infrastructure Summary** pane, click **View Usage Details**.
2.  This view shows historical data for memory and CPU usage. To see GPU-specific metrics, select a GPU worker node from the **Cluster** dropdown menu.
3.  You can now monitor the **GPU Utilization** and **GPU Memory Usage** for the selected node.

### 3. Importing a Language Model (LLM)

Nutanix Enterprise AI simplifies the process of bringing models into your environment. You can import validated models directly from popular hubs like Hugging Face.

1.  From the left-hand navigation menu, click on **Models**.
2.  Click the **Import Models** button.
3.  Select **From Hugging Face Model Hub**. A list of validated models that have been tested to run on Nutanix Enterprise AI will appear.
4.  Choose a model from the list.
5.  In the pop-up window, provide a **Model Instance Name**.
6.  Click **Import**. The model's status will change to `Pending` as it is downloaded and prepared in the background.

### 4. Creating and Deploying a Model Endpoint

Once a model is imported, you need to create an endpoint to make it accessible for applications to use. The endpoint is the live, running instance of your model.

1.  Navigate to the **Endpoints** tab from the left-hand menu.
2.  Click the **Create Endpoint** button.
3.  Fill out the required details:
    *   **Endpoint Name:** A unique name for your deployment.
    *   **Model Instance Name:** Select the model you just imported from the dropdown list.
    *   **Number of GPUs (Per Instance):** Assign the number of GPUs for the model to use.
    *   **GPU Card:** Select the type of GPU card available in your cluster.
    *   **Number of Instances:** Define how many copies of the model should run for high availability.
4.  Click **Create**. The endpoint status will be `Pending` while the resources are allocated and the model is deployed.

### 5. Testing the Endpoint and Creating an API Key

After the endpoint becomes `Active`, you can test it directly from the UI and create API keys for developers to use in their applications.

**To Test the Endpoint:**
1. Click on your active endpoint from the list.
2. In the endpoint overview screen, click the **Test** button at the top.
3. Select a sample request or write a custom one, then click **Test** to see the model's response in real-time.

**To Create an API Key:**
1. Navigate to the **Endpoints** tab and select the **API Keys** sub-tab.
2. Click **Create API Key**.
3. Give the key a name (e.g., `demo-app-key`) and select the endpoint(s) it should have access to.
4. Click **Create**. Copy the generated API key and store it securely, as it will not be shown again.

### 6. Integrating with an Application (Example: AI Chatbot)

Nutanix Enterprise AI is compatible with the OpenAI API standard, making it easy to switch your existing applications from public cloud services to your private on-prem models with minimal code changes.

To reconfigure an existing application, you only need to update three pieces of information:
1.  **API Endpoint URL:** Change this from the public URL (e.g., `api.openai.com`) to your Nutanix AI endpoint URL.
2.  **Model Name:** Change this to the name of your deployed endpoint (e.g., `vllm-llama-3-1`).
3.  **API Key:** Replace the existing key with the new one you generated on the Nutanix AI platform.

### 7. Advanced Use Case: Creating an AI Agent

You can transform your LLM into a powerful AI agent capable of performing tasks by providing specific instructions in the **System Message**. This allows the model to interact with other tools and APIs.

In this example, the chatbot is instructed to act as a tool for creating virtual machines. When a user makes a request in natural language, the model extracts the necessary information, fills in the blanks with default values, and generates a structured **JSON output**. This JSON can then be passed to the Nutanix Prism Central API to automate the VM creation process.


