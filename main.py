from PyPDF2 import PdfReader
import os

path = "F:/Git/python-search-pdf/pdfs/"


def search_pdfs(path, input):
    dir_list = os.listdir(path)
    list_of_found_keywords = []

    for file in dir_list:
        file_path = os.path.join(path, file)
        reader = PdfReader(file_path)
        for page in range(len(reader.pages)):
            page_text = reader.pages[page].extract_text().lower()
            if input in page_text:
                list_of_found_keywords.append([file, int(page + 1)])

    if len(list_of_found_keywords) == 0:
        print(f"{input} not found.")
    else:
        print(f"{input} found in:\n")
        for i in range(len(list_of_found_keywords)):
            print(f"{list_of_found_keywords[i][0]} page {list_of_found_keywords[i][1]}")


def main():
    user_input = input()
    search_pdfs(path, user_input)


if __name__ == "__main__":
    main()
