import spacy

# Load at module import (cached in container)
_nlp = spacy.load("en_core_web_sm")

def split_into_sentences(text: str):
    # 1. Split by double newlines first to enforce hard boundaries (headers, paragraphs)
    # This respects the layout analysis from pdf_parser.py
    chunks = text.split("\n\n")
    
    sentences = []
    global_id = 0
    
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
            
        # 2. Process each chunk with spacy
        doc = _nlp(chunk)
        for sent in doc.sents:
            s = sent.text.strip()
            if s:
                sentences.append({"id": global_id, "text": s})
                global_id += 1
                
    return sentences
