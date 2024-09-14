def main():
    filename = "a.txt"

    # Open the file in append mode
    with open(filename, "a") as f1:
        for _ in range(5):
            word = input("Enter a word: ")
            f1.write(word + " ")

    # Read the entire file
    with open(filename, "r") as f1:
        content = f1.read()

    # Count spaces and find the second space
    space_count = 0
    for char in content:
        if char == " ":
            space_count += 1
            if space_count == 2:
                insert_index = content.index(char) + 1
                break

    # Open the file in write mode and overwrite from the start
    with open(filename, "w") as f1:
        f1.write(content[:insert_index] + "apple" + content[insert_index:])

if __name__ == "__main__":
    main()
