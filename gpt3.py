import openai
import pathlib
import pdfplumber
import numpy as np




def showPaperSummary(paperContent):
    tldr_tag = "\n tl;dr:"
    # openai.organization = 'API KEY org'
    openai.api_key = "apikey"
    # engine_list = openai.Engine.list() 
    
    for page in paperContent:    
        text = page.extract_text() + tldr_tag
        response = openai.Completion.create(engine="davinci",prompt=text,temperature=0.3,
            max_tokens=140,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        print(response["choices"][0]["text"])

paperFilePath = '.\paper.pdf'
paperContent = pdfplumber.open(paperFilePath).pages
showPaperSummary(paperContent)

