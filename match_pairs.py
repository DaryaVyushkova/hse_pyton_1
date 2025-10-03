def match_pairs(boys: list[str], girls: list[str]) -> None:
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)

    if len(boys_sorted) != len(girls_sorted):
        print('Внимание, кто-то может остаться без пары.')
        return

    print('Идеальные пары:')
    for b, g in zip(boys_sorted, girls_sorted):
        print(f'{b} и {g}')

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
match_pairs(boys, girls)

boys2 = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls2 = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
match_pairs(boys2, girls2)
