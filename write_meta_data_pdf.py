from datetime import datetime
from pypdf import PdfReader, PdfWriter

reader = PdfReader("example.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)
    
    
if reader.metadata is not None:
    writer.add_metadata(reader.metadata)
    
    
utc_time = "-01'00"
time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")

writer.add_metadata(
    {
        "/Author": "Martin",
        "/Producer": "Libre Writer",
        "/Title": "Title",
        "/Subject": "Subject",
        "/Keywords": "Keywords",
        "/CreationDate": time,
        "/ModDate": time,
        "/Creator": "Creator",
        "/CustomField": "CustomField",
    }
)

with open("meta-pdf.pdf", "wb") as f:
    writer.write(f)