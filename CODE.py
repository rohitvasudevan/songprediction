import billboard
import datetime
from datetime import timedelta
import csv
from xmllib import newline

filename = 'billaboard_hot_100.csv'

def ex1():
    date_var = datetime.datetime.strptime('1991-10-29', "%Y-%m-%d");
    with open(filename, 'wb') as billaboard_fp:
        csv_writter = csv.writer(billaboard_fp)
        csv_writter.writerow(['title', 'artist', 'peakPos', 'lastPos', 'weeks', 'rank', 'date'])
    
    while date_var < datetime.datetime.now():
        date_var = date_var + timedelta(days=7)
        ex2(str(date_var.date()))

def ex2(chart_date):
    print chart_date
    chart = billboard.ChartData('hot-100',date=chart_date)
    
    for song in chart:
        with open(filename, 'ab') as billaboard_fp:
            csv_writter = csv.writer(billaboard_fp)
            row = [song.title, song.artist, song.peakPos, song.lastPos, song.weeks, song.rank, chart.date]
            row = [item if isinstance(item, int) else item.encode('utf-8') for item in row]
            csv_writter.writerow(row)
    
if __name__ == '__main__':
    ex1()
