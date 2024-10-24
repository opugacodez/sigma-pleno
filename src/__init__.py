from flask import Flask, render_template, request, redirect, url_for, flash
from src.config.database import db
from src.config.env import env
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from src.service.product_service import ProductService
from src.service.cash_flow_service import CashFlowService
from pprint import pprint


def create_app():
    """Inicializa e configura o aplicativo Flask."""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
    app.config['JWT_SECRET_KEY'] = env('SECRET_KEY')
    app.config['SECRET_KEY'] = env('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    JWTManager(app)
    Migrate(app, db)

    register_blueprints(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/products', methods=['GET'])
    def product_list():
        products = ProductService.list_products()[0]
        cashflows = CashFlowService.retrieve_cash_flows()
        return render_template('product_list.html', products=products, cashflows=cashflows)

    @app.route('/products/new', methods=['GET', 'POST'])
    def add_product():
        if request.method == 'POST':
            product_data = {
                'name': request.form['name'],
                'description': request.form['description'],
                'quantity': request.form['quantity'],
                'price': request.form['price']
            }
            ProductService.add_product(product_data)
            flash('Produto adicionado com sucesso!')
            return redirect(url_for('product_list'))
        return render_template('product_form.html')

    @app.route('/products/<int:id>/delete', methods=['POST'])
    def delete_product(id):
        ProductService.remove_product(id)
        flash('Produto removido com sucesso!')
        return redirect(url_for('product_list'))

    @app.route('/products/<int:id>/edit', methods=['GET', 'POST'])
    def edit_product(id):
        product = ProductService.get_product(id)[0]
        cashflow = CashFlowService.retrieve_cash_flow_by_product_id(id)
        pprint(cashflow)
        if request.method == 'POST':
            ProductService.modify_product(id, request.form)
            flash('Produto atualizado com sucesso!')
            return redirect(url_for('product_list'))
        return render_template('product_form.html', product=product, cashflow=cashflow)

    return app


def register_blueprints(app: Flask):
    """Registra todos os blueprints da aplicação."""
    from src.controller.product_controller import main as product_blueprint
    app.register_blueprint(product_blueprint)
    from src.controller.user_controller import user_blueprint
    app.register_blueprint(user_blueprint)
