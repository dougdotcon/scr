from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from models import User
from flask_otp import OTP
from flask_otp import OTPSecret
from flask import Flask

app = Flask(__name__)

bp = Blueprint('auth', __name__, url_prefix='/auth')

login_manager = LoginManager()

@bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return 'Invalid username or password'
    login_user(user)
    return redirect(url_for('index'))

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

app.config['OTP_SECRETS'] = {
    'admin': OTPSecret('admin_secret_key'),
    'user': OTPSecret('user_secret_key')
}

otp = OTP(app)

@bp.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if request.method == 'POST':
        otp_value = request.form['otp']
        if otp.verify(current_user.id, 'admin', otp_value):
            return redirect(url_for('admin_dashboard'))
        else:
            return 'Código de verificação inválido'
    return render_template('verify_otp.html')