from pypdf import PdfWriter

writer = PdfWriter(clone_from="example.pdf")

writer.add_metadata(
    {
        "/Author": "Jan",
        "/Producer": "Libre Writer",
        "/Title": "Title",
    
    }
)

with open("meta2-pdf.pdf", "wb") as f:
    writer.write(f)