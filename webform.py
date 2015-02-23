"""
simples web-based control
from http://www.themagpi.com/issue/issue-9/article/the-python-pit-drive-your-raspberry-pi-with-a-mobile-phone/
do not use this in a production system!
"""
import web
from web import form

# Define the pages (index) for the site
urls = ('/', 'index')
render = web.template.render('templates')

app = web.application(urls, globals())

# Define the buttons that should be shown on the form
my_form = form.Form(
 form.Button("btn", id="btnR", value="OFF", html="Red", class_="btnRed"),
 form.Button("btn", id="btnG", value="ON", html="Green", class_="btnGreen"),
)

# define what happens when the index page is called
class index:
    # GET us used when the page is first requested
    def GET(self):
        form = my_form()
        return render.index(form, "Python Remote Control")

    # POST is called when a web form is submitted
    def POST(self):
        # get the data submitted from the web form
        userData = web.input()

        # Determine which action user submitted
        if userData.btn == "OFF":
            data = "0" #Rgb
        elif userData.btn == "ON":
            data = "1" # rGb
        else:
            print("I didn't understand your input")

        # write the file
        with open('/tmp/blah.txt', 'w') as f:
            f.write(data)
       
        # reload the web form ready for the next user input
        raise web.seeother('/')

if __name__ == '__main__':
    app.run()