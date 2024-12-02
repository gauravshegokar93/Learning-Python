import os
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image


def validate_pdf(file_path):
    # Check if file exists
    if not os.path.isfile(file_path):
        return "Error: File does not exist."

    # Check if the file is a PDF by verifying its extension
    if not file_path.lower().endswith('.pdf'):
        return "Error: File is not a PDF."

    # Check file integrity (file not corrupted)
    try:
        reader = PdfReader(file_path)
        num_pages = len(reader.pages)
    except Exception as e:
        return f"Error: PDF file is corrupted. {e}"

    # Validate PDF version (In newer PyPDF2, the version is available through PdfReader's metadata)
    pdf_version = reader.metadata.get("/PDFVersion", "Unknown")
    if pdf_version == "Unknown":
        return "Warning: PDF version could not be determined."
    elif float(pdf_version) < 1.4:
        return f"Warning: PDF version {pdf_version} is lower than the recommended version."

    # Check fonts and encoding
    # Check for embedded fonts and make sure no font issues are detected
    embedded_fonts = False
    for page in reader.pages:
        if '/Font' in page['/Resources']:
            embedded_fonts = True

    if not embedded_fonts:
        return "Warning: Fonts are not embedded in the document."

    # Check for digital signatures (if applicable)
    signatures = []
    if "/Sig" in reader.trailer["/Root"]:
        signatures.append("Digital signature found.")
    if not signatures:
        signatures.append("No digital signature found.")

    # Check for document structure and header/trailer
    if reader.getDocumentInfo() is None:
        return "Error: Document structure is missing or corrupted."

    # Validate metadata (author, title, etc.)
    metadata = reader.metadata
    if not metadata:
        return "Warning: No metadata found in the document."

    # Check security settings (if PDF has restrictions like print/copy)
    if reader.isEncrypted:
        return "Error: PDF is encrypted. Cannot validate further."

    # Check image and external object links (embedded images)
    try:
        images = []
        for page in reader.pages:
            if "/XObject" in page['/Resources']:
                images.append(page['/Resources']["/XObject"])
        if not images:
            return "Warning: No embedded images found in the PDF."
    except Exception as e:
        return f"Error: Could not extract embedded objects. {e}"

    # Validate accessibility (check for accessibility tags)
    # Simple check - real accessibility checks require more specific methods
    accessibility_check = "Not checked"

    # Validate the size (ensure it is not excessively large)
    file_size = os.path.getsize(file_path)
    if file_size > 50 * 1024 * 1024:  # 50MB limit
        return "Warning: PDF file is too large."

    # Check if the PDF follows PDF/A (archival format)
    # This is a basic check (for full validation, use specific PDF/A tools)
    if "/PDFA" in metadata:
        return "PDF is in PDF/A format."
    else:
        return "PDF is not in PDF/A format."

    return "PDF validation completed successfully."


# Your PDF file path
file_path = '/Users/gauravgopalshegokar/Downloads/20016580891390557356.pdf'

# Run the validation
validation_result = validate_pdf(file_path)
print(validation_result)
