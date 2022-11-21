**DISCLAIMER**

This project is created for two reasons:

1. Educational purpose (the most important purpose)
2. It's a fun way to show the irony of creating an automation for a boring task like creating a book version of the ["Automate Boring Stuff With Python" website](https://automatetheboringstuff.com/).

Thanks for the author Al Sweigart, we could have this wonderful learning metirials for python beginners.

---

## How it works

This Python code requests ["Automate Boring Stuff With Python" website](https://automatetheboringstuff.com/) and then get the list of Table of Contents from homepage. Then it loops through the TOC links and gets the content of the related chapter's HTML. After getting the HTML content, it converts the HTML into PDF. After finishing the scrapping of whole chapters, it merges all chapter-based PDFs as a single PDF book.

---

You can create your own ABSWP e-book by using this project.

## Usage

`pip install -r requirements.txt`

`python3 main.py`
