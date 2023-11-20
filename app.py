from flask import Flask, render_template
import data_processing
import data_analysis

app = Flask(__name__)

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

@app.route('/show_average_price_per_unit')
def show_average_price_per_unit():
    file_path = "data/kc_house_data.csv"
    df = data_processing.load_data(file_path)
    df = data_processing.clean_data(df)
    avg_price_per_unit, plot_filename = data_analysis.analyze_avg_price_per_unit_over_time(df)
    return render_template('average_price_per_unit.html', avg_price_per_unit=avg_price_per_unit, plot_filename=plot_filename)

@app.route('/deal_volume_over_time/<criteria>')
def deal_volume_over_time(criteria):
    # Load the dataset
    file_path = "data/kc_house_data.csv"
    df = data_processing.load_data(file_path)

    # Clean the data
    df = data_processing.clean_data(df)

    # Analyze deal volume based on the specified criteria (bedrooms)
    data_analysis.analyze_deal_volume_over_time_by_criteria(df, criteria)

    return render_template('deal_volume_over_time.html', criteria=criteria)


if __name__ == '__main__':
    app.run(debug=True)
