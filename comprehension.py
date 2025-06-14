def even_squares (sList):
    return [x*x for x in sList if x % 2 == 0]

def worded(sList):
    return {word: len(word) for word in sList}

def wording (sList):
    return {name: score for name, score in sList}

def stupid (sList):
    return (word for word in sList if word[0] in ["a", "e", "i", "o", "u"])