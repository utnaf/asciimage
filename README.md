## ASCIImage

This is an exercise I made to lear some Python. 

## Wat

It takes an image and prints on terminal it's ASCII color art representation.

## How

You need [Pillow](https://github.com/python-pillow/Pillow) to run this script, so please make sure to have it installed and then run

```
python asciimage.py -f test.jpg
```

Where test.jpg is this one

![c&h](https://github.com/utnaf/ascii-stuff/raw/master/test.jpg)

Should return somethin like

![result in terminal](https://github.com/utnaf/ascii-stuff/raw/master/result.png)

## Other options

### Use an url as input

```
python asciimage.py -u https://bit.ly/2Iys8VP
```

### Output in grayscale

```
python asciimage.py -f test.jpg -g
```

### Save it to an HTML file

```
python asciimage.py -f test.jpg -s
```

### Various
Feel free to contribute, comment, suggest, cry, smile, or whatever you do when you see something awesome :)

Still work in progress, I have some ideas for this that I will implement when I have some time. Thanks for stopping by anyway!
