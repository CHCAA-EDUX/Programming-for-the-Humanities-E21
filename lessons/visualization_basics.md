# Basic viusalization in Python #

This is an introduction to Object-Oriented Programming and classes in Python

Learning goals:


* How to create a visualization in Python.
* Use the `pyplot` module from the `matplotlib library` to create simple visualizations.
* How to add and modify axis attributes figure objects
* How to organize several plots into one figure

## Set up data and environment ##

First we set up the data and environment for working with `matplotlib`.

```sh
$ mkdir infovis
$ cd infovis
$ git clone https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21.git
$ mv Programming-for-the-Humanities-E21/dat/series/ data
$ rm -rf Programming-for-the-Humanities-E21
$ mkdir figures
```

If you want to use a virtual environment (not necessary in [UCloud](https://cloud.sdu.dk/)).

```sh
$ sudo pip3 install virtualenv
$ virtualenv -p /usr/bin/python3 ivis
$ source ivis/bin/activate
$ pip install matplotlib
$ pip install numpy
```

Check that we have the data `dat` and environment `ivis` subdirectories

```sh
$ ls -l
data  figures ivis
```

## Ten Rules of Visualization ##

1. Know you Audience
2. Identify your Message
3. Adapt the Figure to the Support Medium
4. Captions are not optional
5. Do not Trust the Defaults
6. Use Color Effectively
7. Do not Mislead the Reader
8. Avoid 'chartjunk'
9. Message Trumps Beauty
10. Get the Right Tool

### Data-Ink Ratio ###

<img src="https://render.githubusercontent.com/render/math?math=\text{Data-Ink Ratio}=\Large\frac{\text{Data-Ink}}{\text{Total ink used to print the graphic}}">


The Data-Ink ratio is a concept introduced by [_Edward Tufte_](https://www.edwardtufte.com/tufte/), the expert whose work has contributed significantly to designing effective data presentations. In his 1983 book, 'The Visual Display of Quantitative Data', he stated the goal:

"Above all else show the data"
(Tufte, 1983)

"A large share of ink on a graphic should present data-information, the ink changing as the data change. Data-ink is the non-erasable core of a graphic, the non-redundant ink arranged in response to variation in the numbers represented."
(Tufte, 1983)

Tufte refers to data-ink as the non-erasable ink used for the presentation of data. If data-ink would be removed from the image, the graphic would lose the content. Non-Data-Ink is accordingly the ink that does not transport the information but it is used for scales, labels and edges. The data-ink ratio is the proportion of Ink that is used to present actual data compared to the total amount of ink (or pixels) used in the entire display. (Ratio of Data-Ink to non-Data-Ink).

### Read series data ###

Start by maling a `series_visualization.py` file and read one of the tabular files from `data/` as a `numpy` array.

```py
import numpy

data = np.loadtxt(fname='data/series-01.csv', delimiter=',')
```

And run the script in interactive mode, inspect the data and check the dimensions

```sh
$ python -i series_visualization.py
>>> data
array([[0., 0., 1., ..., 3., 0., 0.],
       [0., 1., 2., ..., 1., 0., 1.],
       [0., 1., 1., ..., 2., 1., 1.],
       ...,
       [0., 1., 1., ..., 1., 1., 1.],
       [0., 0., 0., ..., 0., 2., 0.],
       [0., 0., 1., ..., 1., 1., 0.]])
>>> data.shape
(60, 40)
```

We see that the array has 60 objects measured on 40 variables. In this case each object is a person and each variable is a persons' inflammation rate (over 40 days). In other words, we have a inflammation rate time series and each variable (columns) represent the rate of inflammation at a given day. 

#### Visual inspection of a numpy array ####

Add simple array visualization to `series_visualization.py` and save the files to your `figures` subdirectory.

```py
import matplotlib.pyplot as plt
image = plt.imshow(data)
plt.savefig('figures/my_array.png')
plt.close()
```

And execute. Now you can open you `my_array.png` file and you can inpect the matplotlib object

```sh
$ python -i series_visualization.py 
>>> image
<matplotlib.image.AxesImage object at 0x7f836fc249b0>
>>> dir(image)
```

Blue pixels in this figure (heat map) represent low values, while yellow pixels represent high values. As you can see, each object (rows) rises and falls over a 40 time unit period (columns).

Let us plot the average intensity pr. time unit.

```py
ave_value = np.mean(data, axis = 0)
ave_plot = plt.plot(ave_value)
plt.savefig('figures/ave_value.png')
plt.close()
```

Here we use the `plot()` function, which plots y versus x as lines and/or markers. Since we only supply one array, `plot()` assumes it is the _y_ or second axis variable.

Q: What happens if you do not close the figure?

For more information about `plot()` see [Pyplot tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html).


We can continue to calculate and blot descriptive statistics of our data set. Let us start with the maximum daily values - this time a little less verbose.

```py
max_plot = plt.plot(np.max(data, axis = 0))
plt.savefig('figures/max_value.png')
plt.close()
```

And then the minimum daily values.

```py
max_plot = plt.plot(np.min(data, axis = 0))
plt.savefig('figures/min_value.png')
plt.close()
```

### Grouping plots ###

`Matplotlib` allows you to group multiple plots in a single figure using subplots. Using `figure()` you can create a canvas to 'draw' your individual plot on. The parameter `figsize` sets the size of the canvas in following the pattern `(width, height)` in inches. We are going to add three plots side by side, so approximately a 3/1 ratio (with an extra inch for y-axis labels). The method `add_subplot()` allow us to add plots to the canvas, it takes three parameters `(nrows, ncols, index)`. We write each subplot to axes variables (`axes1`, `axes2`, `axes3`). With each subplot created, we can modify plot and axis properties using the axes variables. 

Create a new file `group_plots.py` and add.

```py
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='data/series-01.csv', delimiter=',')

fig = plt.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0))

fig.tight_layout()

plt.savefig('figures/group_plots.png')
plt.close()
```

### Visualize multiple files ###

We can use the `glob` library to find all files in a directory that match a pattern.

```sh
$ python
>>> import glob
>>> print(glob.glob('data/series*.csv'))
['data/series-02.csv', 'data/series-07.csv', 'data/series-11.csv', 'data/series-10.csv', 'data/series-12.csv', 'data/series-03.csv', 'data/series-04.csv', 'data/series-09.csv', 'data/series-06.csv', 'data/series-08.csv', 'data/series-05.csv', 'data/series-01.csv']
```

Let us combine a `glob` statement with a `for` loop to visualize multiple files. 

Create a new file `multiple_plots.py`

```py
import glob
import numpy as np
import matplotlib.pyplot as plt

filenames = sorted(glob.glob('data/series*.csv'))
filenames = filenames[0:3]# we only run over three files for efficiency
for filename in filenames:
    print(f'Building plot of {filename}') 

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    
    figurename = f"figures/{filename.split('/')[-1].split('.')[0]}.png"
    print(f'Storing plot as {figurename}\n---')

    plt.savefig(figurename)
    plt.close()
```


---

This material has been adapted from [Software Carpentries](https://software-carpentry.org/) [Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/) lesson by [CHCAA](https://chcaa.io/#/). 