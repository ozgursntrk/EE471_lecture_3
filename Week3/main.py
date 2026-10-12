from custom_classes import MediaItem

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