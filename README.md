# Automatic Metadata Retrieval App for Audacity Recordings using Discogs API

## Overview

This application is designed to streamline the process of filling in metadata for audio recordings in Audacity. It leverages the Discogs API to automatically fetch relevant details for a given Discogs release ID and populate them in Audacity's metadata fields. The app is built using C# with WPF and follows the MVVM (Model-View-ViewModel) architectural pattern. Additionally, it utilizes a Python script powered by `pyautogui` for automating the metadata filling process.

## Features

- **Discogs Integration:** The app takes a Discogs release ID as input and fetches essential metadata for the corresponding release from Discogs using the `Discogs.Client` library.

- **User Interface:** Built with WPF, the app offers an intuitive user interface that enables users to input the Discogs release ID and initiate the metadata retrieval process.

- **MVVM Architecture:** The app follows the MVVM pattern, keeping a clear separation between the application's logic, user interface, and data.

- **Automated Metadata Filling:** After the user clicks the "Save Track Details" button, a Python script powered by `pyautogui` is triggered. This script interacts with the Audacity application, automatically populating the metadata fields with the retrieved information.

- **Audacity Requirement:** The app requires Audacity to be actively open (not in the background) during the metadata filling process.

- **Custom Snapshot:** Please note that you need to provide your own screenshot (snip) of the Audacity application with the relevant metadata fields visible. This is because the positioning and appearance of elements can vary across different computer setups and resolutions.

## Getting Started

1. **Clone Repository:** Clone this repository to your local machine.

2. **Install Dependencies:** Ensure you have the necessary dependencies installed. Run `pip install pyautogui` to install the required Python library.

3. **Compile and Run:** Open the solution in Visual Studio and compile the project. Launch the application.

4. **Provide Snipshot:** Before using the "Save Track Details" functionality, take a screenshot (snip) of Audacity with the metadata fields visible. Replace the default snip in the provided Python script with your custom snip.

5. **Input Discogs Release ID:** Enter the Discogs release ID for the recording you want to retrieve metadata for.

6. **Save Track Details:** Click the "Save Track Details" button. This action triggers the Python script to initiate the metadata filling process.

7. **Audacity Interaction:** Make sure Audacity is actively open on your system. The Python script will use `pyautogui` to navigate Audacity and populate metadata fields based on the retrieved information.
