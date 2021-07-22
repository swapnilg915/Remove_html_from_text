import pandas as pd
from bs4 import BeautifulSoup


def clean_html(raw_text):
	if isinstance(raw_text, str):
		raw_text = raw_text.replace("<br/>","\n")
		email = BeautifulSoup(raw_text, "lxml").text
		return email


# sheets = ["Engine no", "Chassis", "Reg No.", "Nominee", "Mobile", "Email id"]
sheets = ["DF_Endorsement"]
cleaned_emails_dfs = []
for sheet in sheets:
	emails_df = pd.read_excel("dataset/Bot_Test_samples.xlsx", engine='openpyxl', sheet_name=sheet)
	emails_df["Content"] = emails_df["Content"].apply(clean_html)
	cleaned_emails_dfs.append(emails_df)
	print("\n num of sheets : ", len(cleaned_emails_dfs))
	# import pdb;pdb.set_trace()

writer = pd.ExcelWriter('dataset/Bot_Test_samples_cleaned.xlsx')
for idx in range(len(cleaned_emails_dfs)):
	print("\n sheet name : ", sheets[idx])
	df = cleaned_emails_dfs[idx]
	df.to_excel(writer, index=False, sheet_name=sheets[idx])

writer.save()