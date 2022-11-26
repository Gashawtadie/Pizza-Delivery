def app():
    from size import size_pizza
    from lists_class import total
    from lists_class import final_sum
    from menu import sizes
    year = True
    while True:
        print("Wellcome to pizza house, Please select the sizes")
        for key, value in sizes.items():
            print(key, value)
        age = int(input('How old are you?: '))
        if age < 18:
            exit()
        size_pizza()
        con = input("Do you want continue? y/n: ")
        if con == "n":
            break
    for summ in total:
        final_sum += summ
        print(f"Your total price is NIS {final_sum}₪")
