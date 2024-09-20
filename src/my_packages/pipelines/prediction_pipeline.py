import numpy as np
import matplotlib.pyplot as plt

class HeartGradient:
    def __init__(self, gradient_colors=None):
        """Initialize the HeartGradient class with customizable gradient colors."""
        if gradient_colors is None:
            # Default gradient colors if not provided
            self.gradient_colors = ['#ff5e5e', '#ff4d4d', '#ff3333', '#ff1a1a', '#ff0000']
        else:
            self.gradient_colors = gradient_colors

    def draw_heart(self, ax, x, y, size, color):
        """Function to draw a heart using parametric equations."""
        t = np.linspace(0, 2 * np.pi, 100)
        x_heart = 16 * np.sin(t)**3
        y_heart = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
        
        ax.fill(x_heart * size + x, y_heart * size + y, color=color, zorder=2)

    def create_heart_gradient(self):
        """Method to create a gradient heart design with varying sizes and colors."""
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_axis_off()

        # Adjust size scaling based on the number of colors
        sizes = np.linspace(1, 0.5, len(self.gradient_colors))

        # Draw hearts with decreasing sizes and gradient colors
        for i, (size, color) in enumerate(zip(sizes, self.gradient_colors)):
            self.draw_heart(ax, 0, 0, size, color)
        
        plt.show()

# Example usage
heart_gradient = HeartGradient()
heart_gradient.create_heart_gradient()