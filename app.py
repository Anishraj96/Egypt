from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the comma-separated names from the form
        names_input = request.form.get('names')
        # Split the input into a list of names
        names = [name.strip() for name in names_input.split(',') if name.strip()]
        
        # Check if there are at least 11 names
        if len(names) < 11:
            return "Please provide at least 11 names."
        
        # Randomly select 11 names
        selected_names = random.sample(names, 11)
        
        # Randomly select Captain and Vice-Captain
        captain = random.choice(selected_names)
        vice_captain = random.choice([name for name in selected_names if name != captain])
        
        return render_template('result.html', selected_names=selected_names, captain=captain, vice_captain=vice_captain)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)