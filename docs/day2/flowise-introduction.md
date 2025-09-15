


# Flowise.ai Introduction

In this section, we will introduce you to Flowise, a low-code/no-code tool for building AI-powered workflows and applications. We will be using Flowise to build a Retrieval-Augmented Generation (RAG) chatbot that can answer questions about your own private data.

## What is Flowise?

Flowise is an open-source, low-code tool that enables developers to build customized LLM orchestration flows and AI agents on top of LangChain and/or LlamaIndex. LangChain and LlamaIndex are frameworks for simplifying the development of AI applications.

## How does Flowise work?

Flowise provides a visual interface for building AI-powered workflows. You can drag and drop different nodes onto a canvas and connect them to create a workflow. Each node represents a specific function, such as a language model, a document loader, or a vector store.

## Chatbot Flow

The following diagram illustrates the flow of a chatbot built with Flowise:

![Chatbot Flow](assets/chatbot-flow.png)

1.  **Ask Question**: The user asks a question to the chatbot.
2.  **Send Prompt to Inference API**: The chatbot sends the user's question to the Nutanix Enterprise AI inference endpoint.
3.  **Get Answer**: The chatbot receives a response from the inference endpoint and displays it to the user.

## Steps to Create a Chatbot

In the next section, we will walk you through the process of creating a chatbot with Flowise. Here are the high-level steps:

1.  **Gather information from Nutanix Enterprise AI**: You will need to gather the endpoint details from your Nutanix Enterprise AI instance.
2.  **Create a Chatflow in Flowise**: You will create a new chatflow in the Flowise application.
3.  **Add, configure, and connect nodes in the chatflow**: You will add and configure the necessary nodes to create your chatbot.
4.  **Test the chatflow**: You will test your chatbot to ensure that it is working correctly.


