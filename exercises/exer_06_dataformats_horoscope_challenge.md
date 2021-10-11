## Exercises for data formats
### Check your understanding

1) Let this be our dataframe:

```
print(df)

>>>

          fire      earth       air    water
0        Aries     Taurus    Gemini   Cancer
1          Leo      Virgo     Libra  Scorpio
2  Sagittarius  Capricorn  Aquarius   Pisces
```
This type does the following return:

`df.loc[0]`

`df.loc[0].values`


2) What is the difference between these lines:

* `df.drop_duplicates(subset ="horoscope",
                     keep = False, inplace = True)`
* `df.drop_duplicates(subset ="horoscope", keep = first, inplace = True)`  

* `new_df = df.drop_duplicates(subset ="horoscope", keep = last, inplace = False)`    


3) Explain the structure of this JSON data:

```
{
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"image":
		{
			"url": "images/0001.jpg",
			"width": 200,
			"height": 200
		},
	"thumbnail":
		{
			"url": "images/thumbnails/0001.jpg",
			"width": 32,
			"height": 32
		}
}
```

(Found at https://opensource.adobe.com/Spry/samples/data_region/JSONDataSetSample.html)

## Pair Programming -- Horoscope Challenge



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
