"""
fetching dog pictures with the requests library

> make sure you run `source .adv/bin/activate` from your top-level
advanced cs folder before starting!
> run this file by typing in the terminal `python3 dog-images.py`
> API documentation: https://dog.ceo/dog-api/documentation
"""

import requests

# ======================================================================
# MODEL 1 -- Making a request                          
#
# An API (application programming interface) lets one program ask another
# program, usually running on a server somewhere else, for data. The Dog
# API answers requests with dog pictures. 
#
# Call the following function to answer the questions.
# ======================================================================

def part_a():
    # --- Part A: ask for a random dog picture ---
    print("===== PART A =====")
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    print("type(response):", type(response))
    print("status code:", response.status_code)
    print("response.text:", response.text)

    data = response.json()
    print("type(data):", type(data))
    print("data:", data)
    print("keys:", list(data.keys()))
    print("image URL:", data["message"])

# Q1. What type of object does requests.get(url) return? 
#
#
#

# Q2. Compare response.text and data. What is the data type of each? How
#     do they look different when printed?
#
#


# Q3. What keys does the dictionary data have? Which key holds the web
#     address of the dog picture?
#
#


# Q4. Copy the image URL that was printed and paste it into a web browser.
#     What do you see? Then call part_a() again. Is the URL the same? Why
#     do you think that is?
#
#

# ======================================================================
# MODEL 2 -- Breeds and building URLs                  
#
# As we saw yesterday, the Dog API can give us a list of all breeds. 
# It can also return a random picture of a specific breed. To ask for 
# a specific breed, we build the URL with an f-string.
#
# Call the following functions to answer the questions.
# ======================================================================

def get_random_image_url(breed):
    # helper function -- returns the url of a random image of a 
    # specific breed, which is passed in as a parameter
    url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(url)
    data = response.json()
    return data["message"]

# Q5. In get_random_image_url, which part of the URL changes depending on
#     the breed? Write the URL that is built when breed is "husky".
#
#
#

def part_b():
    # --- Part B: a breed that does not exist ---
    print("===== PART B =====")
    response = requests.get("https://dog.ceo/api/breed/unicorn/images/random")
    print("status code:", response.status_code)
    print("data:", response.json())


# Q6. Call part_b(). How does the status code and the contents of the
#      data differ from a successful request?
#
#
#

# Q7. Suppose get_random_image_url("unicorn") were called. Based on part_b,
#      what would it return? Why would that be a problem for a program that
#      expects a web address?
#
#
#

# YOUR TURN: Write a function named is_valid_breed(breed) that returns
#            True if breed is one of the breeds from the API, and
#            False if it is not. You should refer back to your notes from 
#            yesterday to make a request to get all of the breeds. 
#            Be sure to test your function!

def is_valid_breed(breed):
    pass


# ======================================================================
# MODEL 3 -- Saving an image                           
#
# The picture itself is not JSON. When we request an image URL, the
# server sends back the raw data of the image file, which Python stores
# as bytes. To save the picture, we write those bytes to a file.
#
# Note: Files are saved in the same folder as this .py file.
#
# Call the following functions to answer the questions.
# ======================================================================

def part_c():
    # --- Part C: what does an image look like to Python? ---
    print("===== PART C =====")
    image_url = get_random_image_url("beagle")
    print("image URL:", image_url)
    response = requests.get(image_url)
    print("status code:", response.status_code)
    print("type(response.content):", type(response.content))
    print("type(response.text):", type(response.text))
    print("number of bytes:", len(response.content))
    print("first 20 bytes:", response.content[:20])

# Q8. In part_c, what is the data type of response.content? How is it
#      different from the data type of response.text? Why do you think
#      image data is stored in this type?
#
#
#

# Q9. How many bytes does the image have? About how many kilobytes is
#      that (1 kilobyte = 1024 bytes)?
#
#
#

def save_image(image_url, filename):
    # helper function -- saves an image from image_url as filename
    response = requests.get(image_url)
    with open(filename, "wb") as outfile:
        outfile.write(response.content)

def part_d():
    # --- Part D: save a picture ---
    print("===== PART D =====")
    image_url = get_random_image_url("beagle")
    save_image(image_url, "dog.jpg")
    print("saved dog.jpg")

# Q10. Call part_d(). Find dog.jpg in your folder and open it. What do you
#      see? Then call part_d() again. Is the picture the same? What
#      happened to the first picture?
#
#
#

# Q11. In save_image, the file is opened with the mode "wb". Compare it to
#      the modes "w" and "r" you used in earlier activities. What do you
#      think the "b" stands for?
#
#
#

def part_e():
    # --- Part E: what if we use "w" instead of "wb"? ---
    print("===== PART E =====")
    response = requests.get(get_random_image_url("beagle"))
    with open("broken.jpg", "w") as outfile:
        outfile.write(response.content)

# Q12. Call part_e(). What type of error occurred? Explain why it happened.
#      Then look at the image in Finder: how big is broken.jpg?
#
#
#

def part_f():
    # --- Part F: getting a file name from a URL ---
    print("===== PART F =====")
    image_url = "https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg"
    pieces = image_url.split("/")
    print("pieces:", pieces)
    print("last piece:", pieces[-1])

# Q13. In part_f, what does split("/") return? Why is the last piece,
#      pieces[-1], a good name for a file?
#
#
#

def filename_from_url(image_url):
    return image_url.split("/")[-1]

# Q14. Why would it be better to name each saved picture with filename_from_url
#      than to always save it as "dog.jpg"?
#
#
#

# YOUR TURN: Write a function named save_random_dog(breed) that:
#              - gets a random image URL for the breed,
#              - gets a file name using filename_from_url,
#              - saves the picture with save_image,
#              - prints a message such as  Saved n02088094_1003.jpg

def save_random_dog(breed):
    pass


# ======================================================================
# MODEL 4 -- Several pictures at once                  
#
# The Dog API can return several random pictures of a breed in a single
# request by adding a number to the end of the URL.
#
# Call the following function to answer the questions.
# ======================================================================

def get_image_urls(breed, count):
    url = f"https://dog.ceo/api/breed/{breed}/images/random/{count}"
    response = requests.get(url)
    data = response.json()
    return data["message"]

def part_g():
    # --- Part G: three husky pictures ---
    print("===== PART G =====")
    urls = get_image_urls("husky", 3)
    print("type(urls):", type(urls))
    print("len(urls):", len(urls))
    for image_url in urls:
        print(image_url)

# Q15. In Model 2, data["message"] was a string. What is the data type of
#      the "message" value in this model? What does it contain?
#
#
#

# YOUR TURN: Write a function named save_many(breed, count) that gets a
#            list of image URLs with get_image_urls and uses a loop to
#            save every picture (naming each file with filename_from_url).

def save_many(breed, count):
    pass

# Q16. How many requests does save_many("husky", 3) send in total? Explain
#      how you counted.
#
#
#

# ======================================================================
# EXTENSIONS 
# ======================================================================

# EXTENSION 1 -- Handle errors
#   A program that sends requests over the internet should expect things
#   to go wrong: a breed may not exist (as in part_b), or the internet
#   connection may fail. Write a function named safe_random_image_url
#   (breed) that:
#     - returns None (and prints a helpful message) if the status code
#       is not 200, and
#     - returns the image URL otherwise.
#   Then make it also handle a failed connection by wrapping the request
#   in a try/except. (Hint: the error to catch is
#   requests.exceptions.RequestException, and you can add timeout=10 to
#   requests.get so it doesn't wait forever.)

# EXTENSION 2 -- Sub-breeds
#   Write a function named get_sub_breeds(breed) that returns the list of
#   sub-breeds, and a function named get_sub_breed_image_url(breed,
#   sub_breed) that returns a random image URL. Then save one picture of
#   each of the first three sub-breeds of hound.

# EXTENSION 3 -- Chart the breeds
#   The URL  https://dog.ceo/api/breed/<breed>/images  returns a list of
#   ALL the images of a breed. Using these eight breeds:
#       ["beagle", "boxer", "husky", "pug", "poodle", "akita", "collie",
#        "labrador"]
#   build a dictionary that stores the number of images of each breed
#   (the length of that list). Then create a bar chart with matplotlib.
#   Which breed has the most pictures?
