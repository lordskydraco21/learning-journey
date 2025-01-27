from animated_art_generator import AnimatedArtGenerator, ColorPalette
from PIL import Image, ImageDraw, ImageFilter, ImageChops
import math
import numpy as np

class ComplexPatterns(AnimatedArtGenerator):
    def __init__(self, width=500, height=500):
        super().__init__(width, height)
        
    def create_kaleidoscope_layer(self, frame_num, total_frames, segments=8):
        """Create a kaleidoscope effect"""
        base = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(base)
        
        # Create a segment
        segment_angle = 360 / segments
        phase = frame_num * (2 * math.pi / total_frames)
        
        # Draw patterns in one segment
        points = []
        for i in range(20):
            angle = i * (segment_angle / 20) + phase
            radius = 100 + 50 * math.sin(phase * 2 + i * 0.5)
            x = self.width/2 + radius * math.cos(math.radians(angle))
            y = self.height/2 + radius * math.sin(math.radians(angle))
            points.append((x, y))
            
            if len(points) > 1:
                hue = (i/20 + frame_num/total_frames) % 1.0
                color = self.palette.hsv_to_rgb(*self.palette.neon(hue))
                draw.line(points[-2:], fill=color, width=2)
        
        # Rotate and copy the segment
        base_segment = base.crop((self.width/2, 0, self.width, self.height/2))
        for i in range(segments):
            rotated = base_segment.rotate(i * segment_angle)
            base.paste(rotated, (int(self.width/2), int(self.height/2)))
            base.paste(rotated.transpose(Image.FLIP_LEFT_RIGHT), 
                      (int(self.width/2), int(self.height/2)))
        
        return base
    
    def create_fractal_layer(self, frame_num, total_frames):
        """Create a fractal spiral effect"""
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        def draw_fractal(x, y, size, angle, depth):
            if depth <= 0 or size < 5:
                return
            
            hue = (depth/6 + frame_num/total_frames) % 1.0
            color = self.palette.hsv_to_rgb(*self.palette.neon(hue))
            
            # Calculate end point
            end_x = x + size * math.cos(angle)
            end_y = y + size * math.sin(angle)
            
            # Draw line
            draw.line([(x, y), (end_x, end_y)], fill=color, width=2)
            
            # Recursive calls with rotation
            phase = frame_num * (2 * math.pi / total_frames)
            rotation = math.sin(phase) * 30  # Oscillating rotation
            
            draw_fractal(end_x, end_y, size * 0.7, angle + math.radians(rotation), depth - 1)
            draw_fractal(end_x, end_y, size * 0.7, angle - math.radians(rotation), depth - 1)
        
        # Start the fractal from center
        center_x, center_y = self.width/2, self.height/2
        start_angle = frame_num * (2 * math.pi / total_frames)
        
        for i in range(4):  # Draw 4 main branches
            angle = start_angle + i * (math.pi/2)
            draw_fractal(center_x, center_y, 100, angle, 6)
        
        return image
    
    def create_wave_layer(self, frame_num, total_frames):
        """Create an interference wave pattern"""
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        phase = frame_num * (2 * math.pi / total_frames)
        wave_centers = [
            (self.width/2, self.height/2),
            (0, 0),
            (self.width, 0),
            (0, self.height),
            (self.width, self.height)
        ]
        
        for x in range(0, self.width, 4):
            for y in range(0, self.height, 4):
                # Calculate interference from multiple wave sources
                value = 0
                for cx, cy in wave_centers:
                    dist = math.sqrt((x - cx)**2 + (y - cy)**2)
                    value += math.sin(dist/20 - phase)
                
                # Map value to color
                intensity = (value + len(wave_centers)) / (2 * len(wave_centers))
                hue = (intensity + frame_num/total_frames) % 1.0
                color = self.palette.hsv_to_rgb(*self.palette.pastel(hue))
                
                draw.point((x, y), fill=color)
        
        return image
    
    def blend_images(self, images, frame_num, total_frames):
        """Blend multiple image layers with different blend modes"""
        # Start with the first image
        result = images[0]
        
        # Blend subsequent images
        for img in images[1:]:
            # Create masks for smooth transitions
            phase = frame_num * (2 * math.pi / total_frames)
            alpha = int(128 + 64 * math.sin(phase))  # Oscillating opacity
            
            # Apply different blend modes
            screen = ImageChops.screen(result, img)
            multiply = ImageChops.multiply(result, img)
            
            # Blend between different modes based on frame
            if frame_num % 2 == 0:
                result = Image.blend(result, screen, alpha/255)
            else:
                result = Image.blend(result, multiply, alpha/255)
        
        # Add final glow effect
        glow = result.filter(ImageFilter.GaussianBlur(3))
        result = Image.blend(result, glow, 0.3)
        
        return result
    
    def create_frame(self, frame_num, total_frames):
        """Create a complex frame combining multiple effects"""
        # Create individual layers
        kaleidoscope = self.create_kaleidoscope_layer(frame_num, total_frames)
        fractal = self.create_fractal_layer(frame_num, total_frames)
        wave = self.create_wave_layer(frame_num, total_frames)
        
        # Blend layers together
        return self.blend_images([kaleidoscope, fractal, wave], 
                               frame_num, total_frames)

def main():
    print("Complex Pattern Generator")
    print("========================")
    
    # Create and generate complex pattern animation
    generator = ComplexPatterns(500, 500)
    generator.generate_animation("complex_pattern", frames=60, duration=50)
    
    print("\nAnimation generated successfully!")
    print("Check the 'animated_art' directory for the output file.")

if __name__ == "__main__":
    main()
