'''Module importing ElementTree library'''
import xml.etree.ElementTree as ET

# Parse the movie.xml file
tree = ET.parse('movie.xml')
root = tree.getroot()

# 1. List all the child tags of the 'movie' element using iter()
print("Child tags of the 'movie' element:")
for movie in root.iter('movie'):
    child_tags = [sub_child.tag for sub_child in movie]
    print(child_tags)
    break  # Only print once, then break the loop

# 2. Use itertext() to print out the movie descriptions
print("\nMovie Descriptions:")
for movie in root.iter('movie'):
    description = movie.find('description')
    if description is not None:
        print(
            f"Description of {movie.attrib.get('title')} :"
            + description.text.strip()
        )

# 3. Count the number of movies that are favorites and not
favourites_count = 0
not_favourites_count = 0

# Loop through each movie to check the 'favorite' attribute
for movie in root.iter('movie'):
    if movie.attrib['favorite'] == "True":
        favourites_count += 1
    else:
        not_favourites_count += 1

print(f"\nNumber of favourite movies: {favourites_count}")
print(f"Number of movies that are not favourites: {not_favourites_count}")
