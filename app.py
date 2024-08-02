import pandas as pd

df = pd.read_csv('uploads\Housing.csv')

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    
    if not file:
        return "No file uploaded", 400
    
    df = pd.read_csv(file)
    
    # Perform analysis
    head = df.head().to_html(classes='table table-striped')
    description = df.describe().to_html(classes='table table-striped')
    missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html(classes='table table-striped')
    data_types = df.dtypes.to_frame(name='Data Type').to_html(classes='table table-striped')
    #correlation_matrix = df.corr().to_html(classes='table table-striped')
    unique_values = df.nunique().to_frame(name='Unique Values').to_html(classes='table table-striped')

    return render_template('results.html', head=head, description=description, 
                           missing_values=missing_values, data_types=data_types, 
                            unique_values=unique_values)

if __name__ == '__main__':
    app.run(debug=True)
