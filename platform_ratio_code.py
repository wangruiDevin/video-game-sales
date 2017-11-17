import pandas
import pygal
import numpy
from project_module import project as project

def main():
    """main controller"""
    data_frame = pandas.read_csv('Video-Game-Sales/videoGameSales.csv')
    create_chart(data_frame)

def create_chart(data_frame):
    """for create chart"""
    df_convert = project.platform_convert_df(data_frame)
    data = numpy.array(df_convert.groupby('Platform', as_index=False).count()[['Platform', 'Rank']]).tolist()
    chart = pygal.Pie()
    for i in data:
        chart.add(i[0], i[1])
    chart.render_to_file('platform_ratio.svg')
main()
