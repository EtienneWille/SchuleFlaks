from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if(request.method=='GET'):
        all_comments = ""

        try:
            f = open('comments.txt', 'r')
            all_comments = f.readlines()
            f.close()
        except:
            f = open('comments.txt', 'x')
            f.close()

        return render_template('comments.html', comments=all_comments)
    elif(request.method=='POST'):
        f = open("comments.txt", 'a')
        f.writelines(request.form['comment'] + "\n")
        f.close()
        return redirect('/comments')

app.run(debug=True, port=9876)
