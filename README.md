# Claude Skill Repo

A curated collection of skills and tools designed to extend Claude's capabilities. This repository provides ready-to-use workflows, prompt templates, and integration guides for developers building AI-powered applications with Claude's API.

## 📋 Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Available Skills](#available-skills)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains a growing collection of skills that enhance Claude's functionality across various domains including:

- Document processing and analysis
- Code generation and review
- Data transformation and automation
- Creative writing and content generation
- Research and information synthesis
- Workflow automation templates

## 🚀 Getting Started

### Prerequisites

- Access to Claude API (via Anthropic Console)
- Basic understanding of prompt engineering
- Python 3.8+ (for automation scripts)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/andreapede/claude-skills.git
cd claude-skills
```

2. Install dependencies (if using automation scripts):
```bash
pip install -r requirements.txt
```

3. Set up your API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

## 📁 Repository Structure

```
claude-skills/
├── skills/              # Individual skill definitions
│   ├── document/        # Document processing skills
│   ├── code/           # Code-related skills
│   ├── creative/       # Creative writing skills
│   └── data/           # Data analysis skills
├── templates/          # Reusable prompt templates
├── examples/           # Usage examples and demos
├── scripts/            # Automation scripts
└── docs/              # Additional documentation
```

## 🛠️ Available Skills

### Document Processing
- **PDF Analysis**: Extract and analyze content from PDF documents
- **Markdown Converter**: Convert various formats to markdown
- **Summary Generator**: Create concise summaries of long documents

### Code Development
- **Code Review**: Automated code review with best practices
- **Documentation Generator**: Generate comprehensive code documentation
- **Bug Analyzer**: Identify and suggest fixes for common issues

### Data & Analytics
- **Data Transformer**: Convert and transform data between formats
- **Chart Generator**: Create visualizations from data
- **Report Builder**: Generate professional reports

### Creative Content
- **Content Writer**: Generate articles, blog posts, and copy
- **Story Generator**: Create creative narratives
- **SEO Optimizer**: Optimize content for search engines

## 💡 Usage

### Basic Example

```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

# Load a skill from the repository
with open('skills/document/pdf-analyzer.md', 'r') as f:
    skill_prompt = f.read()

# Use the skill
message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": f"{skill_prompt}\n\nAnalyze this document: [your document]"}
    ]
)

print(message.content)
```

### Using Templates

Templates are located in the `templates/` directory. Each template includes:
- Purpose and use case
- Input requirements
- Expected output format
- Customization options

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-skill`)
3. Add your skill with proper documentation
4. Test thoroughly with various inputs
5. Submit a pull request

### Skill Submission Guidelines

- Include clear documentation
- Provide usage examples
- Add test cases
- Follow the existing structure
- Update the main README

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [Anthropic Documentation](https://docs.anthropic.com)
- [Claude API Reference](https://docs.anthropic.com/en/api)
- [Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please open an issue or reach out through GitHub discussions.

---

⭐ If you find this repository helpful, please consider giving it a star!
