# Setup Guide

## Prerequisites

- Python 3.8 or higher
- Git
- API keys for OpenAI and Stability AI

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd storyboard-generator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys**
   ```bash
   # Copy the template
   copy .env.template .env
   
   # Edit .env and add your API keys
   ```

## API Key Setup

### OpenAI API Key
1. Visit https://platform.openai.com/api-keys
2. Create a new API key
3. Add it to your `.env` file as `OPENAI_API_KEY`

### Stability AI API Key
1. Visit https://platform.stability.ai/account/keys
2. Create a new API key
3. Add it to your `.env` file as `STABILITY_API_KEY`

## Verification

Test your setup:
```bash
python main.py --validate-config
```

## Usage Examples

### Full Pipeline
```bash
python main.py "a detective discovering a clue in a rainy city at night"
```

### Script Only
```bash
python main.py --script-only "a space explorer finding alien artifacts"
```

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure your `.env` file exists and contains valid keys
   - Check that your API keys have sufficient credits

2. **Memory Issues**
   - Video generation requires significant RAM
   - Consider using script-only mode for testing

3. **GPU Requirements**
   - Video generation works better with CUDA-enabled GPU
   - CPU fallback is available but slower

### Getting Help

- Check the console output for detailed error messages
- Ensure all dependencies are installed correctly
- Verify your Python version is 3.8+