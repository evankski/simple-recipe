from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

recipes = []
@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/add_recipe')
def add_recipe():
    return render_template('add.html', recipes=recipes)

@app.route('/add', methods=['POST'])
def add():
    recipe = request.form['recipe']
    ingredients = request.form['ingredients']
    directions = request.form['directions']
    recipes.append({"recipe": recipe, "ingredients": ingredients, "directions": directions})
    return redirect(url_for("index"))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    recipe = recipes[index]
    if request.method == 'POST':
        recipe['recipe'] = request.form['recipe']
        recipe['ingredients'] = request.form['ingredients']
        recipe['directions'] = request.form['directions']
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', recipe=recipe, index=index)

@app.route('/delete/<int:index>')
def delete(index):
    del recipes[index]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)