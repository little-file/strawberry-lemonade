import os
from flask import Flask, render_template, request

app = Flask(__name__)

def is_root_directory(path):
    return path == "/"

@app.route('/', methods=['GET', 'POST'])
def home():
    base_directory = os.path.expanduser("~")
    files_and_folders = os.listdir(base_directory)

    selected_item = None
    selected_item_content = None

    if request.method == 'POST':
        selected_item = request.form.get('selected_item')

        if selected_item:
            selected_item_path = os.path.join(base_directory, selected_item)

            if os.path.isdir(selected_item_path):
                selected_item_content = os.listdir(selected_item_path)

    return render_template('index.html', files_and_folders=files_and_folders, selected_item=selected_item, selected_item_content=selected_item_content)

if __name__ == '__main__':
    app.run(debug=True)