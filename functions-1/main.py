def analyze_text(text, min_length=4):
    cleaned_text = text.replace(".", "").replace(",", "").lower()

    words = cleaned_text.split()

    filtered_words = []
    for word in words:
        if len(word) >= min_length:
            filtered_words.append(word)

    if not filtered_words:
        return {"total_words": 0, "unique_words": 0, "longest_word": None}

    total_words = len(filtered_words)
    unique_words = len(
        set(filtered_words)
    )  # set() оставляет только уникальные элементы

    longest_word = max(filtered_words, key=len)

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "longest_word": longest_word,
    }


sample_text = "Python — это отличный язык программирования. Python позволяет писать код быстро и красиво, это факт."
result = analyze_text(sample_text)
print(result)
