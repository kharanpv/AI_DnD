import PyPDF2
from pprint import pprint
def get_fillable_forms(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        print(pdf_reader.get_form_text_fields())

        # Get the trailer (document metadata)
        trailer = pdf_reader.trailer

        # Check if the trailer contains an /AcroForm field
        if "/AcroForm" in trailer:
            # Get the /AcroForm dictionary
            acroform = trailer['/AcroForm']

            # Check if the /AcroForm dictionary contains a /Fields array
            if "/Fields" in acroform:
                # Get the array of form fields
                form_fields = acroform['/Fields']

                # Print the names of all form fields
                for field_ref in form_fields:
                    field_object = pdf_reader.getObject(field_ref)
                    field_name = field_object.get("/T", "Unnamed Field")
                    print(f"Form Field Name: {field_name}")

if __name__ == "__main__":
    # Replace 'your_pdf_file.pdf' with the path to your PDF file
    pdf_path = './DnD_5E_CharacterSheet_FormFillable.pdf'
    get_fillable_forms(pdf_path)
