import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF resume."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

# Test the function
if __name__ == "__main__":
    pdf_path = "../data/sample_resume.pdf"  # Update with actual path
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)  # Print extracted text for verification
