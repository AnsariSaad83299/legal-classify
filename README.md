# 🧾 legal-classify — AI-Powered Legal Document Summarizer

LegiSort is a hybrid CLI + API application that leverages a fine-tuned transformer model to generate concise summaries of legal documents. It uses:

- ⚙️ **Scala 3 (via Scala CLI)** as a command-line interface for user interaction
- 🧠 **Hugging Face Transformers** for language modeling
- 🌐 **Flask API** as the bridge between Scala and the AI model

---

## 🚀 Features

- Summarizes complex legal judgments using a fine-tuned transformer (T5 or Legal-BERT)
- CLI-based interface for input/output (via Scala)
- REST API for clean language model integration (via Flask)
- Reads input from a file or user input, and writes summary to file or terminal
- Modular and easy to extend (batch, web UI, or cloud deployable)
