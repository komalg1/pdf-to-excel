# PDF to Excel Converter

This repository contains a Python script to convert PDF files into Excel spreadsheets. The project is containerized using a development container for easy setup and usage.

## Features
- Extracts tabular data from PDF files and converts it into Excel format.
- Easy to set up and run using a development container.

## Examples

### Input PDF
A PDF file with tabular data:

| Name  | Age | City     |
|-------|-----|----------|
| John  | 25  | New York |
| Alice | 30  | London   |

### Output Excel
An Excel file with the same tabular data:

| Name  | Age | City     |
|-------|-----|----------|
| John  | 25  | New York |
| Alice | 30  | London   |

## How to Use

### Prerequisites
- Install [Docker](https://www.docker.com/).
- Install [Visual Studio Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/komalg1/pdf-to-excel.git
   cd pdf-to-excel
   ```
2. Open the repository in Visual Studio Code.
3. Reopen the folder in the development container:
   - Press `F1` and select `Remote-Containers: Reopen in Container`.
4. Run the script:
   ```bash
   python convert_pdf_to_excel.py input.pdf output.xlsx
   ```

Replace `input.pdf` with the path to your PDF file and `output.xlsx` with the desired output Excel file name.

## License
This project is licensed under the MIT License.
