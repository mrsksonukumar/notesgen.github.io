from flask import Flask, render_template, request
import pyperclip

app = Flask(__name__)

# Function to generate the note
def generate_note():
    script_type = request.form.get('script_type')

    if script_type == "Manual Planning":
        # Rest of the code for generating the note
        pass

    elif script_type == "2 Person Jobs/Special Condition Planning":
        # Rest of the code for generating the note
        pass

    # Add code for other script types here

# Function to copy the generated note
@app.route('/copy_note', methods=['POST'])
def copy_note():
    generated_note = request.form.get('generated_note')
    pyperclip.copy(generated_note)
    return 'Note copied to clipboard.'

# Render the index.html template
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        generate_note()
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
