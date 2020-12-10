from flask import Flask, render_template
from control import Control

# Create flask app and control
app = Flask(__name__)
control = Control()

@app.route('/')
def index():
    switch = control.read_switch()
    return render_template('index.html', switch=switch) 


@app.route("/load/<int:state>", methods=['POST'])
def load(state):
    # Check if the led state is 0 (off) or 1 (on) and set the LED accordingly.
    if state == 0:
        control.set_load(False)
    elif state == 1:
        control.set_load(True)
    else:
        return ('Unknown load state', 400)
    return ('', 204)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='9009')
