def solve(phrases: list):
    result = [] # список палиндромов    
    for phrase in phrases: # пройдите циклом по всем фразам
        clean_phrase = phrase.replace(' ', '') # сохраните фразу без пробелов
        if clean_phrase == clean_phrase[::-1]: # сравните фразу с ней же, развернутой наоборот (через [::-1])
           result.append(phrase)
    return result