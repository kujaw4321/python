from pypdf import PdfReader

reader = PdfReader("sample-1.pdf")
page = reader.pages[0]
print(page.extract_text())

print(page.extract_text(0))

print(page.extract_text(0, 90))

print(page.extract_text(extraction_mode="layout"))

print(page.extract_text(extraction_mode="layout", layout_mode_space_vertically=False))

print(page.extract_text(extraction_mode="layout", layout_mode_strip_rotated=False))
 