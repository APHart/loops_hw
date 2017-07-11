# List we'll use for all of the books in library

books = ["Dune", "Pride and Prejudice"]


# Print welcome title

print "Brighticorn's Books"
print "-------------------"

use_library = True

while use_library:

    print "You can: add / view / check / exit"

    command = raw_input("action > ")
    command = command.lower()

    print "Action:", command

    if command == "exit":
        print "Goodbye!"

        use_library = False

    elif command == "add":
        print "Add Book"

        book = raw_input("Title > ")
        books.append(book)

        print "Added", book

    elif command == "view":
        print "View Books"

        for book in books:
            print book

        print "End of listing"

    elif command == "check":
        print "Check for a Book"

        to_check = raw_input("Title > ")

        if to_check in books:
            print "Found:", to_check

        else:
            print "Not found"

    else:
        print "Sorry, that's not an option"
