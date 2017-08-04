import re

from ..grammar import Annotator

class PunctuationAnnotator(Annotator):
    def annotate(self, tokens):
        if len(tokens) == 1:
            if tokens[0]['pos'] in ["``", "\'\'"]:
                return [('$Quote', tokens[0]['word'])]
            elif tokens[0]['pos'] == "-LRB-":
                return [('$OpenParen', tokens[0]['word'])]
            elif tokens[0]['pos'] == "-RRB-":
                return [('$CloseParen', tokens[0]['word'])]
        return []

class IntegerAnnotator(Annotator):
    def annotate(self, tokens):
        if len(tokens) == 1:
            # if all(token['ner'] in ['NUMBER', 'ORDINAL'] for token in tokens):
            if all('normalizedNER' in token for token in tokens):
                ner_number = tokens[0]['normalizedNER']
                number = re.sub('[^\d\.]','', ner_number)
                value = int(float(number))
                return [('$Int', ('.int', value))]
        return []

annotators = [PunctuationAnnotator(), IntegerAnnotator()]