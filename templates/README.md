# Templates Directory

This directory contains reusable prompt templates that provide standardized structures for common Claude interactions. Templates serve as starting points for consistent, high-quality prompts across various use cases.

## 📝 Template Categories

### Prompt Templates
- **Analysis Templates**: Structured approaches for analyzing content, data, or situations
- **Generation Templates**: Frameworks for creating content, code, or documents
- **Transformation Templates**: Patterns for converting or modifying existing content
- **Review Templates**: Standardized formats for reviewing and evaluating work

### Workflow Templates
- **Multi-step Processes**: Templates for complex, sequential tasks
- **Decision Trees**: Structured decision-making frameworks
- **Quality Assurance**: Templates for testing and validation workflows
- **Documentation Standards**: Consistent formatting for documentation

## 🎯 Template Structure

Each template includes:

```
template-name/
├── README.md          # Template documentation
├── prompt.md          # Main prompt template
├── variables.json     # Customizable parameters
├── examples/          # Usage examples
└── variations/        # Alternative versions
```

## 🔧 Template Components

### Prompt Template
```markdown
# Template Name

## Purpose
Brief description of what this template accomplishes

## Variables
- {{variable_name}}: Description of what to replace
- {{another_variable}}: Another customizable element

## Prompt
Your main prompt text with {{variables}} marked clearly

## Expected Output
Description of what Claude should produce
```

### Variables Configuration
```json
{
  "variables": {
    "variable_name": {
      "type": "string",
      "description": "What this variable represents",
      "default": "default value",
      "required": true
    }
  }
}
```

## 💡 Usage Examples

### Basic Template Usage
```python
# Load template
with open('templates/analysis/text-analysis.md', 'r') as f:
    template = f.read()

# Replace variables
prompt = template.replace('{{text_to_analyze}}', your_text)
prompt = prompt.replace('{{analysis_type}}', 'sentiment')

# Use with Claude
response = client.messages.create(
    model="claude-3-sonnet-20240229",
    messages=[{"role": "user", "content": prompt}]
)
```

### Advanced Template Processing
```python
import json

# Load template and variables
with open('templates/generation/report-generator.md', 'r') as f:
    template = f.read()
    
with open('templates/generation/variables.json', 'r') as f:
    variables = json.load(f)

# Process template with custom values
```

## 📋 Available Templates

### Analysis Templates
- **Content Analysis**: Analyze text for themes, sentiment, and structure
- **Data Analysis**: Examine datasets for patterns and insights
- **Competitive Analysis**: Compare products, services, or strategies
- **Risk Assessment**: Evaluate potential risks and mitigation strategies

### Generation Templates
- **Content Creation**: Generate articles, blogs, and marketing copy
- **Code Generation**: Create functions, classes, and complete programs
- **Documentation**: Generate technical and user documentation
- **Report Writing**: Create professional reports and summaries

### Transformation Templates
- **Format Conversion**: Convert between different file formats
- **Style Adaptation**: Adapt content for different audiences or purposes
- **Language Translation**: Translate content while preserving context
- **Content Optimization**: Improve existing content for specific goals

## 🎨 Customization Options

### Variable Types
- **Text**: String replacements for content
- **Numbers**: Numerical parameters for calculations
- **Lists**: Arrays of items for iteration
- **Objects**: Complex data structures
- **Booleans**: True/false flags for conditional logic

### Template Variations
- **Basic**: Simple, straightforward version
- **Advanced**: Comprehensive version with additional features
- **Specialized**: Domain-specific adaptations
- **Interactive**: Templates with follow-up questions

## 🔄 Template Development

### Creating New Templates
1. Identify common prompt patterns
2. Extract reusable components
3. Define customizable variables
4. Create comprehensive documentation
5. Test with various inputs
6. Provide usage examples

### Template Guidelines
- **Clarity**: Use clear, specific instructions
- **Flexibility**: Allow for customization through variables
- **Consistency**: Follow established formatting standards
- **Documentation**: Provide thorough usage guides
- **Testing**: Validate with multiple scenarios

## 🛠️ Integration

Templates work with:
- Automation scripts
- Web applications
- IDE extensions
- Workflow tools
- CI/CD pipelines

## 📊 Quality Metrics

- **Reusability**: How often templates are used across projects
- **Effectiveness**: Quality of outputs generated
- **Flexibility**: Adaptability to different use cases
- **Clarity**: Ease of understanding and modification
- **Maintenance**: Frequency of updates needed

## 📚 Related Resources

- [Skills Directory](../skills/) - Individual skill implementations
- [Examples Directory](../examples/) - Practical usage demonstrations
- [Scripts Directory](../scripts/) - Automation tools for template processing