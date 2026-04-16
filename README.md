AI Resume Analyzer (RAG-Based Project)

Overview

This project is an AI-powered Resume Analyzer that evaluates a resume against a job description and provides an ATS score, identifies missing skills, and suggests improvements.

The system uses **Retrieval-Augmented Generation (RAG)** to ensure accurate and context-aware responses.
Tech Stack

Python
LangChain
Google Gemini API (LLM + Embeddings)
Pinecone (Vector Database)

Features

* Extracts text from resume (PDF)
* Splits text into meaningful chunks
* Generates embeddings using Gemini
* Stores and retrieves data using Pinecone
* Performs semantic search for relevant context
* Generates ATS score and improvement suggestions

Project Structure

resume_analyzer/
│── main.py
│── config.py
│── services/
│── utils/
│── requirements.txt

Author:
Neha Singh
