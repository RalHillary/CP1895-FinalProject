from flask import Flask, render_template, request, redirect, url_for
from db import (
    create_database,
    read_all_players,
    add_player,
    delete_player,
    update_player,
)
from forms import AddPlayerForm, UpdatePlayerForm

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure key for WTForms CSRF protection

# Ensure the database is set up
create_database()

@app.route("/")
def index():
    """Display the homepage."""
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"], endpoint="add_player")
def add():
    """Display and process the add player form."""
    form = AddPlayerForm()
    if form.validate_on_submit():
        player_data = (
            form.first_name.data,
            form.last_name.data,
            form.position.data,
            form.bat_order.data,
            form.at_bats.data or 0,
            form.hits.data or 0,
        )
        add_player(player_data)
        return redirect(url_for("players"))
    return render_template("add_player.html", form=form)

@app.route("/players")
def players():
    """Display the player list."""
    all_players = read_all_players()
    return render_template("player_list.html", players=all_players)

@app.route("/update/<int:player_id>", methods=["GET", "POST"])
def update(player_id):
    """Display and process the update player form."""
    form = UpdatePlayerForm()
    if request.method == "GET":
        all_players = read_all_players()
        player = next((p for p in all_players if p[0] == player_id), None)
        if player:
            form.first_name.data = player[1]
            form.last_name.data = player[2]
            form.position.data = player[3]
            form.bat_order.data = player[4]
            form.at_bats.data = player[5]
            form.hits.data = player[6]
        else:
            return redirect(url_for("players"))

    if form.validate_on_submit():
        updated_data = {
            "first_name": form.first_name.data,
            "last_name": form.last_name.data,
            "position": form.position.data,
            "bat_order": form.bat_order.data,
            "at_bats": form.at_bats.data,
            "hits": form.hits.data,
        }
        update_player(player_id, updated_data)
        return redirect(url_for("players"))

    return render_template("update_player.html", form=form)

@app.route("/delete/<int:player_id>")
def delete(player_id):
    """Handle player deletion."""
    delete_player(player_id)
    return redirect(url_for("players"))

if __name__ == "__main__":
    app.run(debug=True)
