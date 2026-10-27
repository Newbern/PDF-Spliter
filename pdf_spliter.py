from pypdf import PdfReader, PdfWriter
from tkinter import Tk, filedialog
from datetime import datetime
import os

# Hide tkinter window
root = Tk()
root.withdraw()

# Select PDF file
input_pdf = filedialog.askopenfilename(
    title="Select PDF File",
    filetypes=[("PDF Files", "*.pdf")]
)

if not input_pdf:
    print("No file selected.")
    quit()

# Output folder next to script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_root = os.path.join(script_dir, "split_output")

# Create date/time subfolder
date_folder = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_folder = os.path.join(output_root, date_folder)

os.makedirs(output_folder, exist_ok=True)

# Read PDF
reader = PdfReader(input_pdf)

count = 0

for page_num, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)

    output_path = os.path.join(
        output_folder,
        f"page_{page_num + 1}.pdf"
    )

    try:
        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"Saved: page_{page_num + 1}.pdf")
        count += 1

    except Exception as e:
        print(f"Failed page {page_num + 1} - {e}")

print(f"\nFinished! {count} pages processed.")
print(f"Saved to:\n{output_folder}")

input("\nPress Enter to exit...")
