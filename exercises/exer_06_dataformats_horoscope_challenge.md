## Horoscope Challenge



Write a program that gives you today's horoscope!

Start writing your "recipe" for what your program should do.
Add the Python commands _afterwards_.



### Steps


1. Write a program that receives today's horoscope for *your* zodiac sign.
Access the horoscope string. Count Words in the horoscope text.


2. Save it in a text file.


- Hint:
```
# save a txt-file
outputfile = open('outputfile.text', 'w')
n = outputfile.write("text you want to output")
outputfile.close()
```



3. Let the program take a user input which is one of the 12 zodiac signs. Your program should return the daily horoscope of the inputted zodiac sign and save it in a text file.

- Hint:
```
userInput = input("[Message to user]")

```

4. Write a program that receives JSON data on the daily horoscopes for all the zodiac signs and save it in a CSV file.

* Hint: Use `for` loops.


5. Is your program robust? Or does it crash if the user input something which is not a zodiac sign?
