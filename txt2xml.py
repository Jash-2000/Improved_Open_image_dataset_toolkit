######################

## Author : Jash Shah
## Date : 31/3/21

###################

"""
Directory Structure of the Dataset should be as follows. (The topmost row denotes outermost directory)
 
    -> OID
    -> Dataset
    -> train or test or validation folder
    -> Individual class folders
    -> Individual Images

"""

import xml.etree.ElementTree as ET
import os
import numpy as np
import pandas as pd
import cv2
print("Requirements are fullfilled\n")

def convert2xml( folder , name , df_main , df , h, w , c):
    df_modified = pd.DataFrame(columns=['ImageID','Source','LabelName','Confidence','XMin','XMax','YMin','YMax','IsOccluded','IsTruncated','IsGroupOf','IsDepiction','IsInside'])

    for i,rows in df_main.iterrows():
        flag = 0 
        
        if str(name) == str(rows['ImageID']):
            
            for j,r in df.iterrows():
                if ( str(r['Code']) == str(rows['LabelName']) ):
                    rows['LabelName'] = str(r['Classes'])
                    flag = 1
            
            new_rows = []
            if flag == 1:
                new_rows.append(rows.values)
                df_modified = df_modified.append(pd.DataFrame(new_rows, columns=df_modified.columns)).reset_index()

    df_modified = df_modified.drop( ['index','ImageID','Source','Confidence'], axis = 1)
    print(df_modified.head())
    #input("Continue?")      # Interrupt added for testing the code.
    
    #####################################################################################################
    
    print("\nCreating the xml files for the file : ",name,".jpg")
    image_name = name + ".jpg"
    
    annotation = ET.Element('annotation')
    fileName = ET.SubElement(annotation, 'filename')
    fileName.text = image_name
    
    size = ET.SubElement(annotation, 'size')
    width = ET.SubElement(size, 'width')
    width.text = str(w)
    height = ET.SubElement(size, 'height')
    height.text = str(h)
    depth = ET.SubElement(size, 'depth')
    depth.text = str(c)
    
    for i,rows in df_modified.iterrows():
        obj = ET.SubElement(annotation, 'object')
        
        Name = ET.SubElement(obj, 'name')
        Name.text = str(rows['LabelName'])
        inside = ET.SubElement(obj, 'inside')
        inside.text = str(rows['IsInside'])
        truncated = ET.SubElement(obj, 'truncated')
        truncated.text = str(rows['IsTruncated'])
        occluded = ET.SubElement(obj, 'occluded')
        occluded.text = str(rows['IsOccluded'])
        groupof = ET.SubElement(obj, 'groupof')
        groupof.text = str(rows['IsGroupOf'])
        depiction = ET.SubElement(obj, 'depiction')
        depiction.text = str(rows['IsDepiction'])

        bbox = ET.SubElement(obj, 'bndbox')
        
        xmin_value = float(rows['XMin']) * w
        xmin = ET.SubElement(bbox, 'xmin')
        xmin.text = str(xmin_value)
        
        ymin_value = float(rows['YMin']) * h
        ymin = ET.SubElement(bbox, 'ymin')
        ymin.text = str(ymin_value)

        xmax_value = float(rows['XMax']) * w
        xmax = ET.SubElement(bbox, 'xmax')
        xmax.text = str(xmax_value)
        
        ymax_value = float(rows['YMax']) * h
        ymax = ET.SubElement(bbox, 'ymax')
        ymax.text = str(ymax_value)
        # End of one object

    # Writing in XML file
    xml_folder = output_folder + "/xml_files"
    try:
        os.mkdir(xml_folder)
    except:
        pass
    xml_file = xml_folder + "/" + name + ".xml"
    print("\n Completed the xml generation. Now saving the files as ", xml_file)

    # Saving the XMl document now
    mydata = ET.tostring(annotation)
    myfile = open(xml_file, "wb")
    myfile.write(mydata)
    
# End of Function
################################################################################################################

input_path = "OID/csv_folder/"          # Path for the csv files 

df = pd.read_csv(input_path + "class-descriptions-boxable.csv")
df.columns = ["Code" , "Classes"]

Mylist = ["Apple", "Orange"]         # List of required classes

# Dropping the unneccesarry classes
for i,row in df.iterrows():
    if row["Classes"] not in Mylist:
        df = df.drop(index = i, axis = 0)

print("Printing the dataframe containing just the required classes\n")
print(df)
input("\n Press any key to continue")

######################################################################################

input_folder = "OID/Dataset/"                     # Path where the images get stored

for files in os.listdir(input_folder):
    output_folder = input_folder + files

    if(files == "test"):
        df_test = pd.read_csv(input_path + "test-annotations-bbox.csv")
        
        for file in os.listdir(input_folder + files):
            for file_name in os.listdir(input_folder + files + "/" + file):
                im = cv2.imread(input_folder + files + "/" + file + "/" + file_name)
                h,w,c = im.shape
                if (str(file_name)[-4:] == ".jpg" ):            
                    convert2xml(output_folder, str(file_name)[:-4], df_test, df, h, w, c)

    elif(files == "train"):
        df_train = pd.read_csv(input_path + "train-annotations-bbox.csv")

        for file in os.listdir(input_folder + files):
            for file_name in os.listdir(input_folder + files + "/" + file):
                im = cv2.imread(input_folder + files + "/" + file + "/" + file_name)
                h,w,c = im.shape
                if (str(file_name)[-4:] == ".jpg" ):            
                    convert2xml(output_folder, str(file_name)[:-4], df_train, df, h, w, c)

    elif(files == "validation"):
        df_val = pd.read_csv(input_path + "validation-annotations-bbox.csvs")

        for file in os.listdir(input_folder + files):
            for file_name in os.listdir(input_folder + files + "/" + file):
                im = cv2.imread(input_folder + files + "/" + file + "/" + file_name)
                h,w,c = im.shape
                if (str(file_name)[-4:] == ".jpg" ):            
                    convert2xml(output_folder, str(file_name)[:-4], df_val, df, h, w, c)

    else:
        print("\n\n The directory structure of your dataset is incorrect!! Please read the code from line 27 \n")