# 2-3. Personal Message
# Step 1: Store a person's name in a variable
name = "Eric"

# Step 2: Print a message using that variable
# f-string lets us insert the variable directly into the text
print(f"Hello {name}, would you like to learn some Python today?")


# 2-4. Name Cases
# Step 1: Store a name in a variable
name = "eric"

# Step 2: Print the name in lowercase
print(name.lower())   # lower() makes all letters small

# Step 3: Print the name in uppercase
print(name.upper())   # upper() makes all letters BIG

# Step 4: Print the name in title case
print(name.title())   # title() capitalizes the first letter of each word

# 2-5. Famous Quote
# Step 1: Just print a quote directly
# Notice the quotation marks inside the string
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')


# 2-6. Famous Quote 2
# Step 1: Store the famous person's name in a variable
famous_person = "Albert Einstein"

# Step 2: Build the message using that variable
# f-string lets us combine text and variables easily
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'

# Step 3: Print the message
print(message)


# 2-7. Stripping Names
# Step 1: Store a name with extra whitespace (tabs and newlines)
name = "\t\n Eric \n\t"

# Step 2: Print the original name (with whitespace showing)
print("Original:", name)

# Step 3: Remove whitespace from the left side only
print("lstrip():", name.lstrip())   # lstrip() removes spaces/tabs/newlines on the LEFT

# Step 4: Remove whitespace from the right side only
print("rstrip():", name.rstrip())   # rstrip() removes spaces/tabs/newlines on the RIGHT

# Step 5: Remove whitespace from both sides
print("strip():", name.strip())     # strip() removes spaces/tabs/newlines on BOTH sides


# 2-8. File Extensions
# Step 1: Store a filename in a variable
filename = "python_notes.txt"

# Step 2: Remove the ".txt" part using removesuffix()
# This shows the filename without its extension
print(filename.removesuffix(".txt"))
