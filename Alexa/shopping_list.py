import pyttsx3
grocery_list=['apple','onion','banana','milk','shrimp']
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',180)

def talk(text):
    engine.say(text)
    engine.runAndWait()



def diplay_grocery_list():

    print('Your present grocery list contains',grocery_list)
    talk('Your present grocery list contains'+str(grocery_list))

    return grocery_list

def add_item():
    talk('Which item would you like to add')
    items=str(input('Add Your items :'))
    if items in grocery_list:
        talk(items+'is already present in your list, try adding new items')


    else:

        grocery_list.append(items)
        talk(items+"was added successfully in your list")
        print(grocery_list)


    return grocery_list

def remove_item():
    talk('Enter the item which you want to remove')
    item=str(input('Item to remove :'))
    if item in grocery_list:
        grocery_list.remove(item)
        talk(item +'was removed from your list')
        print(grocery_list)
    else :
        talk('This item is not present in your list so cant be removed   Please try checking the items again')
    print(grocery_list)
    return grocery_list


def check_item():
    talk('Enter the item which you want to check')
    item=str(input('Check items :'))
    if item in grocery_list:
        print('yes the '+item+' is already present in your list')
        talk('Yes the' +item+'is already present in your list')
    else:
        talk(item+' is not present in your list...Would you like to like to add it type yes or no')
        print(item+' is not present in your list...Would you like to like to add it type yes or no')
        response= str(input('type yes or no :'))
        if response == 'yes':
            add_item()
        else:
            print('Ok this item is not added in your list')

            talk('Ok this item is not added in your list')
    print(grocery_list)
    return grocery_list



def shopping_list(action_item):
    if action_item==1:
        diplay_grocery_list()


    elif action_item ==2:
        add_item()

    elif action_item ==3:
        remove_item()

    elif action_item ==4:
        check_item()
    else:
        talk('Action item should be between 1 to 4')
        print('Action item should be between 1 to 4')