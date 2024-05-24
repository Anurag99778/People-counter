# People Counter Project

This project is designed to count the number of people going up and down on an escalator using computer vision techniques. The project uses YOLOv8 for object detection, SORT for object tracking, and OpenCV for image processing and visualization. The results are stored in a database for further analysis.

## Demo 

[![People Counting Project Demo](https://img.youtube.com/vi/OhaHZhh4qnY/0.jpg)](https://youtu.be/OhaHZhh4qnY?si=SFwHvv5wnMlz3Sv8)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/people-counter.git
    cd people-counter
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Download the pre-trained YOLOv8 model weights and place them in the `Yolo-Weights` directory. Ensure the model file is named `yolov8l.pt`.

## Usage

1. Place your video file in the `Videos` directory and name it `people.mp4`.
2. Run the `people-counter.py` script:
    ```sh
    python people-counter.py
    ```
3. The program will start processing the video and display the count of people moving up and down on the screen. The results will be stored in a database through the `insert_counts` function.

## Files

- `people-counter.py`: The main script to run the people counter.
- `mask-1.png`: The mask image to focus on the region of interest.
- `graphics-1.png`: Overlay graphics to display on the video.
- `Yolo-Weights/`: Directory to store the YOLO model weights.
- `Videos/`: Directory to store the input video file.
- `database.py`: Contains the `insert_counts` function to insert counts into the database.
- `requirements.txt`: List of required Python packages.

