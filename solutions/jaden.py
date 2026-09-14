def to_jaden_case(text):
    words = []
    k = 0
    t = False
    for i in text:
        k+=1
        if k == 1 and i.upper() != i:
            words.append(k-1)
        if i == " ":
            words.append(k)
    for i in words:
        text = text[:i] + text[i].upper() + text[i + 1 :]
    return text