from flask import Flask, render_template, request
import data_processing
import data_analysis

app = Flask(__name__)

# Load the dataset
file_path = "data/house_sales_dataset.csv"
df = data_processing.load_data(file_path)

@app.route('/')
def index():
    return render_template('index.html')

# Add routes for different analyses (e.g., volume of deals, average price per unit)

if __name__ == '__main__':
    app.run(debug=True)
