# **Youtube to MP4 Converter**

## **Video Demo**
https://youtu.be/OGDErmPB-lg

## **Description**:
When I find myself coding for several hours, I usually go on Youtube.com and find music to help me focus. I had decided it would be best to download some of those songs onto my computer, just in case they get removed from the platform or if the website was down for some reason. Therefore, I created a program that takes any video from Youtube and downloads the audio from the video as an MP4 file. When a video is downloaded, a CSV file will be created that will show what videos have been downloaded using the program as well. This can be used so users know what videos they have already downloaded.

## **How to Use**
When running the program, the user is greeted with a graphical user interface that has a text entry box. Simply copy the link from a Youtube video and if the link is valid, the audio will be downloaded to a folder within the program(Pytube Downloader). A CSV file will be created and the title, author, and Youtube link will be written.

## **Notable Libraries Used**
- pytube
- tkinter

## **Functions**
- check_valid_link: This function uses regular expression and ensures the link that is provided by the user is a valid Youtube link. If the link matches the regular expression, it's returned, but if not, a messagebox provided by tkinter informs the user the input is not a valid link. When the user clicks the "convert" button, this is the first function that the program runs. 
- convert: The link from check_valid_link is utilized by pytube to download the highest quality, audio only stream of the video. Throughout this process, the user is greeted with messageboxes that confirm if the user is downloading the correct video and also lets them know when their download is complete.
- get_csv: A CSV file is created or added to (depends if the csv is already present in the operating system). This file contains the title of the video, the channel, and the link of the video.

## **What I Learned**
In this project, I wanted to focus on the user experience. By using tkinter, I was able to create a GUI that the user interacts with and gives various updates regarding the user's download. I made certain design choices I thought were appropriate such as font size and even had to adjust the colors of backgrounds of tkinter's labels and buttons.

## **Limitations**
The main limitation is Youtube can change certain things in their backend, causing pytube to crash. I ran into this issue when writing my program and had to use stackoverflow to solve this issue. I essentially went into the pytube folder and edited the library as suggested by other users and my program began working.



