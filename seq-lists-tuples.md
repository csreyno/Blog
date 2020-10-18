[Seqeunces Lesson Link](https://learn.digitalcrafts.com/immersive/lessons/solving-problems-using-code/sequences/#lesson)
## Sequences, Lists, and Tuples (Python)

 - a **sequence** is a data type that can store mutliple individual values.
    - *lists*, *tuples*, and *ranges* area all examples of a **sequence**

### <u>List</u>
mutable sequence - versatile, general purpose

    programming_languages = ["bash", "python", "html", "CSS", "Javascript"]
### <u>Tuple</u>
immutable sequence - best for representing a fixed value

    gps_coords = (33.84, -84.37)
### <u>Range</u>
list of numeric values

    nums_from_zero_to_ten = range(10)
    nums_from_one_to_ten = range(1,10)

#### List Literal 
- one or more values separated by commas
- enclosed in brackets [ ]

<u>Access items in a sequence:</u>

- "0" in an index *always* represents the first value in a list

so index value "0" from above list of programming languages: would be "bash" and value "1" would be "python", etc  

    print("The first language is:", programming_languages[0])  

If a value is referenced outside the index an "IndexError" will be thrown:  
like any error, can be addressed with a "try/except"  

    try:
        print("item does not exist")
    except IndexError:
        print("You almsot got an IndexError!")

### <u>Accesing All Items  </u>

    print("These are programming languages:")
    print(programming_languages)
### <u>Slicing</u>  - uses ":"
The first value in a slice <u>IS</u> included but the second is <u>NOT</u> so:

    fruit = ["apple", "orange", "banana", grape"]
    print(fruit[1:4]) #This will print "orange" and "banana" but not "grape"
    print(fruit[1:]) #Leaving the second value empty will print "banana" and all values listed after including the final value
If you omit the starting value in a slice it will begin at "0"  

### <u>Length of a Sequence</u> ###
use the "len( )" function on the sequence so it returns an integer  
### <u>Loops</u> ###
    index = 0 #Begin with index "O"
    while index < len(fruit):
        fruit1 = fruit[index]
        print("%d: %s" % (index +1, todo))
        index += 1

- intial state - index variable at 0  
- conditional: only run the code if index < len(fruit)  
- a code block that moves us closer to an end condition: index += 1  

when run we see:

    1: apple
    2: orange
    3: banana
    4: grape

#### <u>For Loop</u> #####
If you dont want the specific index of an item and just want the items themselves, use a "for loop":

    fruit = ["apple", "orange", "banana", grape"]

    for fruit1 in fruit:
        print(fruit1)
    
results in:

    apple
    orange
    banana
    grape

"For loops" are shorthand fot iterating **AND** accessing items.  

To number the list:

    fruit = ["apple", "orange", "banana", grape"]

    count = 1
    for fruit1 in fruit:
        print("%d: %s" % (count, todo))
        count += 1

### <u>Adding Items to a List</u>
1. ".append( )" method

    fruit = ["apple", "orange", "banana", grape"]

    fruit.append("kiwi")
    fruit.append("pineapple")

2. concatenation "+" operator

    fruit = ["apple", "orange", "banana", grape"]

    fruit = fruit + ["kiwi", "pineapple"]

3. can alse use the .extend( ) modifier in the same way as .append( )  

#### <u>Replacing Items in a List</u>

    fruit = ["apple", "orange", "banana", grape"]

    fruit[1] = "pear"
    print(fruit)
    
    ["apple", "pear", "banana", grape"]
In the above "orange" has been replaced with "pear".  

\- To replace multiple items a "slice" can be used:  

    fruit = ["apple", "orange", "banana", grape"]

    fruit[0:4] = ["kiwi", "pear"]
    print(fruit)
\- Just like in a normal slice the above will replace items from index 0 up to, but not including, index 4. The slice will replace the segment covered with a new list.  

### <u>Delete Items from a List</u>
Use the "del" keyword:  

    fruit = ["apple", "orange", "banana", grape"]
    del fruit[0] #removes first item

    del fruit[1:3] #removes items at index 1 up to but not including index 3

### <u>Using</u> range( ) <u>Function to generate numbers</u>

    size = 3
    for y in arange(size):
        for x in range(size):
            print(y, x)

outputs:

     0 0
     0 1
     0 2
     1 0
     1 1 
     1 2
     2 0
     2 1
     2 2

### <u>Using Strings as Sequences</u>

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    print("First letter is", alphabet[0])

    print("First three letters are", [:2])

    print("There are %d letters in the aplhabet" % len(alphabet))

\- loops through characters of a string:

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for letter in alphabet:
        print(letter) #prints each letter on its own line

\- convert a string to a list:

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    alphalist = list(alphabet)
    alphalist[0] = "4"

    print(alphalist) #replaces letter "a" with "4"

\- convert a list to a string:

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    alphalist = list(alphabet)
    alphalist[0] = "4"

    print(alphalist)

    alphabet = "".join(alphalist)
    print(alphabet)  
Because we used an empty string ("") to join the items the resulting string has no spaces. could put in "\n" for a line break after each letter too

### <u>Tuples and Sequence Operations</u>
\- Just like with strings you can index, slic, and get he length of a tuple BUT you cannot modify a tuple.

    coords = (33.55, -85.36)

    latitude = coords[0]
    longitude = coords[1]

    print("The latitude is %f and the longitude is %f" % (latitude, longitude))

\- Tuples are immutable so assigning to an Index of a tuple results in an error  
\-But you cn concatenate to produce a new tuple:

    fruit = ("apple", "banana", "orange", "pear")

    fruit = fruit[:-1] #all but the last

    fruit = fruit + ("kiwi", ) #to create a tuple with a single item you must wrap it in "" and add a trailing comma as shown