def vector1d(content):
    # Function properties
    return content
def real(content):
    # Function properties
    # shutting yard algorithm
    return content

class Tokenizer:
    
    def __init__(self,tType):

        self.tokenizer_type = tType

        self.tokenizers = {
            "vector1d":vector1d,
            "real":real
        }

    def tokenize(self,content):
        # Maybe do some controls here.
        return self.tokenizers[self.tokenizer_type](content)


vectorTokenizer = Tokenizer("vector1d")
result = vectorTokenizer.tokenize("[1,2] + [3,4]/2")

complexTokenizer = Tokenizer("real")
result = complexTokenizer.tokenize("sin(100)/2 + (5*cos(180))")