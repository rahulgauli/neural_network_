
def isAnagram(s: str, t: str) -> bool:
    map_letters = []

    for str in s:
        map_letters.append(str)

    for str in t:
        if str not in map_letters:
            return False
    return True


print(isAnagram("jar","jam"))