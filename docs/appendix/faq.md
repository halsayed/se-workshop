


# Frequently Asked Questions

This page provides answers to frequently asked questions about the workshop and Nutanix Enterprise AI.

## General Questions

### Q: What is the difference between Nutanix Enterprise AI and public cloud AI services?

**A:** Nutanix Enterprise AI provides a private, on-premises AI platform that gives you full control over your data and models. Unlike public cloud AI services, NAI ensures data sovereignty, predictable costs, and the ability to run AI workloads at the edge or in air-gapped environments.

### Q: Do I need to have prior experience with Kubernetes to attend this workshop?

**A:** While prior Kubernetes experience is helpful, it is not strictly required. However, you should have a basic understanding of containerization concepts and be comfortable using command-line tools.

### Q: Can I use Nutanix Enterprise AI with my existing Kubernetes cluster?

**A:** Yes, Nutanix Enterprise AI can be deployed on any CNCF-certified Kubernetes distribution, including your existing cluster. However, for optimal performance and support, we recommend using the Nutanix Kubernetes Platform (NKP).

## Technical Questions

### Q: What types of models can I deploy with Nutanix Enterprise AI?

**A:** Nutanix Enterprise AI supports a wide range of models, including Large Language Models (LLMs) from popular repositories like Hugging Face and NVIDIA NIM. You can also upload and deploy your own custom models.

### Q: How much GPU memory do I need to run a Large Language Model?

**A:** The GPU memory requirements depend on the size of the model. As a general rule of thumb, you need approximately 2 GB of GPU memory per billion parameters. For example, an 8B parameter model would require about 16 GB of GPU memory.

### Q: Can I run multiple models on the same GPU?

**A:** Yes, you can run multiple smaller models on the same GPU, provided that the total memory usage does not exceed the GPU's available memory. However, for optimal performance, it's recommended to run one model per GPU.

### Q: What is the difference between RAG and fine-tuning?

**A:** RAG (Retrieval-Augmented Generation) retrieves relevant documents from a knowledge base and uses them to augment the model's input, while fine-tuning involves retraining the model on a specific dataset. RAG is generally easier to implement and doesn't require retraining the model, while fine-tuning can provide better performance for specific tasks but requires more computational resources.

## Workshop-Specific Questions

### Q: What should I do if I encounter an error during the lab?

**A:** First, check the troubleshooting section of the workshop documentation. If you can't find a solution there, ask your instructor for assistance.

### Q: Can I access the lab environment after the workshop?

**A:** The lab environment is typically available only during the workshop. However, you can follow the instructions in the workshop documentation to set up your own environment.

### Q: Where can I find the workshop materials after the workshop?

**A:** The workshop materials will be available in the workshop documentation. You can also find additional resources in the external links section.

## Licensing and Deployment Questions

### Q: What are the different licensing options for Nutanix Enterprise AI?

**A:** Nutanix Enterprise AI offers several licensing options:
- **GPT-in-a-Box**: A complete, validated solution that includes hardware, software, and support.
- **Bare Metal / Bring-Your-Own Kubernetes**: Software-only licensing for deployment on your existing infrastructure.
- **Stand Alone (Public Cloud)**: Deployment on public cloud platforms like AWS, Azure, and GCP.

### Q: Can I deploy Nutanix Enterprise AI in a public cloud?

**A:** Yes, Nutanix Enterprise AI can be deployed natively in public clouds like AWS, Azure, and GCP, leveraging their native Kubernetes services and GPU instances.

### Q: How do I get support for Nutanix Enterprise AI?

**A:** Support for Nutanix Enterprise AI is available through the standard Nutanix support channels. You can also find additional resources and community support on the Nutanix Community forum.

If you have a question that is not answered here, please ask your instructor or contact Nutanix support.

