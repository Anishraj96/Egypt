from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the list of names from the form
        names = request.form.get('names').split(',')
        names = [name.strip() for name in names if name.strip()]

        # Select 11 random names
        selected_11 = random.sample(names, min(11, len(names)))

        # Select Captain and Vice-Captain
        captain = random.choice(selected_11)
        vc_candidates = [name for name in selected_11 if name != captain]
        vice_captain = random.choice(vc_candidates)

        return render_template('result.html', selected_11=selected_11, captain=captain, vice_captain=vice_captain)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)