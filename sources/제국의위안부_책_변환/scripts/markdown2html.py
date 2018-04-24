from flask import render_template
import flask
import markdown2
import os

app = flask.Flask('my app')
dir_path = 'data/markdown/'

def create_home_address():
    return '<a href="index.html">목록으로</a>'
def create_prev_address(file_path, file_name):
    return '<a href="{0}">이전으로 - {1}</a>'.format(file_path[:-2]+'html', file_name[6:-3].replace('-', ' '))
def create_next_address(file_path, file_name):
    return '<a href="{0}">다음으로 - {1}</a>'.format(file_path[:-2]+'html', file_name[6:-3].replace('-', ' '))

if __name__ == '__main__':
    file_names = os.listdir(dir_path)
    file_count = len(file_names)
    file_zip = list(zip(range(file_count),file_names))

    for idx, file_name in file_zip:
        with open(dir_path+file_name, 'r', encoding='utf-8') as f:
            text = f.read()
            md = markdown2.markdown(text)
        with app.app_context():
            prev_link = create_prev_address(file_zip[idx-1][1], file_zip[idx-1][1]) if idx>0 else ''
            next_link = create_next_address(file_zip[idx+1][1], file_zip[idx+1][1]) if idx<file_count-1 else ''
            rendered = render_template('book.html',
                                       title=file_name[:-2] if file_name.find('index')<0 else '제국의 위안부 E-Book', 
                                       home_link=create_home_address() if file_name.find('index')<0 else '',
                                       prev_link=prev_link if file_name.find('index')<0 else '',
                                       next_link=next_link if file_name.find('index')<0 else '',
                                       content=md)
        with open('../../books/제국의위안부/'+file_name[:-2]+'html', 'w', encoding='utf-8') as f:
            f.write(rendered)
            print(file_name+' -> '+file_name[:-2]+'html')
    #     break