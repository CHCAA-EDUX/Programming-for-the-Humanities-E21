
# CSV files and JSON data #

CSV and JSON are data formats you most likely will encounter when doing data analysis.

* CSV data (**C**omma **S**eparated **Va**lues) is widely used for tabular data. You might have seen it when working with a spreadsheet in Microsoft Excel. CSV files *only* contain text in tabular form (rows and columns).

* JSON data (**J**ava**S**cript **O**bject **N**) is widely used for web applications and for communicating with servers. JSON data is structured in a nested hierarchy structured in kay-value pairs.

This lesson will cover how to work with CSV files and JSON data in Python.

We will use the libraries: `csv`, `json` and `pandas` for reading, writing and analysing data.

Furthermore, we will make use of `urlopen` from `urllib.request` for accessing JSON data from a Web API.


In the end of the lesson there is a coding exercise/challenge. Building on a horoscope program, the exercise can be used as practice for accessing one type of data and store it in a different format.



## CSV files

A CSV file is a plain text file. CSV stands for 'comma-separated values' indicating that our data is separated by commas, structuring our data in tabular form.
Each line in the file represents a row in a table and the commas indicate the division into cells.

You might have worked with tables and spreadsheets in Microsoft Excel. You can read a CSV file into Excel but the file itself lacks some of the information you will get from Excel, e.g., value types (everything is a string in a CSV format). However, with CSV files we gain *simplicity*!


As a string can contain commas within it, CSV files also have escape characters to distinguish between these and those making a boundary between two cells.
In Python, there exists a `csv` module for reading and writing tabular data in CSV format.

### CVS Reader
To read data from a CSV file we first need to create a `reader` object.
The `reader` object will iterate over the lines in the given CSV file.

```
import csv

path = "data/zodiac_dates.csv"
with open(path) as zodiacFile:
    reader = csv.reader(zodiacFile)
    zodiacData = list(reader)
zodiacData

>>>
[['Pisces', '19-02', '20-03'],
 ['Aries', '21-03', '19-04'],
 ['Taurus', '20-4', '20-05'],
 ['Gemini', '21-5', '20-6'],
 ['Cancer', '21-06', '22-07'],
 ['Leo', '23-07', '22-08'],
 ['Virgo', '23-08', '22-09'],
 ['Libra', '23-09', '22-10'],
 ['Scorpio', '23-10', '21-11'],
 ['Sagittarius', '22-11', '21-12']]
```


By calling the `list()` function on our `reader` object we get a list of lists. A list of lists is called a *matrix* and we can access the data in the list by specifying the row and column: ```list[row][col]```.

```
zodiacData[0][0]
>>>
'Pisces'

zodiacData[7][2]
>>>
'22-10'
```

**Remember**: The computer counts from 0!

### DictReader

From what is printed above we see that the first column contains the name of the zodiac sign, the second the start date, and the third column the end date. This information can be passed to our `reader` obejct and used to access the columns. To do this we use `DictReader` and `DictWriter`.

Instead of reading and writing a CSV file as lists, as the `reader` and `writer` objects, `DictReader` and `DictWriter` use dictionaries instead. The first row of the CSV file is used as the keys of the dictionaries.

```
import csv
zodiacFile =  open('zodiac.csv')
dictReader = csv.DictReader(zodiacFile, ['Zodiac Sign', 'Start Date', 'End Date'])
for row in dictReader:
    print(row['Zodiac Sign'], row['Start Date'], row['End Date'])

>>>

Pisces 19-02 20-03
Aries 21-03 19-04
Taurus 20-4 20-05
Gemini 21-5 20-6
Cancer 21-06 22-07
Leo 23-07 22-08
Virgo 23-08 22-09
Libra 23-09 22-10
Scorpio 23-10 21-11
Sagittarius 22-11 21-12

```


### CSV Writer
A sharp astrology enthusiast will notice that our data set does not contain data on Aquarius and Capricorn. To add this we need a `writer` object to write to our CSV file.

```
with open(path + 'restOfZodiacFile2.csv', 'w', newline='') as restOfZodiacFile:
    outputWriter = csv.writer(restOfZodiacFile)
    outputWriter.writerow(['Capricorn', '22-12', '19-01'])
    outputWriter.writerow(['Aquarius', '20-01', '18-02'])

>>>

22
```

The `writerow()`method takes a list as an argument. The list will be a row in the outputted CSV file and each value in the list is placed in a cell.


However, this has added the data about Aquarius and Capricorn in a separate file. If we want to add it to the existing file we need to pass our `zodiacFile` to the `writer` object open for appending - note the `a+` in the following code example.
We use `DictWriter` to add the headers in the first row:

```
import csv

with open(path+'zodaic_dates.csv', 'a+', newline = '') as newfile:
    output_writer = csv.writer(newfile)
    output_writer.writerow(['Capricorn', '22-10', '19-01'])
    output_writer.writerow(['Aquarius', '20-01', '18-02'])

```

Our CSV file ```zodiac.csv``` now contains data on all the zodiac signs:

```
Pisces,19-02,20-03
Aries,21-03,19-04
Taurus,20-4,20-05
Gemini,21-5,20-6
Cancer,21-06,22-07
Leo,23-07,22-08
Virgo,23-08,22-09
Libra,23-09,22-10
Scorpio,23-10,21-11
Sagittarius,22-11,21-12
Capricorn,22-12,19-01
Aquarius,20-01,18-02
```

### Deletion of rows
(this is only a maybe part as it is quite cumbersome to do it with out the pandas library. But to show it might be a good transition to the pandas part)

```
def delete_row(path_to_file, path_to_new_file):
    with open(path_to_file) as wrongfile, open(path_to_new_file, 'w') as correctFile:
        writer = csv.writer(correctFile)
        reader = csv.reader(wrongfile)
        for i, row in enumerate(reader):
            if i != 12 and i != 13:
                writer.writerow(row)


path = "data/zodiac.csv"
new_path = "data/zodiac_updated.csv"
delete_row(path, new_path)
```

## pandas
Additional to the `csv` module there are multiple other Python libraries for reading and writing to data sets as well as doing data analysis.

`pandas` is a commonly used library used for working with data sets. It has powerful built-in functions for analysing, cleaning, exploring, and manipulating data.

### Series

`pandas` series is a one-dimensional array that can hold any type of data (contrary to our CSV files which only contain string values)

```
import pandas as pd

list_a = ['aries', 'leo', 'virgo', 2]
var = pd.Series(list_a)
print(var)

>>>

0       aries
1       leo
2       virgo
3       2
dtype:  object

```

### DataFrames
When creating a `Series` we can add a key/value object - like a dictionary. A `Series` object is like a column in a table. Hence, multiple `Series` can make up a multidimensional table - also called a `DataFrame`.


```
import pandas as pd

elements = {
  "fire": ['Aries', 'Leo', 'Sagittarius'],
  "earth": ['Taurus', 'Virgo', 'Capricorn'],
  "air": ['Gemini', 'Libra', 'Aquarius'],
  "water": ['Cancer', 'Scorpio', 'Pisces']
}

df = pd.DataFrame(elements)
print(df)

>>>

          fire      earth       air    water
0        Aries     Taurus    Gemini   Cancer
1          Leo      Virgo     Libra  Scorpio
2  Sagittarius  Capricorn  Aquarius   Pisces


```

With the `loc` method we can access specific rows in our DataFrame.

```
print(df.loc[1])
>>>

fire          Leo
earth         Virgo
air           Libra
water         Scorpio
Name: 1, dtype: object

```

### Load data sets
We can use ```pandas``` to read CSV files.

```
df = pd.read_csv(path+'zodiac_dates.csv')

print(df.to_string())

>>>

Pisces  19-02  20-03
0         Aries  21-03  19-04
1        Taurus   20-4  20-05
2        Gemini   21-5   20-6
3        Cancer  21-06  22-07
4           Leo  23-07  22-08
5         Virgo  23-08  22-09
6         Libra  23-09  22-10
7       Scorpio  23-10  21-11
8   Sagittarius  22-11  21-12
9     Capricorn  22-12  19-01
10     Aquarius  20-01  18-02
11    Capricorn  22-12  19-01
12     Aquarius  20-01  18-02
13    Capricorn  22-12  19-01
14     Aquarius  20-01  18-02
```

We add the headers to the `DataFrame` otherwise will `pandas` treat the first row  of our data set (`Pisces  19-02  20-03`) as the header.:

```
import pandas as pd

df = pd.read_csv('zodiac.csv', names = ['Zodiac Sign', 'Start Date', 'End Date'])
print(df.to_string())

>>>

      Zodiac Sign Start Date End Date
0        Pisces      19-02    20-03
1         Aries      21-03    19-04
2        Taurus       20-4    20-05
3        Gemini       21-5     20-6
4        Cancer      21-06    22-07
5           Leo      23-07    22-08
6         Virgo      23-08    22-09
7         Libra      23-09    22-10
8       Scorpio      23-10    21-11
9   Sagittarius      22-11    21-12
10    Capricorn      22-12    19-01
11     Aquarius      20-01    18-02
```

The `to_string()` method prints out the entire data frame. If we work on a big data set and want to get an idea of how the data set looks like, we can print the first five rows with the `head()` methods and the last five rows with the `tail()` method.

In the example below, the values in the CSV file are not separated by a comma but by a `|`. We pass this information to our `pandas read_csv` object with: `sep='|'`.

```
import pandas as pd

df = pd.read_csv('horoscopes.csv', sep='|')
df.columns = ['number', 'horoscope', 'date', 'zodiac sign']
df.head()

>>>
      number 	horoscope 	                                     date 	   zodiac sign
0 	     0 	 You’re not the sort to play safe and even if y... 	12-01-2013 	aries
1 	     1 	 There is no such thing as something for nothin... 	12-02-2013 	aries
2 	     2 	 As the new moon falls in one of the more adven... 	12-03-2013 	aries
3 	     3 	 You will hear something amazing today but can ... 	12-04-2013 	aries
4 	     4 	 A friend or colleague you have not seen for a ... 	12-05-2013 	aries
```



### pd.to_datetime()
In our data set, dates are given as a string. We can change this with `pandas`'s `todatetime()` method:

```
print("Type in original dataframe: ")
print(type(df.loc[0][2]))

df['date'] = pd.to_datetime(df['date'])
print("Type after 'to date time' update: ")
print(type(df.loc[0][2]))
df.head()
```


### Group by
We can also group our data by and count how many entries we have pr group
```
grouped_df = df.groupby("zodiac sign")["date"].count()
grouped_df
>>>

zodiac sign
aquarius       1078
aries          1076
cancer         1074
capricorn      1079
gemini         1083
leo            1085
libra          1082
pisces         1081
sagittarius    1080
scorpio        1084
taurus         1080
virgo          1079
Name: date, dtype: int64
```
### Cleaning Data
A useful feature of the `pandas` library is the way we can clean data and handle missing data.

If there are empty cells in a data set our data analysis might be wrong. With the method `dropna()` we remove all rows which contain empty cells. When working with big data sets it is usually OK to remove a few rows.
```
import pandas as pd

df = pd.read_csv('example.csv')
new_df = df.dropna()
```

The method `dropna()` returns a new `DataFrame` -- here saved in the variable `new_df` -- and does not change in the original `DataFrame`.

If we want to makes changes in the original `DataFrame` we add the argument `inplace = True` to the `dropna()` method:

```
import pandas as pd

df = pd.read_csv('example.csv')
df.dropna(inplace = True)
```

Instead of removing an entire row we can also replace empty cells with a value using the `fillna()` method.

```
import pandas as pd

df = pd.read_csv('example.csv')

# replacing empty cells in a specific column:
df['Example Column'].fillna(130, inplace = True)

# replacing empty cells for entire DataFrame
new_df = df.fillna(130, inplace = True)
```

## JSON Data

Another format used for exchanging data is JSON. It is a lightweight standard for exchanging structured data.

Data sets can be stored as JSON and are often used when sending and receiving data from servers. A JSON file plain text file, but has the format of an *object*.

JSON data is text-based - meaning that we can (learn to) read them in a normal text editor - even though they might look rather cryptic at first sight.

JSON stands for **J**ava**S**cript **O**bject **N**otation and was originally developed for JavaScript. However, JSON files are saved as plain text, so we do not need to learn/write any JavaScript in order to work with JSON data.


Many websites and APIs use JSON format for their data. It is therefore highly useful to learn to work with JSON data.


The grammar of JSON:

| Syntax       | **Datatype**     |
| :----------- | :----------: |
|  { and } | contain an object  |
| [ and ]   | contain elements of an array |
| :         | separates a key from a value in an object |
| ,         | separates the elements in an array |
| " ... "   | contain a string |
| e.g. 4    | integers |
| true, false, null | literals |


### Import JSON Data with pandas

`pandas` has a built-in `read_json` function which import JSON strings and files into a `pandas DataFrame`.


```
import pandas as pd

df = pd.read_json('horoscopes.JSON')

print(df.head())

>>>

    sign       date                      horoscope
0  aquarius 2021-08-19  You've been like a diamond in the rough in rec...
1    pisces 2021-08-19  As a Pisces, you're cosmically guided by the e...
2     aries 2021-08-19  Youve been pushing harder than ever to make he...
3    taurus 2021-08-19  The universe knows you're prone to holding bac...
4    gemini 2021-08-19  As a Gemini, your world revolves around the in...


```

Again, we can access a specific element in the `DataFrame` with the `loc` method:

```
print(df.loc[7][2])
>>>

The world has been testing your lifestyle, Virgo.
You've been working hard to deepen your relationship
with your work and body. Thursdays skies act as a progress
check, as the illuminating sun locks eyes with growth-giving
Jupiter. This optimistic pairing highlights what still needs
releasing and renewal, before you can fully embrace
a work/life balance that supports all your needs.


```

### Read JSON respons from a link

The webpage [http://horoscope-api.herokuapp.com/horoscope/today](http://horoscope-api.herokuapp.com/horoscope/today) offers daily horoscopes in JSON format. Here is a small code example which receives JSON data on the daily horoscope for libra:
```
import json
from urllib.request import urlopen

def getTodaysHoroscope(url_to_api):
    response = urlopen(url_to_api)
    data_json = json.loads(response.read())
    return data_json

url = "http://horoscope-api.herokuapp.com/horoscope/today/Libra"
receivedJOSONdata = getTodaysHoroscope(url)
df = pd.json_normalize(receivedJOSONdata)
df.loc[0][1]
>>>

    sign 	date 	horoscope
0 	leo 	2021-09-02 	Keep a watchful eye on the reality of your fin...

```

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




.
