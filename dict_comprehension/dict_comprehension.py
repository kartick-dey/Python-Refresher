def dict_comprehension_func():
    friends = [
        (1, 'Hindole', 24),
        (2, 'Bijay', 25),
        (3, 'Maity', 24)
    ]

    friends_mapping = {friend[1]: friend for friend in friends}

    print(friends_mapping)


dict_comprehension_func()
