from flask import Flask, render_template
import data_processing
import data_analysis

app = Flask(__name__)

from flask import render_template

@app.route('/some_route')
def some_route():
    # Your data processing logic here...
    return render_template('floor_counts.html', floor_counts=floor_counts_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary')
def show_summary():
    file_path = "data/kc_house_data.csv"
    df = data_processing.load_data(file_path)
    df = data_processing.clean_data(df)
    summary_statistics = data_processing.get_summary_statistics(df)
    return render_template('summary.html', summary_statistics=summary_statistics)

@app.route('/floor_counts')
def show_floor_counts():
    file_path = "data/kc_house_data.csv"
    df = data_processing.load_data(file_path)
    df = data_processing.clean_data(df)
    floor_value_counts = data_processing.get_floor_value_counts(df)
    return render_template('floor_counts.html', floor_value_counts=floor_value_counts)

if __name__ == '__main__':
    app.run(debug=True)
