from custom_classes import MediaItem, Book, DVD

book = MediaItem("1984", "George Orwell")
movie = MediaItem("Inception", "Christopher Nolan")

print("--- Before ---")
print(book)
print(movie)

print("\n--- Checking out the book ---")
print(book.checkout())
print(book.checkout())

print("\n--- After ---")
print(book)
print(movie)

print("\n--- Book with page count ---")
print(Book("Dune", "Frank Herbert", 412))

print("\n--- DVD checkout ---")
dvd = DVD("Interstellar", "Christopher Nolan", 169)
print(dvd)
print(dvd.checkout())
print(dvd.checkout())
print(dvd)