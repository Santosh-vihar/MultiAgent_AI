# Oracle AI - Setup & Installation Guide

## ✓ Installation Status
All dependencies have been successfully installed.

## Required Dependencies (Installed)
- `groq` - Groq API client
- `streamlit` - Web framework for the UI
- `pandas` - Data processing
- `pdfplumber` - PDF text extraction
- `PyPDF2` - Alternative PDF processing

## Running the Application

### Option 1: Run with Streamlit (Recommended)
```bash
streamlit run oracle_AI.py
```
This will start the web UI at `http://localhost:8501`

### Option 2: Install all dependencies from requirements.txt
```bash
pip install -r requirements.txt
```

## Configuration

### Groq API Key (Important)
To use the AI analysis features, you need to set your Groq API key:

**Option A: Environment Variable**
```bash
$env:GROQ_API_KEY = "gsk_your_key_here"
```

**Option B: Streamlit Secrets**
Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "gsk_your_key_here"
```

## File Structure
- `oracle_AI.py` - Main Streamlit application
- `agents.py` - AI agent prompts and logic (Architect, Risk, Failure, Innovation)
- `hf_client.py` - API client (using Groq)
- `pdf_reader.py` - PDF text extraction utility
- `requirements.txt` - Python dependencies

## Features
✓ PDF upload and text extraction
✓ Architecture analysis
✓ Risk assessment
✓ Failure prediction
✓ Innovation review

## Troubleshooting

### "Module not found" errors
Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Groq API errors
- Verify your API key has the correct permissions and format (typically starting with `gsk_`).
- Check internet connection.

### PDF extraction issues
- Ensure PDF is not scanned/image-based.
- Try a different PDF file.
- The system will show a warning if extraction fails.

## Next Steps
1. Set your Groq API key in `.streamlit/secrets.toml`.
2. Run: `streamlit run oracle_AI.py`
3. Open http://localhost:8501 in your browser.
