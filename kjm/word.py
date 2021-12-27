def solution(s):
    text_l = s.split(" ")
    result = ""
    for i in text_l:
        word = ""
        for j in range(len(i)):
            if j%2 == 0:
                word += i[j].upper()
            if j%2 == 1:
                word += i[j].lower()
        result += (word+ " ")
    return result

