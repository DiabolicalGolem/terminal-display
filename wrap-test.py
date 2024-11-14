w, h = 15, 10
text = "Testing the word wrapping is a fun challenge!"


def wrap(text):
    words = text.split()
    
    wrap_array = [""]
    line = 0
    for word in words:
        if (len(wrap_array[line]) + len(word) + 1) <= w:
            wrap_array[line] += " "+word
        else:
            line += 1
            wrap_array.append(word)

    for i in range(len(wrap_array)):
        wrap_array[i] = wrap_array[i].strip()

    return wrap_array

print(wrap(text))
