items = []

def insert_item():
  name = input("Enter the name of the item: ")
  price = input("Enter the price of the item: ")

  item = {
    "name": name,
    "price": price
  }
  items.append(item)

def display_items():
  print("Name\tPrice")
  print("___________")
  for item in items:
    print(f"{item['name']}\t{item['price']}")

def search_items(search_name):
  for item in items:
    if item['name'] == search_name:
      print(f"Item {search_name} found!")
      return

  print("Item not found!")

def main():
  while(True):
    print("1. Insert\n2. Show\n3. Search\n4. Exit\n\n")
    choice = int(input("Enter choice: "))
    if choice == 1:
      insert_item()
    elif choice == 2:
      display_items()
    elif choice == 3:
      search_name = input("Enter the name of the item you're looking for: ")
      search_items(search_name)
    elif choice == 4:
      break

# This is a way of calling a function and make it global, so that you can call it in different files in your project
if __name__ == '__main__':
  main()