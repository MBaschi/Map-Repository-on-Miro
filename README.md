# Python Folder Structure Visualizer for Miro 
## Overview 
The aim of this project is to create a Miro board to visualize the structure of a folder or an application written in Python. This tool is useful for creating an initial board to take notes about the folder/files/code of the application. Given a path to a local folder, the program cycles through the folder and sends requests to plot elements with their names as rectangles on the Miro board.

## How to Use 
1. Create a Miro Developer Board
Follow the tutorial provided by Miro to create a developer board: Getting Started with OAuth

2. Save Token and Board URL/ID
After creating the Miro developer board, save the token and URL or ID of the board.

3. Clone the Repository
Clone this repository to your local machine
4. Configure the Application
Edit the configuration file (config.json) and insert the following information:

Path to the folder you want to visualize.
Miro token obtained from step 2.
Board ID or URL obtained from step 2.
5. Run the Application
Execute the main script to visualize the folder structure on the Miro board

6. Interact with the Miro Board
Once the program is run successfully, the Miro board will be populated with rectangles representing different elements such as folders, files, and Python classes inside the files. You may need to move around the board and zoom out to find the map as the view may not be in the correct initial position.

# Notes 
Ensure that the provided Miro token and board details are accurate in the configuration file to avoid authentication errors.
It's recommended to review the Miro API documentation for advanced usage or customization options.
# Credits 
This project was developed by Matteo Baschieri.
