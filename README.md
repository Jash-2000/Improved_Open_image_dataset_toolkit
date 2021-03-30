# Open Image Dataset Downloder Toolkit

This repo has been forked from [cavidparker](https://github.com/cavidparker/open_image_dataset_downloader) with the sole reason of adding **__Resumeable__ and __version switching__** features in the standard toolkit. This would be useful in case the user has connectivity issues or power outrages. Also, I have updated the readme to provide comprehensive instructions of use. 

For getting more information about Open Images Dataset, please go through [Info.md](https://github.com/Jash-2000/open_image_dataset_downloader/blob/main/Info.md) file. 

## Downloading required files

For downloading the bounding box csv files 
* Follow the instructions provided at the official link of [Open-Images Dataset](https://storage.googleapis.com/openimages/web/download.html). You would be required to download the 4 csv files as explained over here. 

* Alternatively, you can also follow the following steps

    ```
    # get the training data
    wget https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/train-images-boxable.csv
    wget https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/train-annotations-bbox.csv

    # get the test data
    wget https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/test-annotations-bbox.csv
    wget https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/test-images.csv
    ```
* In case you directly know the Version file's URL, you can directly download from there. For example, for the using the latest version, download from the following URLs

    * [https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv](https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv)
    
    * [https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv](https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv)
    
    * [https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv](https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv) 

* Using the automated script files

    The file **module/bounding_boxes.py** already contains the above mentioned code. So, it will prompt you to donwload all the required files the first time you run the code.

**P.S -  If you clone this repo, you will already have the csv files present in **/OID/csv_folder** for V4. In case you want to work with other versions, delete the present files and overwrite them with the new files**

## Paraser Arguments

* type_csv - Which class of images you want to download [ train, test, val or all]
* classes - Space seperated name of classes you want to dowload
* limit - Limit the number of images you want to download

## Steps to be followed if you are resuming the paused download

**Python3 is required**
 
* Run the following command to implement simple resume feature

```shell
    python main.py downloader --resume
```

* In case you want to add additional items when resuming, run the following script
```shell
    python main.py downloader --classes Apple Orange --type_csv all --limit 400
```


**By default, the script is configured to resume downloading from the previous state. In case you do not wish to do so, delete **log.csv** file present in the master folder**.

## Steps to be followed if you are downloading the images.

**Python3 is required.**

1. Clone this repository
    
    ```
        git clone https://github.com/Jash-2000/open_image_dataset_downloader.git
    ```

2. Install the required Images
    
    ```python
        pip install -r requirements.txt
    ```

3. First of all, if you simply want a quick reminder of al the possible options given by the script, you can simply launch, from your console of choice, the main.py. Remember to point always at the main directory of the project

    ```shell
        python3 main.py
    ```

    or in the following way to get more information

    ```shell
        python3 main.py --help
    ```
    
    The full list of Parsers is present in the **/Modules/parser.py**

4. Download different classes in seperate folders
    
    ```shell
        python main.py downloader --classes Balloon Airplane --type_csv train --limit 400   
    ```

5. download in the same folder

    ```shell
        python main.py downloader --classes Balloon Airplane --type_csv train --limit 1000 --multiclasses 1
    ```

## Sources of error
 
   * If you are running the code for the first time (i.e. you are not resuming the code), make sure to delete the **log.csv** file. Different version of Pandas have different rule for overwriting.

   * Make sure you have downloaded the corrrect bounding box csv file.
   * Make sure that the class labels have been called correctly while running the script.

## Downloaded file's structure

The algorith will take care to download all the necessary files and build the directory structure like this:

```
main_folder
│   main.py
│
└───OID
    │   file011.txt
    │   file012.txt
    │
    └───csv_folder
    |    |
    |    └───v4
    |    |
    |    └───v5
    |    |
    |    └───v6
    |         │   class-descriptions-boxable.csv
    |         │   validation-annotations-bbox.csv
    |
    └───Dataset
        |
        └─── test
        |
        └─── train
        |
        └─── validation
             |
             └─── v4
             |
             └─── v5
             |
             └─── v6
                  |
                  └───Apple
                  |     |
                  |     |0fdea8a716155a8e.jpg
                  |     |2fe4f21e409f0a56.jpg
                  |     |...
                  |     └───Labels
                  |            |
                  |            |0fdea8a716155a8e.txt
                  |            |2fe4f21e409f0a56.txt
                  |            |...
                  |
                  └───Orange
                        |
                        |0b6f22bf3b586889.jpg
                        |0baea327f06f8afb.jpg
                        |...
                        └───Labels
                              |
                              |0b6f22bf3b586889.txt
                              |0baea327f06f8afb.txt
                              |...
```
If you have already downloaded the different csv files you can simply put them in the `csv_folder`. The script takes automatically care of the download of these files, but if you want to manually download them for whatever reason [here](https://storage.googleapis.com/openimages/web/download.html) you can find them.

If you interupt the downloading script `ctrl+d` you can always restart it from the last image downloaded.
