# Scripts Directory

This directory contains automation scripts and utility tools that help with the development, deployment, and management of Claude skills. These scripts streamline common tasks and provide convenient workflows for skill development.

## 🛠️ Script Categories

### Development Scripts
- **Skill Generator**: Create new skill templates and boilerplate code
- **Template Processor**: Process and validate prompt templates
- **Test Runner**: Execute automated tests for skills and examples
- **Documentation Builder**: Generate documentation from code and templates

### Deployment Scripts
- **Package Builder**: Bundle skills for distribution
- **Environment Setup**: Configure development and production environments
- **Dependency Manager**: Install and manage required packages
- **Configuration Validator**: Verify setup and configuration files

### Utility Scripts
- **File Converter**: Convert between different file formats
- **Batch Processor**: Process multiple files or datasets
- **API Client**: Simplified interface for Claude API interactions
- **Performance Monitor**: Track and analyze script performance

### Maintenance Scripts
- **Cleanup Tool**: Remove temporary files and clean workspace
- **Update Manager**: Update skills and dependencies
- **Backup Creator**: Create backups of important files
- **Link Checker**: Validate internal and external links

## 📁 Directory Structure

```
scripts/
├── dev/               # Development and testing scripts
├── deploy/            # Deployment and distribution scripts
├── utils/             # General utility scripts
├── maintenance/       # Maintenance and cleanup scripts
└── config/            # Configuration files for scripts
```

## 🚀 Getting Started

### Prerequisites
```bash
# Python 3.8 or higher
python --version

# Required packages
pip install -r scripts/requirements.txt

# Environment variables
export ANTHROPIC_API_KEY='your-api-key'
export CLAUDE_SKILLS_HOME='/path/to/claude-skills'
```

### Basic Usage
```bash
# Make scripts executable
chmod +x scripts/dev/create-skill.sh
chmod +x scripts/utils/batch-process.py

# Run a development script
./scripts/dev/create-skill.sh "data-analyzer" "data"

# Run a utility script
python scripts/utils/format-converter.py input.pdf output.md
```

## 🔧 Available Scripts

### Development Scripts

#### `create-skill.sh`
Creates a new skill with proper structure and boilerplate code.
```bash
./scripts/dev/create-skill.sh <skill-name> <category>
```

#### `test-runner.py`
Executes comprehensive tests for skills and examples.
```bash
python scripts/dev/test-runner.py --category data --verbose
```

#### `validate-templates.py`
Validates prompt templates for syntax and structure.
```bash
python scripts/dev/validate-templates.py templates/
```

### Deployment Scripts

#### `package-skills.py`
Creates distribution packages for skills.
```bash
python scripts/deploy/package-skills.py --output dist/ --format zip
```

#### `setup-environment.py`
Configures development environment with necessary dependencies.
```bash
python scripts/deploy/setup-environment.py --env development
```

### Utility Scripts

#### `batch-processor.py`
Processes multiple files using specified skills.
```bash
python scripts/utils/batch-processor.py \
  --skill document/pdf-analyzer \
  --input docs/ \
  --output results/
```

#### `api-client.py`
Simplified Claude API client for testing and development.
```bash
python scripts/utils/api-client.py \
  --prompt "Analyze this text" \
  --input sample.txt \
  --model claude-3-sonnet-20240229
```

#### `format-converter.py`
Converts files between different formats.
```bash
python scripts/utils/format-converter.py \
  --input document.pdf \
  --output document.md \
  --format markdown
```

### Maintenance Scripts

#### `cleanup.py`
Removes temporary files and cleans the workspace.
```bash
python scripts/maintenance/cleanup.py --deep --confirm
```

#### `update-dependencies.py`
Updates all dependencies to latest compatible versions.
```bash
python scripts/maintenance/update-dependencies.py --check-security
```

## ⚙️ Configuration

### Global Configuration (`scripts/config/global.json`)
```json
{
  "api": {
    "base_url": "https://api.anthropic.com",
    "model": "claude-3-sonnet-20240229",
    "max_tokens": 1000,
    "temperature": 0.7
  },
  "paths": {
    "skills_dir": "skills/",
    "templates_dir": "templates/",
    "examples_dir": "examples/",
    "output_dir": "output/"
  },
  "logging": {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/scripts.log"
  }
}
```

### Script-Specific Configuration
Each script can have its own configuration file in `scripts/config/`.

## 📊 Monitoring and Logging

### Log Files
- `logs/scripts.log`: General script execution logs
- `logs/api-usage.log`: Claude API usage tracking
- `logs/errors.log`: Error and exception logs
- `logs/performance.log`: Performance metrics and timing

### Monitoring Features
- API usage tracking and cost estimation
- Execution time measurement
- Success/failure rate monitoring
- Resource usage analysis

## 🔍 Testing and Validation

### Test Categories
- **Unit Tests**: Individual script component testing
- **Integration Tests**: End-to-end workflow testing
- **Performance Tests**: Speed and efficiency benchmarks
- **API Tests**: Claude API interaction validation

### Running Tests
```bash
# Run all tests
python scripts/dev/test-runner.py

# Run specific test category
python scripts/dev/test-runner.py --category unit

# Run tests with coverage
python scripts/dev/test-runner.py --coverage
```

## 🛡️ Error Handling

### Common Issues
- **API Key Missing**: Ensure `ANTHROPIC_API_KEY` is set
- **Permission Denied**: Check file permissions with `chmod +x`
- **Module Not Found**: Install dependencies with `pip install -r requirements.txt`
- **Rate Limiting**: Scripts include automatic retry logic with exponential backoff

### Debug Mode
```bash
# Enable debug logging
export DEBUG=true
python scripts/utils/api-client.py --debug
```

## 🔄 Automation Workflows

### CI/CD Integration
```yaml
# Example GitHub Actions workflow
name: Test Skills
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install dependencies
        run: pip install -r scripts/requirements.txt
      - name: Run tests
        run: python scripts/dev/test-runner.py --ci
```

### Scheduled Tasks
Scripts can be scheduled using cron or task schedulers:
```bash
# Daily cleanup (crontab entry)
0 2 * * * /path/to/claude-skills/scripts/maintenance/cleanup.py --quiet
```

## 📚 Development Guidelines

### Creating New Scripts
1. **Purpose**: Clearly define what the script accomplishes
2. **Dependencies**: Minimize external dependencies
3. **Configuration**: Use configuration files for customizable options
4. **Error Handling**: Implement robust error handling and logging
5. **Documentation**: Include comprehensive docstrings and usage examples
6. **Testing**: Write tests for critical functionality

### Best Practices
- Use argparse for command-line interfaces
- Implement proper logging throughout scripts
- Follow PEP 8 style guidelines for Python
- Include progress indicators for long-running operations
- Provide helpful error messages and suggestions

## 📖 Related Resources

- [Skills Directory](../skills/) - Core skill implementations
- [Templates Directory](../templates/) - Prompt templates used by scripts
- [Examples Directory](../examples/) - Usage examples that demonstrate script integration
- [API Documentation](https://docs.anthropic.com/en/api) - Claude API reference