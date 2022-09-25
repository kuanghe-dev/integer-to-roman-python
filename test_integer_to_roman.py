from integer_to_roman import integer_to_roman

def test_integer_to_roman():
    intToRomanMappings = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        10: 'X',
        24: 'XXIV',
        40: 'XL',
        50: 'L',
        51: 'LI',
        73: 'LXXIII',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        537: 'DXXXVII',
        900: 'CM',
        999: 'CMXCIX',
        1000: 'M',
        2018: 'MMXVIII',
        3497: 'MMMCDXCVII',
    }

    for integer, expectedRoman in intToRomanMappings.items():
        assert integer_to_roman(integer) == expectedRoman, f'converting {integer}'