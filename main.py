def wedding_graph(length_of_list, list_of_couples):

    sorted_list_of_couples = sorted(list_of_couples)
    list_of_tribes = []
    for people in sorted_list_of_couples:
        if length_of_list > 1000:
            print("Too many people")
            break
        for tribe in list_of_tribes:
            if people[0] in tribe:
                tribe.add(people[1])
                break
            elif people[1] in tribe:
                tribe.add(people[0])
                break
        else:
            list_of_tribes.append(set((people[0], people[1])))

    men_in_each_tribe = [len({man for man in tribe if man % 2}) for tribe in list_of_tribes]
    women_in_each_tribe = [len({women for women in tribe if not women % 2}) for tribe in list_of_tribes]

    return sum(men_in_each_tribe) * sum(women_in_each_tribe) - sum((male * female for male, female in zip(men_in_each_tribe, women_in_each_tribe)))


