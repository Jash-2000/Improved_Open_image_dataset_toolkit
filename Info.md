<h1 align="center"> ~ OIDv4/5/6 ToolKit ~ </h1>

Do you want to build your personal object detector but you don't have enough images to train your model? Do you want to train your personal image classifier, but you are tired of the deadly slowness of ImageNet? Have you already discovered [Open Images Dataset v4](https://storage.googleapis.com/openimages/web/index.html) that has [600](https://storage.googleapis.com/openimages/2018_04/bbox_labels_600_hierarchy_visualizer/circle.html) classes and more than 1,700,000 images with related bounding boxes ready to use? Do you want to exploit it for your projects but you don't want to download gigabytes and gigabytes of data!?

With this repository we can help you to get the best of this dataset with less effort as possible.
In particular, with this practical ToolKit written in Python3 we give you, for both object detection and image classification tasks, the following options:

**(2.0) Object Detection**

* download any of the [600](https://storage.googleapis.com/openimages/2018_04/bbox_labels_600_hierarchy_visualizer/circle.html) classes of the dataset individually, taking care of creating the related bounding boxes for each downloaded image
* download multiple classes at the same time creating separated folder and bounding boxes for each of them
* download multiple classes and creating a common folder for all of them with a unique annotation file of each image
* download a single class or multiple classes with the desired [attributes](https://storage.googleapis.com/openimages/web/download.html)
* use the practical visualizer to inspect the donwloaded classes

**(3.0) Image Classification**

* download any of the [19,794](https://storage.googleapis.com/openimages/web/download.html#attributes) classes in a common labeled folder
* exploit tens of possible commands to select only the desired images (ex. like only test images)


<!-- ![Snippet of the OIDv4 available classes](images/classes.png) -->

# Open Image Dataset v4
All the information related to this huge dataset can be found [here](https://storage.googleapis.com/openimages/web/index.html).
In these few lines are simply summarized some statistics and important tips.

**Object Detection**

<table>
    <tr><td></td><td><b>Train<b></td><td><b>Validation<b></td><td><b>Test<b></td><td><b>#Classes<b></td></tr>
    <tr><td>Images</td><td>1,743,042</td><td>41,620	</td><td>125,436</td><td>-</td></tr>
    <tr><td>Boxes</td><td>14,610,229</td><td>204,621</td><td>625,282</td><td>600</td></tr>
</table>

**Image Classification**

<table>
    <tr><td></td><td><b>Train<b></td><td><b>Validation<b></td><td><b>Test<b></td><td><b>#Classes<b></td></tr>
    <tr><td>Images</td><td>9,011,219</td><td>41,620</td><td>125,436</td><td>-</td></tr>
    <tr><td>Machine-Generated Labels</td><td>78,977,695</td><td>512,093</td><td>1,545,835</td><td>7,870</td></tr>
    <tr><td>Human-Verified Labels</td><td>27,894,289</td><td>551,390</td><td>1,667,399</td><td>19,794</td></tr>
</table>

As it's possible to observe from the previous table we can have access to images from free different groups: train, validation and test.
The ToolKit provides a way to select only a specific group where to search.
Regarding object detection, it's important to underline that some annotations has been done as a group. It means that a single bounding box groups more than one istance. As mentioned by the creator of the dataset:
- **IsGroupOf**: Indicates that the box spans a group of objects (e.g., a bed of flowers or a crowd of people). We asked annotators to use this tag for cases with more than 5 instances which are heavily occluding each other and are physically touching.
That's again an option of the ToolKit that can be used to only grasp the desired images.

Finally, it's interesting to notice that not all annotations has been produced by humans, but the creator also exploited an enhanced version of the method shown here reported [1](#reference)
