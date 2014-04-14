dominant-color
==============

Analyze image and determine the dominant color.  Two approaches are here, a k-means approach as presented by Charles Leifer (http://charlesleifer.com/blog/using-python-and-k-means-to-find-the-dominant-colors-in-images/), and bucketing approach.

prerequisites
-------------
* (optional, but recommended) create a virtualenv
* pip install -r requirements.txt

usage for k-means
-----------------
* python k-means.py -f <filename> -c <number-of-colors>
* result: The program will apply the k-means clustering algorithm to the colors to determine the representative colors and output the hex values for those colors.  It also opens the original image and some sample images of the representative colors.

usage for dominant
------------------
* python dominant.py -f <filename> -c <number of colors>
* result: The program converts the color palette of the image to the number of colors specified.  The number of counts in each of the color buckets is then output.  The color tuple with the highest count would be considered the dominant color.  This program also opens the image being processed, the image after the palette change, and a sample of each of the selected colors.
