from flask import Flask, render_template, url_for, request, jsonify, session

from board import create_board, is_mine

app = Flask(__name__)
app.secret_key = b'_5#y2L"dF4Q8z\n\xec]/'


@app.route('/')
def main():
    return render_template("index.html")


@app.route("/play/<level>")
def play(level=3):
    url_for("static", filename="jquery-3.5.0.min.js")
    board = create_board(int(level))
    session["board"] = board
    return render_template("play.html", largo=range(len(board[0])), alto=range(len(board)))


@app.route('/check', methods=['POST'])
def check():
    x = int(request.form["x"])
    y = int(request.form["y"])

    pc = is_mine(session["board"], x, y)
    if isinstance(pc, bool):
        return jsonify({"mina": pc})
    else:
        return jsonify(pc)


if __name__ == '__main__':
    app.run()
