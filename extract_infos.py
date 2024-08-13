from pypdf import PdfReader

reader = PdfReader("meta2-pdf.pdf")

meta = reader.metadata

print(meta.title)
print(meta.author)
print(meta.subject)
print(meta.creator)
print(meta.producer)
print(meta.creation_date)
print(meta.modification_date)