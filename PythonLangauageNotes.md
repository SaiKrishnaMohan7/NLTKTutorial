# Python Language Notes

## Naming conventions

### Variables

    # lowercase separated by _

### Functions

    Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability. Use one leading underscore only for non-public methods and instance variables. To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.

    In Python, mangling is used for "private" class members which are designated as such by giving them a name with two leading underscores and no more than one trailing underscore.

    By default, parameters have a positional behavior and you need to inform them in the same order that they were defined.

    Fucntions cannot be called before they are defined. A kind of workaround is defining a main() function and doing if __name__ == main: <enter> main(). Inside of main call the fucntion you need. CS50(Prof. Dave Malan, good source).

###defauldict
    
    can be used to created dictionaries on the fly. When trying to access an element that doesn't exist in the dictionary, a KeyError is thrown, in a defaultdict, it creates that element/entry on the fly.

    defaultdict(s) can be initialized with primitive types like int or list. The key may be whatever but the value will be of the type the defaultdict is initialized.