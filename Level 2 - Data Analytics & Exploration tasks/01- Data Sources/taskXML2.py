import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('movie.xml')  # Make sure the XML file is named 'movie.xml'
root = tree.getroot()

# Variables to count favorite and non-favorite movies
favorite_count = 0
non_favorite_count = 0

# Iterate over each movie in the XML
for movie in root.iter('movie'):
    # List all child tags of the movie element
    print(f"Child tags of {movie[1].attrib.get('title')}:", [child.tag for child in movie])
    
    # Print out the movie descriptions using itertext()
    print(f"Description of {movie.attrib.get('title')} :", ''.join(movie.find('description').itertext()).strip())
    
    # Count the number of favorite and non-favorite movies
    if movie.attrib['favorite'] == "True":
        favorite_count += 1
    else:
        non_favorite_count += 1

# Print out the number of favorite and non-favorite movies
print(f"\nNumber of favorite movies: {favorite_count}")
print(f"Number of non-favorite movies: {non_favorite_count}")
