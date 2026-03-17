import pdfplumber
import pandas as pd

pdf_path = r"C:\Users\SamuelJoshuaRaj\OneDrive - CYGNUSA Technologies\Desktop\elections\merged_output.pdf"
excel_path = r"C:\Users\SamuelJoshuaRaj\OneDrive - CYGNUSA Technologies\Desktop\lalgudi pdf\output.xlsx"

all_tables = []

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            df = pd.DataFrame(table[1:], columns=table[0])
            all_tables.append(df)

final_df = pd.concat(all_tables, ignore_index=True)
final_df.to_excel(excel_path, index=False)

print("✅ PDF converted to Excel successfully!")