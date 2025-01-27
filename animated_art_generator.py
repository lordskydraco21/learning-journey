import numpy as np
from PIL import Image, ImageDraw
import os
from datetime import datetime
import math
import colorsys

class ColorPalette:
    def __init__(self):
        self.golden_ratio = 0.618033988749895
        
    def complementary(self, hue):
        """Get complementary color hue"""
        return (hue + 0.5) % 1.0
    
    def triadic(self, hue):
        """Get triadic color hues"""
        return [(hue + i/3.0) % 1.0 for i in range(3)]
    
    def analogous(self, hue, num_colors=3, spread=0.05):
        """Get analogous color hues"""
        return [(hue + i*spread) % 1.0 for i in range(num_colors)]
    
    def rainbow_gradient(self, pos):
        """Get a rainbow gradient color at position (0-1)"""
        return pos % 1.0
    
    def golden_ratio_color(self, base_hue, index):
        """Get a color using golden ratio progression"""
        return (base_hue + self.golden_ratio * index) % 1.0
    
    def pastel(self, hue, pastel_factor=0.3):
        """Convert a hue to a pastel color"""
        return (hue, 0.4 + pastel_factor, 1.0)
    
    def neon(self, hue, neon_factor=0.2):
        """Convert a hue to a neon color"""
        return (hue, 0.8 + neon_factor, 1.0)
    
    def gradient_between(self, hue1, hue2, pos):
        """Get a color between two hues"""
        # Handle wrap-around
        if abs(hue2 - hue1) > 0.5:
            if hue2 > hue1:
                hue1 += 1.0
            else:
                hue2 += 1.0
        hue = (hue1 + (hue2 - hue1) * pos) % 1.0
        return hue
    
    def hsv_to_rgb(self, h, s, v):
        """Convert HSV to RGB color"""
        rgb = colorsys.hsv_to_rgb(h, s, v)
        return tuple(int(x * 255) for x in rgb)

class AnimatedArtGenerator:
    def __init__(self, width=500, height=500):
        self.width = width
        self.height = height
        self.output_dir = 'animated_art'
        os.makedirs(self.output_dir, exist_ok=True)
        self.palette = ColorPalette()
        
    def create_frame(self, frame_num, total_frames):
        """Create a new frame (to be implemented by subclasses)"""
        pass
    
    def generate_animation(self, name, frames=60, duration=100):
        """Generate and save an animated GIF"""
        print(f"Generating {name} animation...")
        
        images = []
        for i in range(frames):
            print(f"Generating frame {i+1}/{frames}")
            frame = self.create_frame(i, frames)
            images.append(frame)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.gif"
        filepath = os.path.join(self.output_dir, filename)
        
        images[0].save(
            filepath,
            save_all=True,
            append_images=images[1:],
            duration=duration,
            loop=0
        )
        print(f"Saved: {filepath}")
        return filepath

class SpinningMandala(AnimatedArtGenerator):
    def create_frame(self, frame_num, total_frames):
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        base_hue = frame_num / total_frames
        rotation = frame_num * (360 / total_frames)
        
        num_triangles = 12
        for i in range(num_triangles):
            angle = (i * 360 / num_triangles + rotation) % 360
            
            # Use triadic colors for each third of the mandala
            triad_index = (i * 3) // num_triangles
            triad_colors = self.palette.triadic(base_hue)
            hue = self.palette.gradient_between(
                triad_colors[triad_index % 3],
                triad_colors[(triad_index + 1) % 3],
                (i % (num_triangles//3)) / (num_triangles//3)
            )
            
            # Add neon effect for more vibrancy
            color = self.palette.hsv_to_rgb(*self.palette.neon(hue))
            
            # Calculate triangle points
            radius = self.width * 0.4
            points = []
            for j in range(3):
                point_angle = angle + j * 120
                x = self.width/2 + radius * math.cos(math.radians(point_angle))
                y = self.height/2 + radius * math.sin(math.radians(point_angle))
                points.append((x, y))
            
            draw.polygon(points, fill=color)
        
        return image

class ExpandingSpiral(AnimatedArtGenerator):
    def create_frame(self, frame_num, total_frames):
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        start_angle = (frame_num * 10) % 360
        expansion = frame_num / total_frames
        base_hue = frame_num / total_frames
        
        center_x, center_y = self.width/2, self.height/2
        points = []
        
        for i in range(720):
            angle = math.radians(i/2 + start_angle)
            radius = (i/5 + 50) * (0.5 + expansion)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.append((x, y))
            
            if len(points) > 1:
                # Create a rainbow wave effect
                pos = (i/720 + frame_num/total_frames) % 1.0
                hue = self.palette.rainbow_gradient(pos)
                
                # Add golden ratio progression for more interesting colors
                hue = self.palette.golden_ratio_color(hue, i)
                
                # Alternate between neon and pastel
                if i % 2 == 0:
                    color = self.palette.hsv_to_rgb(*self.palette.neon(hue))
                else:
                    color = self.palette.hsv_to_rgb(*self.palette.pastel(hue))
                
                draw.line(points[-2:], fill=color, width=2)
        
        return image

class PulsatingCircles(AnimatedArtGenerator):
    def create_frame(self, frame_num, total_frames):
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        phase = frame_num * (2 * math.pi / total_frames)
        base_hue = frame_num / total_frames
        
        # Get analogous colors for a harmonious palette
        num_circles = 15
        colors = self.palette.analogous(base_hue, num_circles, 0.3)
        
        for i in range(num_circles):
            # Pulsating effect
            base_radius = (i + 1) * (self.width / (2 * num_circles))
            pulse = math.sin(phase + i * math.pi/8)
            radius = base_radius * (0.8 + 0.2 * pulse)
            
            # Color with alternating neon and pastel
            hue = colors[i]
            if i % 2 == 0:
                color = self.palette.hsv_to_rgb(*self.palette.neon(hue, 0.3))
            else:
                color = self.palette.hsv_to_rgb(*self.palette.pastel(hue, 0.4))
            
            # Draw circle
            x0 = self.width/2 - radius
            y0 = self.height/2 - radius
            x1 = self.width/2 + radius
            y1 = self.height/2 + radius
            draw.ellipse([x0, y0, x1, y1], outline=color, width=2)
        
        return image

class MorphingStars(AnimatedArtGenerator):
    def create_frame(self, frame_num, total_frames):
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        phase = frame_num * (2 * math.pi / total_frames)
        points = 5 + int(2.5 * (math.sin(phase) + 1))
        base_hue = frame_num / total_frames
        
        # Get complementary colors for contrast
        hue1 = base_hue
        hue2 = self.palette.complementary(base_hue)
        
        radius_outer = self.width * 0.4
        radius_inner = radius_outer * 0.4
        center_x, center_y = self.width/2, self.height/2
        
        star_points = []
        for i in range(points * 2):
            angle = i * math.pi / points + phase
            radius = radius_outer if i % 2 == 0 else radius_inner
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            star_points.append((x, y))
        
        star_points.append(star_points[0])  # Close the path
        
        # Draw with gradient between complementary colors
        for i in range(len(star_points)-1):
            pos = i / (len(star_points)-1)
            hue = self.palette.gradient_between(hue1, hue2, pos)
            
            # Add neon effect for more vibrancy
            color = self.palette.hsv_to_rgb(*self.palette.neon(hue))
            
            draw.line([star_points[i], star_points[i+1]], fill=color, width=2)
        
        return image

def main():
    print("Animated Art Generator")
    print("=====================")
    
    # Generate animations with enhanced colors
    mandala = SpinningMandala(500, 500)
    mandala.generate_animation("spinning_mandala", frames=60, duration=50)
    
    spiral = ExpandingSpiral(500, 500)
    spiral.generate_animation("expanding_spiral", frames=60, duration=50)
    
    circles = PulsatingCircles(500, 500)
    circles.generate_animation("pulsating_circles", frames=60, duration=50)
    
    stars = MorphingStars(500, 500)
    stars.generate_animation("morphing_stars", frames=60, duration=50)
    
    print("\nAll animations generated successfully!")
    print("Check the 'animated_art' directory for the output files.")

if __name__ == "__main__":
    main()
