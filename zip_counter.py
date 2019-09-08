def zip_counter():
    letters = ['a','b','c','d','e','f','g','h','i','j',]
    numbers = []
    x = 0
    for a in letters:
        x = x + 1
        numbers.append(x)    
    alphanumero = zip(numbers, letters)
    count = len(letters)
    while count != 0:
        for i in alphanumero:
            print(i, sep= '\n')
            count = count - 1
    print("That's all folks!")
    
```
>>> zip_counter()
(1, 'a')
(2, 'b')
(3, 'c')
(4, 'd')
(5, 'e')
(6, 'f')
(7, 'g')
(8, 'h')
(9, 'i')
(10, 'j')
That's all folks!
>>> 
```
