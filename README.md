# URL Content Downloader

## Description
The **URL Content Downloader** is a web-based application that allows users to download content from multiple URLs and save it locally. Users can input URLs through a simple graphical interface (GUI) built with HTML, which then utilizes a Flask backend to download content concurrently.

## Features
- User-friendly HTML form for URL input.
- Downloads multiple URLs concurrently.
- Saves downloaded content to a specified directory.
- Provides error handling and logs download progress.

## Tech Stack
- **Frontend**: HTML, CSS
- **Backend**: Python, Flask
- **Concurrent Downloads**: Python ThreadPoolExecutor
- **HTTP Requests**: `requests` library

## Screenshot
**After visting website**
![Screenshot 2024-11-04 232408](https://github.com/user-attachments/assets/7a3c643a-1ed6-493d-8bd8-fd10922339f5)
**After enter link or folder name**
![Screenshot 2024-11-04 234139](https://github.com/user-attachments/assets/69acf083-7a16-4ba6-85bd-9acc1f60921e)
**Press download.**


## Prerequisites
- Python 3.x
- `requests` library
- `Flask` library

## Installation

1. **Clone the Repository**
   
   git clone https://github.com/your-username/url-content-downloader.git
   cd url-content-downloader

2. **Install Dependencies Make sure requests and Flask are installed.**
   
   pip install Flask requests

3. **Directory Structure Ensure that index.html is saved in a templates folder within the project directory:**
   
   url-content-downloader/
   ├── app.py
   ├── README.md
   └── index.html   

## Usage

1. Run the Application Start the Flask server by running:
   ```bash
   python app.py

2. Access the Web Interface Open a web browser and go to http://127.0.0.1:5000.

3. Download Content
   -Enter URLs (one per line) in the text area.
   -Specify a directory for saving downloaded files (optional).
   -Click Download to start the process.
   -Content from each URL will be saved in the specified directory.

## Example
1. Sample Input:
   https://example.com
   https://httpbin.org/image/png

2. Output: The content is saved in the specified directory as files named after the URLs.   

## Project Structure

1. app.py - The main Flask application that handles URL processing and downloading.
2. templates/index.html - The front-end interface for user input.
3. README.md - Documentation for the project.

## Contributing
**If you’d like to contribute:**

1. Fork the repository.
2. Create a new feature branch (git checkout -b feature-name).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-name).
5. Open a pull request.

## Acknowledgments
1. The requests library for HTTP requests.
2. The Flask framework for the backend structure.
