"""Read text from a PDF file with graceful fallbacks.

Tries pdfplumber first (best layout-preserving extraction), then PyPDF2.
If neither library is installed, returns a helpful message so the Streamlit
app can display it instead of crashing with ModuleNotFoundError.
"""

def extract_pdf_text(pdf_file) -> str:
    # Prefer pdfplumber for best extraction quality
    try:
        import pdfplumber

        parts = []
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    parts.append(text)
        return "\n".join(parts).strip()
    except Exception:
        # Fall back to PyPDF2 if available
        try:
            from PyPDF2 import PdfReader

            reader = PdfReader(pdf_file)
            parts = []
            for page in reader.pages:
                try:
                    text = page.extract_text()
                except Exception:
                    text = None
                if text:
                    parts.append(text)
            return "\n".join(parts).strip()
        except Exception:
            # Extraction libraries not available — return empty string so the
            # Streamlit UI can show a clear warning instead of feeding an
            # instructional message into the agents.
            return ""
