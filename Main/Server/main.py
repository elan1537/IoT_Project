from flask import *
from Raspberry.sendReceived import Transceiver

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/request")
def request():
    transfer = Transceiver()
    transfer.__send__("GETSTRING")
    transfer.__read__()

    return redirect(url_for('main'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

