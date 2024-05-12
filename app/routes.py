from flask import render_template
from flask import flash
from flask import redirect
from app import obj
from app.forms import LoginForm

## Need these variable to manipulate the database
from app.models import User, Post
from app import db


@obj.route("/")
@obj.route("/index.html")
def hello():
    company_name_update = "foober"
    a_list_of_names = ['Eric', 'Alex', 'Amer', 'Daniel']
    a_list_dictionary_of_author_book_names = [
        {
            'author': 'John',
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': 'Susan',
            'body': 'The Avengers movie was so cool!'
        }
    ]


    return render_template('home.html', company=company_name_update, title="THIS IS \
                           DIFFERENT", names=a_list_of_names,
                           author_list=a_list_dictionary_of_author_book_names)

@obj.route("/login", methods=["GET", "POST"])
# tells flask to execute login() when user goes to /login path of the webpage
def login():
    current_form = LoginForm()
    if current_form.validate_on_submit():
        flash(f'GOOD username {current_form.username.data}')
        flash(f'GOOD password {current_form.password.data}')

        ########### Add a row to the database (User table) #########
        # u = User(username=current_form.username.data, email='test@email.com')
        # db.session.add(u)
        # db.session.commit()


        ################ Get/search a row to the database (User table) #############
        ### Look up all users
        # users = User.query.all()
        # for u in users:
        #     # shows on the terminal
        #     print(u.id, u.username, u.email)

        #     # show on html?
        #     #flash()

        ### Look up users by id
        # print(User.query.get(2))

        ### Look up users by attribute (returns a list)
        # search = User.query.filter_by(username='carlos')
        # for s in search:
        #     print(s)



        ############### Delete a row in the database  (User table) #########

        # user_to_del = User.query.get(1)
        # db.session.delete(user_to_del)
        # db.session.commit()

        ################################################################
        # How to add to User and Post?

        # step 1: create user
        #u = User(username=current_form.username.data, email='test@email.com')
        #db.session.add(u)
        #db.session.commit()

        # step 2: create post
        # p = Post(body='hello this is my post', author=User.query.get(1))
        # db.session.add(p)
        # db.session.commit()

        # ## step 3: search for post
        # # search user or get user id
        # u = User.query.get(1)
        # # to show post
        # print(u.posts())


        return redirect('/')

    # this is only going to show in the console
    #print(f'This is the username {current_form.username.data}')
    return render_template("login.html", form=current_form)
