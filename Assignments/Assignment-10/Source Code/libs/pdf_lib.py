import PyPDF2
import json

def pdf_to_json(pdf_path, json_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Get the number of pages in the PDF
        num_pages = pdf_reader.numPages

        # Initialize an empty dictionary to store form data
        form_data = {}

        # Iterate through each page
        for page_num in range(num_pages):
            # Get the page
            page = pdf_reader.getPage(page_num)

            # Extract form fields data
            form_fields = page.getFields()

            # Iterate through form fields
            for field_name, field in form_fields.items():
                # Get the field value
                field_value = field.get('/V')

                # Add field data to the dictionary
                form_data[field_name] = field_value

        # Dump the output
        return json.dump(form_data, indent=2)

# Below is all testing stuff
if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your form-fillable PDF
    input_pdf_path = 'input.pdf'

    # Replace 'output.json' with the desired output JSON file path
    output_json_path = 'output.json'

    pdf_to_json(input_pdf_path, output_json_path)

    print(f'Conversion complete. Form data saved to {output_json_path}')

