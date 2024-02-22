def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            division = my_list1[i] / my_list_2[i]
        except ValueError:
                print("Indivisible Input")
                division = 0
        except IndexError:
            print("out of line")
            division = 0
        finally:
            (new_list)
    return(new_list)


