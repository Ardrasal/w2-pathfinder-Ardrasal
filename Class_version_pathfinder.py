class ElevationMap:
    def __init__(self, elevation):
        self.elevation = elevation

    def open_file(self):
        elevation_small_file = open('elevation_small.txt', 'r')
        elevation = elevation_small_file.readlines()
        # clean_elevation = [letter.replace('\n', '').strip().split() for letter in elevation]
        print(elevation)
        return elevation

    print(open_file)
        
        # def clean_text(self):   
    # elevation_list = [[int(clean_elevation) for clean_elevation in row] for row in clean_elevation]
    # max_elevation = max(elevation_list)
    # max_max_elevation = max(max_elevation)
    # min_elevation = min(elevation_list)
    # min_min_elevation = min(min_elevation)
    # print(min_min_elevation)