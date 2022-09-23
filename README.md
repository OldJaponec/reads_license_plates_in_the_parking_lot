

[![oldjaponec](https://img.shields.io/github/followers/oldjaponec?label=Follow%20me&style=social)](https://github.com/OldJaponec)
[![OCR](https://img.shields.io/badge/API-Free_OCR-orange?style=plastic)](https://ocr.space/ocrapi)
![tests](https://img.shields.io/badge/tests-60%25-yellowgreen
?style=plastic)
[![MongoDB](https://img.shields.io/badge/Mongo-DB-green?style=plastic)](https://www.mongodb.com/)
[![python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue?style=plastic)](https://www.python.org/)
[![compvision](https://img.shields.io/badge/Computer-Vision-red?style=plastic)](https://en.wikipedia.org/wiki/Computer_vision)


# License plate reader

### Table of Contents
> ##### 1. Description
> ##### 2. Installation and setup
> ##### 3. Tests



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
> ##### 2.1. Install Python
> ##### 2.2. Run the Terminal
> ##### 2.3. Install pip
> ##### 2.4. Installing the required libraries


#### 2.1. Install Python

First you need to install [python](https://www.python.org/) if you don't have it. Or skip this point if [python](https://www.python.org/) is already installed on your computer.

You can [download and install python](https://www.python.org/) from the [official website](https://www.python.org/). For Windows, check the checkbox to set pip in the menu.


#### 2.2. Run the Terminal

To run the console on windows press Win+R and enter cmd in the window that appears. For Linux press ctrl + alt + T to open a terminal. On Mac OC press Command+Space.


#### 2.3. Install pip

First you have to check if you have [pip](https://pypi.org/). You can do this with a command in the terminal

```pip --version```

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

Just copy the code and run it line by line in your terminal.
