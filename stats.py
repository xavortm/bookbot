def get_num_words(content): 
    return len(content.split())

def get_characters_count(content):
    result: dict[str, int] = {}

    for c in content:
        c = c.lower()
        if c in result:
            result[c] += 1
        else:
            result[c] = 1

    return result

def sort_on(items):
    return items['num']

def get_format_dict(dictionary: dict[str, int])->list[dict[str, int | str]]:
    formatted: list[dict[str, int | str]] = [] 
    for key, value in dictionary.items():
        formatted.append({
            "char": key,
            "num": value
        })

    formatted.sort(reverse=True, key=sort_on)
    return formatted
    
