

[![oldjaponec](https://img.shields.io/github/followers/oldjaponec?label=Follow%20me&style=social)](https://github.com/OldJaponec)
[![OCR](https://img.shields.io/badge/API-Free_OCR-orange?style=plastic)](https://ocr.space/ocrapi)
![tests](https://img.shields.io/badge/tests-60%25-yellowgreen?style=plastic)
[![MongoDB](https://img.shields.io/badge/Mongo-DB-green?style=plastic)](https://www.mongodb.com/)
[![python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue?style=plastic)](https://www.python.org/)
[![compvision](https://img.shields.io/badge/Computer-Vision-red?style=plastic)](https://en.wikipedia.org/wiki/Computer_vision)


# License plate reader

<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/app.png' width=100%>


### Table of Contents
> ##### [1. Description](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#1-description-1)
> ##### [2. Installation and setup](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#2-installation-and-setup-1)
   >> ##### [2.1. Install Python](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#21-install-python-2)
   >> ##### [2.2. Run the Terminal](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#22-run-the-terminal-2)
   >> ##### [2.3. Install pip](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#23-install-pip-2)
   >> ##### [2.4. Installing the required libraries](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#24-installing-the-required-libraries-2)
   >> ##### [2.5. Dowload project files](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#25-dowload-project-files-2)
   >> ##### [2.6. Connecting to the Free OCR API](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#26-connecting-to-the-free-ocr-api-2)
   >> ##### [2.7. Connecting to the MongoDB](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#27-connecting-to-the-mongodb-2)
> ##### [3. Tests](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#1-tests)
> ##### [4. Contacts](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#4-contacts)



---

### 1. Description

This program is a test assignment, which you can find at the link.

The program uses the [Free OCR API](https://ocr.space/ocrapi).

As a test, the program gets images with license plates from the "images" folder in root directory. In this case they are [Israeli license plates]((https://www.google.com/search?q=israeli+license+car+plate&tbm=isch&ved=2ahUKEwj0wdT-iaf6AhWxpYsKHcXLDG4Q2-cCegQIABAA&oq=israeli+license+car+plate&gs_lcp=CgNpbWcQAzoECCMQJzoFCAAQgARQ5hFYpDdggz5oAHAAeACAAU6IAZwFkgEBOZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=hKMrY_TvILHLrgTFl7PwBg&bih=969&biw=1920&hl=en)) downloaded in advance from [google images ](https://www.google.com/search?q=israeli+license+car+plate&tbm=isch&ved=2ahUKEwj0wdT-iaf6AhWxpYsKHcXLDG4Q2-cCegQIABAA&oq=israeli+license+car+plate&gs_lcp=CgNpbWcQAzoECCMQJzoFCAAQgARQ5hFYpDdggz5oAHAAeACAAU6IAZwFkgEBOZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=hKMrY_TvILHLrgTFl7PwBg&bih=969&biw=1920&hl=en)for the test. The program scans them for license plates. And if one of them is found in the image, the program decides whether to let the car through or not, according to the given conditions, in this example:

 + Cars with license plates that end in 25 or 26 are 
public transport and should be let through.
 + Cars with license plates ending in 85, 86, 87, 88, 89 and 00 should not be let in.
 + Vehicles with license plates with 7 digits long and ending in 0 or 5 should not be allowed in.

All actions are written to the [mongoDB](https://www.mongodb.com/) database. In the form of:

 + Database identifier(automatic [mongoDB](https://www.mongodb.com/))
 + Car plate.
 + Date and time.
 + Deciding.

For the test, the console prints all errors at the stages of opening the file and determining the license plate number. If successful, the console prints the license plate number and decision to skip the car.


---

### 2. Installation and setup
   > ##### [2.1. Install Python](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#21-install-python-2)
   > ##### [2.2. Run the Terminal](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#22-run-the-terminal-2)
   > ##### [2.3. Install pip](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#23-install-pip-2)
   > ##### [2.4. Installing the required libraries](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#24-installing-the-required-libraries-2)
   > ##### [2.5. Dowload project files](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#25-dowload-project-files-2)
   > ##### [2.6. Connecting to the Free OCR API](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#26-connecting-to-the-free-ocr-api-2)
   > ##### [2.7. Connecting to the MongoDB](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/blob/main/README.md#27-connecting-to-the-mongodb-2)


#### 2.1. Install Python

First you need to install [python](https://www.python.org/) if you don't have it. Or skip this point if [python](https://www.python.org/) is already installed on your computer.

You can [download and install python](https://www.python.org/) from the [official website](https://www.python.org/). For Windows, check the checkbox to set pip in the menu.


#### 2.2. Run the Terminal

To run the console on windows press Win+R and enter cmd in the window that appears. For Linux press ctrl + alt + T to open a terminal. On Mac OC press Command+Space.


#### 2.3. Install pip

First you have to check if you have [pip](https://pypi.org/). You can do this with a command in the terminal

`pip --version`

It also works for Windows, Mac and Linux.
If you get something like this:

`pip 22.2.2 from /home/oldjaponec/.local/lib/python3.8/site-packages/pip (python 3.8)`

You have [pip](https://pypi.org/) on your computer. Otherwise we need to install it.

For Linux:

`sudo apt-get install python3-pip`

For Mac:

`sudo easy_install pip`

For Windows, you need to download [pip](https://pypi.org/) from the [official website ](https://pypi.org/) and install it following the instructions.

#### 2.4. Installing the required libraries

We need several libraries to run the program.

Just copy the code and run it line by line in your [terminal](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot#22-run-the-terminal-1).

`pip install requests`

`pip install python-dotenv`

`pip install pymongo`

#### 2.5. Dowload project files

Download or copy all the files from this repository. Make sure that the files are in the same folder - the root folder of your project. Create an images folder and fill it with [car plates](https://www.google.com/search?q=israeli+license+car+plates&sxsrf=ALiCzsYLLKYUYWmImY_JJo9zKbUeKRMK0w:1664225930308&source=lnms&tbm=isch&sa=X&ved=2ahUKEwibqZvbrLP6AhWmmIsKHTAvC4cQ_AUoAXoECAEQAw&biw=1536&bih=758&dpr=1.25).

#### 2.6. Connecting to the [Free OCR API](https://ocr.space/OCRAPI)

Go to the [OCRAPI website](https://ocr.space/OCRAPI) and register. After confirming your email, you will receive the API key. Copy it and paste it into the .env file that is in your root folder. Instead of `<api_key>` in the line:

`API_KEY=<api_key>`

You get something like this:

`API_KEY=H53761852795248`

#### 2.7. Connecting to the [MongoDB](https://www.mongodb.com/)

Go to the [MongoDB website](https://www.mongodb.com/) and click Try Free. Fill out the form. Choose Python and name your project. Create Cluster. It's going to take some time.

<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/f9b69f1596a0c420b7a25c1006db0a0b9d897497/screens/1.png' width=70%>
<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/2.png' width=70%>

After completing the creation process, you must add a new database user: 

<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/3.png' width=70%>
<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/4.png' width=70%>

Paste the user's password into the .env file instead of `<user_password>`:

`MONGO_USER_PASSWORD=<user_password>`

You get something like this:

`MONGO_USER_PASSWORD=mysecretpassword1234`

Add your IP adress:

<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/5.png' width=70%>
<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/6.png' width=70%>

Add your own database:

<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/7.png' width=70%>
<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/8.png' width=70%>

Insert the name of the base and the collection in the corresponding fields by analogy above:

`MONGO_DATABASE_NAME=<database_name>`

`MONGO_DATABASE_COLLECTION_NAME=<collection_name>`

Connect your application:

<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/9.png' width=70%>
<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/10.png' width=70%>
<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/11.png' width=70%>
<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/12.png' width=70%>
<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/13.png' width=70%>
<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/14.png' width=70%>

Copy conection string and past in the corresponding field in .env:

`MONGO_CONNECTION_STRING=<connection_string>`

### 1. Tests

Open a terminal and navigate to your project folder. To do this, you can copy the path from the line of your file browser and paste it after the `cd` command. Something like this, depending on your OS:

`cd /home/projects/reads_license_plates_in_the_parking_lot`

Then run main.py with the command:

`python3 main.py`

Or for some systems

`python main.py`

If you've done it right, you'll see something like this:

```
There is no license plate on the image  ./images/car_plate_8.jpg
21217561 : YES
There is no license plate on the image  ./images/car_plate_9.jpeg
There is no license plate on the image  ./images/car_plate_3.jpg
2222277 : YES
8118508 : YES
31029651 : YES
1797765 : NO
There is no license plate on the image  ./images/car_plate_1.jpeg
There is no license plate on the image  ./images/car_plate_6.jpeg
```

And new entries will appear in your database

<img src='https://raw.githubusercontent.com/OldJaponec/reads_license_plates_in_the_parking_lot/main/screens/tests.png' width=70%>

### 4. Contacts

If you have questions you can create a new [discussion](https://github.com/OldJaponec/reads_license_plates_in_the_parking_lot/discussions) or email oldjaponec@gmail.com
