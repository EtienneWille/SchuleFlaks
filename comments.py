from flask import Blueprint, render_template, request, redirect

comments_blueprint = Blueprint('comments', __name__)


@comments_blueprint.route('/comments', methods=['POST', 'GET'])
def comments():
    if (request.method == 'GET'):
        all_comments = ""

        try:
            f = open('comments.txt', 'r')
            all_comments = f.readlines()
            f.close()
        except:
            f = open('comments.txt', 'x')
            f.close()

        return render_template('comments.html', comments=all_comments)
    elif (request.method == 'POST'):
        f = open("comments.txt", 'a')
        f.writelines(request.form['comment'] + "\n")
        f.close()
        return redirect('/comments')