# RAG-n-Roll-Extractor

A professional Retrieval-Augmented Generation (RAG) extraction tool that helps process and prepare documents for RAG applications.

## Architecture

![RAG Architecture](assets/RAG.png)

*Image source: [LangChain Cookbook - Semi-structured and Multi-modal RAG](https://github.com/langchain-ai/langchain/blob/master/cookbook/Semi_structured_and_multi_modal_RAG.ipynb)*

## Features

- [Coming soon]

## Installation

### System Dependencies (Windows)

1. Install Poppler for PDF processing:
   ```powershell
   # Using Chocolatey (recommended)
   choco install poppler

   # OR download from: http://blog.alivate.com.au/poppler-windows/
   # and add the bin/ directory to your PATH
   ```

2. Install Tesseract OCR:
   ```powershell
   # Using Chocolatey (recommended)
   choco install tesseract
   
   # OR download installer from: https://github.com/UB-Mannheim/tesseract/wiki
   # and add the installation directory to your PATH
   ```

3. Install Chocolatey (if not already installed):
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

### Python Package Installation

```bash
# Clone the repository
git clone https://github.com/andykofman/RAG-n-Roll-Extractor.git
cd RAG-n-Roll-Extractor

# Install using Poetry
poetry install
```

## Usage

[Coming soon]

## Project Structure

```
src/
└── rag_n_roll_extractor/
    └── __init__.py
```

## Development

### Setup Development Environment

```bash
# Install development dependencies
poetry install --with dev
```

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

[MIT License](LICENSE)

## Authors

- A.Ali (ali.a@aucegypt.edu) 