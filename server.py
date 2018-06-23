from flask import Flask, flash, request, redirect, url_for, render_template
import os
import intel

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = os.path.join('./static', file.filename)
            file.save(filename)
            classes = intel.what_class(filename)
            return render_template('image.html', classes = classes, filename = file.filename)
    return render_template('main.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)
