from RandomWordGenerator import RandomWord

rw = RandomWord(max_word_size=12, constant_word_size=True,
                include_digits=False, special_chars="_")
print(f"Your random password - {rw.generate()}")
