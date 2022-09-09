# practice problems
import sys

def num2eng(n):
    """Return string of english text description of positive integer n."""

    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','fourty','fifty','sixty','seventy',
            'eighty','ninety']
    powers = ['','ten','hundred','thousand']

    s = str(n)[-1::-1]
    eng = []
    for p in range(len(s)):
        word = tens[int(s[p])] if (p==1) else ones[int(s[p])]
        if (p > 1) and int(s[p]):
            word = word + ' ' + powers[p]
        #ad-hoc teens
        if (p == 1) and (int(s[p]) == 1):
            eng.pop()
            word = teens[int(s[p-1])]
        eng.append(word)
    eng.reverse()
    eng = [e.strip() for e in eng if e]
    eng = ' '.join(eng)
    return eng

if __name__ == "__main__":
    pass
