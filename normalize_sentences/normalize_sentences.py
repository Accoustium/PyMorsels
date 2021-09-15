import re


def normalize_sentences(paragraph: str):
    para = Paragraph(paragraph)
    return str(para)


class Paragraph:
    structure = re.compile(r'[ ]?(.+?[\.|!|\?]) ?')

    def __init__(self, paragraph: str):
        self.raw_paragraph = paragraph
        self.sentences = self.structure.findall(paragraph)

    def __repr__(self):
        return f"Paragraph({self.raw_paragraph})"

    def __str__(self):
        if not self.sentences:
            return self.raw_paragraph
        else:
            return '  '.join(self.sentences)
