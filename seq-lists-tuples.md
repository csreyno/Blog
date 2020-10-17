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

