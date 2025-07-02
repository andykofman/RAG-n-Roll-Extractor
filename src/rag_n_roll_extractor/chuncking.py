from unstructured.partition.pdf import partition_pdf
import os

# Note: Before running this script, install Poppler from:
# https://github.com/oschwartz10612/poppler-windows
# And add its bin directory to your PATH environment variable

# Set Tesseract path explicitly
os.environ['PATH'] = os.environ['PATH'] + ';C:\\Program Files\\Tesseract-OCR'

output_path = "local_test"
file_path = output_path + "/attention.pdf"

chunks = partition_pdf(
    filename=file_path,
    infer_table_structure=True,  # extract tables
    strategy="hi_res",  # high resolution, unstrucutred uses computer vision in this 
    extract_image_block_types=["Image", "Table"],  # extract images and tables
    image_output_dir="images",  # output directory for images
    extract_images_to_payload=True,  # if true, images are extracted and added to the payload
)

print("Extracted element types:", set([str(type(chunk)) for chunk in chunks]))






