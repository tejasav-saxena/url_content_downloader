from flask import Flask, request, render_template, redirect, url_for
import os
from concurrent.futures import ThreadPoolExecutor
import requests

app = Flask(__name__)

def download_content(url, save_dir):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        file_name = os.path.join(save_dir, url.split("/")[-1] or "index.html")
        with open(file_name, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    urls = request.form["urls"].splitlines()
    save_dir = request.form.get("directory", "downloads")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda url: download_content(url, save_dir), urls)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
