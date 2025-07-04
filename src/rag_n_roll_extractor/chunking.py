from unstructured.partition.pdf import partition_pdf
import os
from pathlib import Path

# Note: Before running this script, install Poppler from:
# https://github.com/oschwartz10612/poppler-windows
# And add its bin directory to your PATH environment variable

# Set Tesseract path explicitly (to be removed later)
os.environ['PATH'] = os.environ['PATH'] + ';H:\\Tesseract (OCR)'

# Get absolute paths
script_dir = Path(__file__).parent
project_root = script_dir.parent.parent
output_path = project_root / "local_test"
file_path = output_path / "attention.pdf"

# Debug information
print(f"Script directory: {script_dir}")
print(f"Project root: {project_root}")
print(f"PDF file path: {file_path}")
print(f"File exists: {file_path.exists()}")
print(f"File size: {file_path.stat().st_size if file_path.exists() else 'N/A'} bytes")

# Try to find Poppler in PATH
import subprocess
try:
    result = subprocess.run(['pdfinfo', '--version'], capture_output=True, text=True)
    print(f"Poppler version: {result.stdout.strip()}")
except Exception as e:
    print(f"Poppler not found in PATH: {e}")

# You may need to specify the Poppler path explicitly
# Replace this path with your actual Poppler installation path
poppler_path = None  # Set this to your Poppler bin directory if needed
# Example: poppler_path = r"C:\poppler\bin"

chunks = partition_pdf(
    filename=str(file_path),
    infer_table_structure=True,  # extract tables
    strategy="hi_res",  # high resolution, unstrucutred uses computer vision in this 
    extract_image_block_types=["Image", "Table"],  # extract images and tables
    image_output_dir="images",  # output directory for images
    extract_images_to_payload=True,  # if true, images are extracted and added to the payload
    pdf2image_poppler_path=poppler_path,  # explicitly specify Poppler path if needed
)

print("Extracted element types:", set([str(type(chunk)) for chunk in chunks]))






