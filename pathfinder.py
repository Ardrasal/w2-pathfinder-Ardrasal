from PIL import Image


def open_file(file):
    """
    Opens file, theoretically 'elevation_small_file' should display formatted
    version--not sure why that didn't display. 'elevation', if printed, lists
    strings of numbers with '/n'.
    """
    elevation_small_file = open(file, 'r')
    elevation = elevation_small_file.readlines()
    return elevation


def clean_elevation(elevation):
    
    """
    'Clean_elevation' strips '\n' and separates each number into it's own
    string. 'Elevation_list' turns the strings into integers.
    """
    cleaned_elevation_list = [letter.replace(
        '\n', '').strip().split() for letter in open_file(file)]
    elevation_list = [[int(cleaned_elevation_list) for cleaned_elevation_list
                      in row] for row in cleaned_elevation_list]
    return elevation_list


def find_max(elevation_list):
    """
    Gets the maximum elevation in each row, and then returns the maximum for
    all rows--I suspect this isn't working how I intended, but it's close!
    """
    maximum_elevation_per_row = max(elevation_list)
    maximum_point = max(maximum_elevation_per_row)
    return maximum_point


def find_min(elevation_list):
    """
    Same as max, but for minimum elevation.
    """
    minimum_elevation_per_row = min(elevation_list)
    minimum_point = min(minimum_elevation_per_row)
    return minimum_point


def scale_elevation(number):
    """
    Scale the minimum to maximum range to a 0-255 range, in order to convert
    elevations to a greyscale image.
    """
    maximum_point = 5561
    minimum_point = 3143
    rgb_number = [[round(int((y) - minimum_point)/(maximum_point -
                   minimum_point) * 255) for y in x] for x in number]
    return rgb_number
   

def plot_picture(list):
    """
    Takes the scaled 'rgb_number'(s) and puts them in x,y format to plot
    picture in greyscale.
    """
    # for index, num in enumerate(row):
    #     print(index)
    for y, row in enumerate(rgb_number):
        for x, num in enumerate(row):
            img.putpixel((x,y), (num, num, num))
            img.save('test.png')


file = 'elevation_small.txt'
elevation = open_file(file)
elevation_list = clean_elevation(elevation)
max = find_max(elevation_list)
min = find_min(elevation_list)
scale_elevation(elevation_list)
plot_picture(rgb_number)
