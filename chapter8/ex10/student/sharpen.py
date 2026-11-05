"""
File: sharpen.py

Sharpens the outlines in an image while keeping its original colors.
"""

from images import Image


def sharpen(image, degree, threshold):
    """Returns a new image with its edges sharpened.

    degree:    how much to darken each edge pixel (subtracted from
               each of its RGB values).
    threshold: how large the brightness difference between a pixel and
               its neighbors must be for the pixel to count as an edge.
    The original image is not modified.
    """
    def average(triple):
        (r, g, b) = triple
        return (r + g + b) / 3

    def darken(triple):
        (r, g, b) = triple
        return (max(0, r - degree),
                max(0, g - degree),
                max(0, b - degree))

    new = image.clone()
    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldAvg = average(oldPixel)
            leftAvg = average(leftPixel)
            bottomAvg = average(bottomPixel)
            if abs(oldAvg - leftAvg) > threshold or \
               abs(oldAvg - bottomAvg) > threshold:
                new.setPixel(x, y, darken(oldPixel))
            else:
                new.setPixel(x, y, oldPixel)
    return new


def main(filename="smokey.gif", degree=50, threshold=20):
    image = Image(filename)
    print("Close the window to see the sharpened image.")
    image.draw()
    newImage = sharpen(image, degree, threshold)
    newImage.draw()


if __name__ == "__main__":
    main()