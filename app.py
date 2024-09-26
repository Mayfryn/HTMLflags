from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель для збереження ручок
class Pen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=True)
    collection = db.Column(db.String(100), nullable=True)
    pen_type = db.Column(db.String(50), nullable=True)
    color = db.Column(db.String(50), nullable=True)
    refill_type = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=True)
    description = db.Column(db.Text, nullable=True)
    my_rating = db.Column(db.Integer, nullable=True)
    visitor_rating = db.Column(db.Float, nullable=True)

# Модель для збереження ножів
class Knife(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=True)
    collection = db.Column(db.String(100), nullable=True)
    blade_length = db.Column(db.String(50), nullable=True)
    color = db.Column(db.String(50), nullable=True)
    metal_type = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=True)
    description = db.Column(db.Text, nullable=True)
    my_rating = db.Column(db.Integer, nullable=True)
    visitor_rating = db.Column(db.Float, nullable=True)

# Створення бази даних
with app.app_context():
    db.create_all()

# Головна сторінка
@app.route('/')
def index():
    pens = Pen.query.all()  # Вибірка всіх ручок з бази даних
    knives = Knife.query.all()  # Вибірка всіх ножів з бази даних
    return render_template('index.html', pens=pens, knives=knives)

# Додати ручку
@app.route('/add_pen', methods=['POST'])
def add_pen():
    brand = request.form.get('brand', '')
    collection = request.form.get('collection', '')
    pen_type = request.form.get('pen_type', '')
    color = request.form.get('color', '')
    refill_type = request.form.get('refill_type', '')
    price = request.form.get('price', 0.0)  # За замовчуванням 0.0 для ціни
    description = request.form.get('description', '')
    my_rating = request.form.get('my_rating', None)  # None для рейтингу, якщо не передано
    
    new_pen = Pen(brand=brand, collection=collection, pen_type=pen_type, color=color,
                  refill_type=refill_type, price=price, description=description, my_rating=my_rating)
    
    db.session.add(new_pen)
    db.session.commit()
    
    return redirect(url_for('index'))

# Додати ніж
@app.route('/add_knife', methods=['POST'])
def add_knife():
    brand = request.form.get('brand', '')
    collection = request.form.get('collection', '')
    blade_length = request.form.get('blade_length', '')
    color = request.form.get('color', '')
    metal_type = request.form.get('metal_type', '')
    price = request.form.get('price', 0.0)
    description = request.form.get('description', '')
    my_rating = request.form.get('my_rating', None)
    
    new_knife = Knife(brand=brand, collection=collection, blade_length=blade_length, color=color,
                      metal_type=metal_type, price=price, description=description, my_rating=my_rating)
    
    db.session.add(new_knife)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)