import PyPDF2

def extract_text(filepath):
    try:
        if filepath.endswith(".pdf"):
            text = ""

            with open(filepath, "rb") as file:
                reader = PyPDF2.PdfReader(file)

                for page in reader.pages:
                    page_text = page.extract_text()

                    if page_text:
                        text += page_text

            return text

        else:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()

    except Exception as e:
        print("PDF Error:", e)
        return ""