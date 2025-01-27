import turtle
import random
from PIL import Image, ImageDraw
import os
from datetime import datetime
import math

class TurtleArtGenerator:
    def __init__(self, width=800, height=800):
        self.width = width
        self.height = height
        self.output_dir = 'turtle_art'
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Create PIL Image and Draw objects
        self.image = Image.new('RGB', (width, height), 'black')
        self.draw = ImageDraw.Draw(self.image)
        self.current_pos = (width//2, height//2)
        self.angle = 0  # 0 degrees is pointing right
        
    def save_image(self, name):
        """Save the image"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.output_dir, filename)
        self.image.save(filepath)
        print(f"Saved: {filepath}")
        return filepath
    
    def clear_screen(self):
        """Clear the image"""
        self.image = Image.new('RGB', (self.width, self.height), 'black')
        self.draw = ImageDraw.Draw(self.image)
        self.current_pos = (self.width//2, self.height//2)
        self.angle = 0
    
    def random_color(self):
        """Generate a random RGB color"""
        return (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
    
    def move_forward(self, distance, draw_line=True, color=None):
        """Move forward and optionally draw a line"""
        # Calculate new position
        rad_angle = math.radians(self.angle)
        new_x = self.current_pos[0] + distance * math.cos(rad_angle)
        new_y = self.current_pos[1] + distance * math.sin(rad_angle)
        new_pos = (int(new_x), int(new_y))
        
        # Draw line if requested
        if draw_line:
            self.draw.line([self.current_pos, new_pos], fill=color or self.random_color(), width=2)
        
        self.current_pos = new_pos
    
    def right(self, angle):
        """Turn right by given angle"""
        self.angle = (self.angle + angle) % 360
    
    def left(self, angle):
        """Turn left by given angle"""
        self.angle = (self.angle - angle) % 360
    
    def spiral_pattern(self, size=300, angle=91):
        """Generate a colorful spiral pattern"""
        print("Generating spiral pattern...")
        self.clear_screen()
        
        for i in range(size):
            color = self.random_color()
            self.move_forward(i * 2, color=color)
            self.right(angle)
        
        return self.save_image("spiral")
    
    def star_burst(self, lines=50, size=300):
        """Generate a star burst pattern"""
        print("Generating star burst pattern...")
        self.clear_screen()
        
        for _ in range(lines):
            color = self.random_color()
            self.move_forward(size, color=color)
            self.move_forward(-size, color=color)
            self.right(360/lines)
        
        return self.save_image("star_burst")
    
    def geometric_pattern(self, size=200, iterations=36):
        """Generate a geometric pattern"""
        print("Generating geometric pattern...")
        self.clear_screen()
        
        for _ in range(iterations):
            color = self.random_color()
            for _ in range(4):
                self.move_forward(size, color=color)
                self.right(90)
            self.right(360/iterations)
        
        return self.save_image("geometric")
    
    def snowflake(self, size=100, iterations=6):
        """Generate a snowflake pattern"""
        print("Generating snowflake pattern...")
        self.clear_screen()
        
        def koch_curve(size, depth):
            if depth == 0:
                self.move_forward(size, color=self.random_color())
            else:
                size /= 3
                koch_curve(size, depth-1)
                self.left(60)
                koch_curve(size, depth-1)
                self.right(120)
                koch_curve(size, depth-1)
                self.left(60)
                koch_curve(size, depth-1)
        
        for _ in range(3):
            koch_curve(size, iterations)
            self.right(120)
        
        return self.save_image("snowflake")
    
    def circular_pattern(self, radius=200, points=36):
        """Generate a circular pattern with connecting lines"""
        print("Generating circular pattern...")
        self.clear_screen()
        
        # Calculate points on circle
        circle_points = []
        for i in range(points):
            angle = math.radians(i * 360 / points)
            x = self.width//2 + radius * math.cos(angle)
            y = self.height//2 + radius * math.sin(angle)
            circle_points.append((int(x), int(y)))
        
        # Connect each point to every other point
        for i in range(points):
            for j in range(i + 1, points):
                self.draw.line([circle_points[i], circle_points[j]], 
                             fill=self.random_color(), width=1)
        
        return self.save_image("circular_pattern")

def main():
    # Create art generator
    generator = TurtleArtGenerator(800, 800)
    
    print("Turtle Art Generator")
    print("===================")
    print(f"Output directory: {generator.output_dir}")
    print("Generating patterns...")
    
    # Generate different patterns
    generator.spiral_pattern(300, 91)
    generator.star_burst(50, 300)
    generator.geometric_pattern(200, 36)
    generator.snowflake(200, 4)
    generator.circular_pattern(300, 36)
    
    print("\nAll patterns generated successfully!")
    print("Check the 'turtle_art' directory for the output files.")

if __name__ == "__main__":
    main()
