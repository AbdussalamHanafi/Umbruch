
def get_umbruch_text(text, char_per_zeile):
    new_text = ""

    char_zeile = 0
    for c in text:
        new_text += c
        char_zeile += 1
        if char_zeile >= char_per_zeile:
            new_text += "\n"
            char_zeile = 0
            
    return new_text