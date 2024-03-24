# Video to Text Extractor
The Video to Text Extractor is a Python application designed to extract text from video files using speech recognition. It provides a user-friendly interface for users to browse, select, and process video files, ultimately producing transcribed text output.

**Features**
1. Browse and Select Video: Users can easily browse their local system and select a video file for processing.

2. Speech Recognition: The application utilizes the SpeechRecognition library to extract audio from the selected video and perform speech recognition on the audio content.

3. Text Output: The transcribed text from the speech recognition process is saved to a text file for further analysis or reference.

4. Graphical User Interface (GUI): The application offers a graphical interface built with PySimpleGUI, allowing users to interact with the program intuitively.

**Dependencies**
The following dependencies are required to run the Video to Text Extractor:

1. Python 3.x: The programming language used for development.

2. PySimpleGUI: Provides the framework for creating the graphical user interface.

3. moviepy: A library for video editing and processing, used here to extract audio from video files.

4. SpeechRecognition: Enables the application to recognize speech from audio files.

**Installation**
To install and run the Video to Text Extractor, follow these steps:

1. Clone the Repository: Clone the project repository to your local machine using Git:
`git clone https://github.com/your_username/video-to-text-extractor.git`

2. Install Dependencies: Navigate to the project directory and install the required dependencies using pip:
`cd video-to-text-extractor
pip install -r requirements.txt`

**Usage**
1. Run the Application: Execute the main Python script video_to_text_extractor.py to launch the application:

`python video_to_text_extractor.py `

2. Browse and Select Video: Use the "Browse" button in the graphical interface to navigate your local file system and select the video file you want to process.

3. Processing and Speech Recognition: Upon selecting the video file, the application will extract audio from the video and perform speech recognition on the audio content.

4. Text Output: The transcribed text will be saved to a text file named recognized.txt in the same directory as the script.

5. View Results: You can open the recognized.txt file using any text editor to view the extracted text.

6. Exit the Application: Close the application window when you're done processing video files.
