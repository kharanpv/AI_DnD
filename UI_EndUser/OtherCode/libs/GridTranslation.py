CURRENT_FACTOR = 512
def get_true_coords(coords):
    return coords.x/CURRENT_FACTOR, coords.y/CURRENT_FACTOR, coords.z/CURRENT_FACTOR

def convert_coords(coords):
    coords.x =  coords.x * CURRENT_FACTOR
    coords.y = coords.y * CURRENT_FACTOR
    coords.z = coords.z * CURRENT_FACTOR
    return coords
