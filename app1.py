"""
    Napisz program, w którym z dwóch napisów wybierzesz ten, w którym więcej
    razy wystąpił wybrany przez Ciebie znak. Dla tak wyznaczonego napisu
    zastąp wszystkie wystąpienia tego znaku znakiem '*' jeżeli znak
    wystąpił w napisie na pozycji parzystej lub znakiem '#' jeżeli znak wystąpił
    w napisie na pozycji nieparzystej.
"""
def choose_text_containg_greater_number_of(c: str, text1: str, text2: str) -> str:
    if len(c) != 1:
        raise ValueError('Character length is not correct')

    if len(text1) == 0:
        raise ValueError('First text is empty')

    if len(text2) == 0:
        raise ValueError('Second text is empty')

    return text1 if text1.count(c) > text2.count(c) else text2

def replace_char_with(even_replacer: str, odd_replacer: str, replaced: str, text: str) -> str:
    return ''.join([(even_replacer, odd_replacer)[i % 2] if c == replaced else c for i, c in enumerate(text)])

def main() -> None:
    t1 = 'kmprograms'
    t2 = 'python'
    t3 = choose_text_containg_greater_number_of('r', t1, t2)
    print(t3)
    t4 = replace_char_with('*', '#', 'r', t3)
    print(t4)


if __name__ == '__main__':
    main()

