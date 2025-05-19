def compress_string(string):
    i = 0
    palavra_reduzida = ''
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i+1] == string[i]:
            count += 1
            i += 1
        palavra_reduzida += string[i] + str(count)
        i += 1
    if len(string) > len(palavra_reduzida):
        return palavra_reduzida
    return string

print(compress_string("aabccccaaa"))
print(compress_string("abcdefg"))
