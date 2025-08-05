#fix our previous code


print("enter a shopping list of items seperated by commas and no spaces. ex.(eggs,milk,orange)")
shopping_list = input().lower().split(",")

print("enter the current contents of your fridge seperated by commas and no spaces. ex.(eggs,milk,orange)")
fridge_content = input().lower().split(",")
if "" in fridge_content:
    fridge_content.remove("")


def list_change(change_list,frig):
    print(f"your current list is {change_list}")
    print("would you like to 'remove' an item from the list or 'add' one to it?")
    change_type = input().lower()
    if change_type == "remove":
        def list_remove(list_rem,fri):
            print(f"this is your current list {list_rem}")
            print("what would you like to remove from the list?")
            change_rem = input().lower()
            m = -1
            for stuff in list_rem:
                m += 1
                if stuff == change_rem:
                    list_rem.remove(stuff)
                    print(f"this is your list {list_rem}")
                    main_fridge_input(list_rem,fri)
            
                elif m == len(list_rem) -1 and stuff != change_rem:
                    print("no such item exists please check your spelling and try again")
                    print(f"this is your list {list_rem}")
                    list_remove(list_rem,fri)

        list_remove(change_list,frig)
    elif change_type == "add":
        print(f"this is your current list {change_list}")
        print("what would you like to add?")
        change_add = input().lower()
        change_list.append(change_add)
        change_list = list(set(change_list))
        print(f"this is your new list {change_list}")
        main_fridge_input(change_list,frig)



def fridge_take(listig,icebox):
    print("what item would you like to remove from the fridge?")
    req_item_take = input().lower()
    i = -1
    for item in icebox:
        i += 1
        if req_item_take == item:
            icebox.remove(item)
            print(" item removed ")
            main_fridge_input(listig,icebox)
        elif i == len(icebox) - 1 and item != req_item_take:
            print("no such item exists please check your spelling and try again")
            print(icebox)
            fridge_take(listig,icebox)

# alternative verrsion of the set list switcheroo on lines 30 - 33:
# restocked_fridge = list(set(restocked_fridge + restock_list))

def fridge_restock(restock_list,restocked_fridge):
    restocked_fridge = restocked_fridge + restock_list
    restocked_fridge = set(restocked_fridge)
    restocked_fridge = list(restocked_fridge)
    print("fridge has been restocked")
    main_fridge_input(restock_list,restocked_fridge)

def main_fridge_input(shop_list,fridge):
    print(fridge)
    print("would you like to 'change' list, 'restock' the fridge, or 'take' something from it?")
    mf_input = input().lower()
    if mf_input == "take":
        fridge_take(shop_list,fridge) 

    elif mf_input == "restock":
        fridge_restock(shop_list,fridge)

    elif mf_input == "change":
        list_change(shop_list,fridge)


    else :
        print("something seems to have gone wrong check your spelling and try again")
        main_fridge_input(shop_list,fridge)
    


#    y = -1
#    for things in restocked_fridge:
#        y += 1
#        if things == "":
#            restocked_fridge.remove("")
#            break
#        elif y == len(restocked_fridge) - 1 and things != "":
#            break
#
#






main_fridge_input(shopping_list,fridge_content)
