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
to_jaden_case("most trees are blue")
# 'Most Trees Are Blue'

to_jaden_case("When I die. then you will realize")
# 'When I Die. Then You Will Realize'

to_jaden_case("Dying is mainstream")
# 'Dying Is Mainstream'