def open_file(file):
    """
    Opens file, theoretically 'elevation_small_file' should display formatted version--not sure why that didn't display. 'elevation' displayed list of strings of numbers with '/n'.
    """
    elevation_small_file = open(file, 'r')
    elevation = elevation_small_file.readlines()
    return elevation


def clean_elevation(elevation):
    breakpoint()
    """
    'Clean_elevation' strips '\n' and separates each number into it's own string. 'Elevation_list' turns the strings into integers.
    """
    cleaned_elevation_list = [letter.replace(
        '\n', '').strip().split() for letter in open_file(file)]
    elevation_list = [[int(cleaned_elevation_list) for cleaned_elevation_list in row] for row in cleaned_elevation_list]
    return elevation_list


def find_max(elevation_list):
    """
    Gets the maximum elevation in each row, and then returns the maximum for all rows. *I'm not sure why this one stopped working when I moved it into a function. Before it printed all the numbers, and then printed 5561 at the end, so I will use that as the max going forward.
    """
    max_elevation= max(elevation_list)
    print(max_elevation)
    max_max_elevation= max(max_elevation)
    # print(max_max_elevation)
    return max_max_elevation


def find_min(elevation_list):
    """
    Same as max, but for minimum elevation. *This one also stopped working when I moved it into a function. Previously I got 3143 as the min.
    """
    min_elevation= min(elevation_list)
    min_min_elevation= min(min_elevation)
    # print(min_min_elevation)
    # return min_min_elevation


# def scale_elevation():
#     """
#     Scale the minimum to maximum range to a 0-255 range, in order to convert elevations to a greyscale image, using the formula: (elevation/max elevation) * 255
#     """
#     for number in elevation_list:
#         new_int = int((number/5561) * 255)
#         print(new_int)
#         return new_int





elevation_list= list
file= 'elevation_small.txt'
elevation= open_file(file)
clean_elevation= clean_elevation(elevation)

max= find_max(elevation_list)
# min = min(elevation_list)
# scale_elevation()
