print("""

██████╗░░█████╗░░█████╗░██╗░░██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
██████╦╝██║░░██║██║░░██║█████═╝░  ██║░░██╗░███████║██╔████╔██║█████╗░░
██╔══██╗██║░░██║██║░░██║██╔═██╗░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
██████╦╝╚█████╔╝╚█████╔╝██║░╚██╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
""")


list_own = []
list_wish = []

book = input("Enter The Name Of a Book You Own : ")
list_own.append(book)

book = input("Enter The Name Of Anthore Book You Own (or Prees 'Enter' For Skip) : ")
if book:
    list_own.append(book)

print(f"\nYou Library : {list_own}\n")

book = input("Enter The Name Of a Book You Wish To have In The Future : ")
list_wish.append(book)

book = input("Enter The Name Of Anthore Book You Wish To have (or Press 'Enter To Skip') : ")

if book:
    list_wish.append(book)

print(f"\nYour Wishlist : {list_wish}\n")

book = input("Enter The name Of a Book Froom Your Library You Wich to acquired (or Press 'Enter' To Skip) : ")
if book in list_wish:
    list_own.append(book)
    list_wish.remove(book)

print(f"\nUpdated Library : {list_own}")
print(f"Updated Wishlist : {list_wish}\n")

book = input("Enter The Name Of a Book From Your Library You Wish Donate (Or Press 'Enter' To Skip) : ")
if book in list_own:
    list_own.remove(book)

print(f"\nFinal Library After Donations: {list_own}")


input("\nPress 'Enter' To Exit...")
