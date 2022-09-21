import requests
import json
import os

from database import insert_base
from setting import api_key


# license plate ending lists
public_transport = (['25'], ['26'])
forbidden_numbers = (['61'], ['85'], ['86'], ['87'], ['88'], ['89'] ,['00'])



def check_image(image):
    ''' 
    The function just checks if the file exists
    '''
    try:
        open(image, 'rb')
        return True
    except:
        return False



def ocr_space_file(filename, overlay=False, api_key=api_key, language='eng'):
    '''
    OCR.space API request with local file.
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
    :param api_key: OCR.space API key.
    :param language: Language code to be used in OCR.
            List of available language codes can be found on https://ocr.space/OCRAPI
    :return: Result in JSON format.
    '''

    # specify variables for the API to work
    payload = {'isOverlayRequired': overlay, 'apikey': api_key, 'language': language}
    
    # specify the path to api
    path = 'https://api.ocr.space/parse/image'

    # open image file
    with open(filename, 'rb') as f:

        # send request to api
        result = requests.post(path,
                          files={filename: f},
                          data=payload,
                          )
    # return decode result
    return result.content.decode()



def find_plate(request_result):
    '''
    The function finds the car number in the text of the query result
    :return: True if there is a license plate 
                    and if it is the only one
                    and car number as a string like
             False if there is no license plate 
                    or if there are more that looks like a car license plate
                    and error information
    '''
    
    # load request result as json file
    file_json = json.loads(request_result)

    # get different text on image from json file and convert to list
    text_list = file_json['ParsedResults'][0]['ParsedText'].split('\r\n')

    # list of all numbers on image
    numbers = []

    # go through the list
    for text in text_list:

        # filter only numbers
        number = [ch for ch in text if ch.isdigit()]

        # check number length to find car plate
        if len(number) in (6,7,8):

            # apend number to list of numbers as string type
            numbers.append(''.join(number))

    # if there is a car plate
    if numbers:
        
        # if car plate is the only one
        if len(numbers) != 1:
           
            # return False and information
            return (False, 
                'There is more than one number that looks like a car license plate on the image ')
        else:
            # return True and car plate
            return (True, numbers[0])

    # if not numbers
    return (False,
        'There is no license plate on the image ')



def permit_car(car_plate):
    '''
    The function takes a license plate and checks it against the given conditions
    '''

    # if number is length 7 and ends with 5 or 0
    if len(car_plate) == 7 and car_plate[-1] in ('0', '5'):

        # add to database and return False
        insert_base(car_plate, 'No')
        return False

    # if the last two numbers are numbers in the public transport list
    if car_plate[-2:] in public_transport:

        # add to database and return True
        insert_base(car_plate, 'Yes')
        return True

    # if the last two digits are numbers from the forbidden list
    if car_plate[-2:] in forbidden_numbers:

        # add to database and return False
        insert_base(car_plate, 'No')
        return False

    # if none of the above add to database and return True
    insert_base(car_plate, 'Yes')
    return True



# TESTS
if __name__ == '__main__':

    # specify the path to the folder with images
    images_dir = os.curdir + '/images/'

    # get a list of images
    image_list = [images_dir + file for file in os.listdir(images_dir)]

    # # go through the list
    for image in image_list:

        # if the image does not exist
        if not check_image(image):
            print("This image does not exist: ", image)
            continue

        # send image to api function
        request_result = ocr_space_file(image)
        
        # find car plate on the image
        result_find_plate = find_plate(request_result)

        # if the search fails, print error information
        if not result_find_plate[0]:
            print(result_find_plate[1], image)
            continue

        # else get car plate
        car_plate = result_find_plate[1]

        # we check the number according to the conditions,
        # and print the car number and the answe
        # (the function write the result to the database)

        if permit_car(car_plate):
            print(car_plate, ': YES')
            continue

        print(car_plate, ': NO')

