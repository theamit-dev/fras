import base64
import binascii
import csv

with open('/Users/lokeshdwivedi/PycharmProjects/FRAS/punjabdataphoto.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        try:
            data = row["|photo|"][1:-1]
            image_64_decode = base64.decodebytes(bytes(data, 'utf-8'))
            pid = row["|pid|"][1:-1]
            path = "/Users/lokeshdwivedi/PycharmProjects/FRAS/images/" + pid + ".jpg"
            image_result = open(path, 'wb')
            image_result.write(image_64_decode)
        except binascii.Error as err:
            pass
