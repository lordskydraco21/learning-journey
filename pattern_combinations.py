from animated_art_generator import AnimatedArtGenerator, ColorPalette
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageEnhance
import math
import numpy as np

class PatternCombinations(AnimatedArtGenerator):
    def __init__(self, width=500, height=500):
        super().__init__(width, height)
    
    def create_vortex_layer(self, frame_num, total_frames):
        """Create a spinning vortex effect"""
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        center_x, center_y = self.width/2, self.height/2
        phase = frame_num * (2 * math.pi / total_frames)
        
        # Create multiple spiral arms
        for arm in range(6):
            points = []
            arm_phase = phase + (arm * math.pi / 3)
            
            for t in range(0, 360 * 3, 5):
                angle = math.radians(t) + arm_phase
                radius = 5 + t/5 * (1 + 0.3 * math.sin(phase * 2))
                x = center_x + radius * math.cos(angle)
                y = center_y + radius * math.sin(angle)
                points.append((x, y))
            
            # Draw spiral arm
            if len(points) > 1:
                for i in range(len(points)-1):
                    progress = i / len(points)
                    hue = (progress + frame_num/total_frames) % 1.0
                    color = self.palette.hsv_to_rgb(*self.palette.neon(hue))
                    draw.line(points[i:i+2], fill=color, width=2)
        
        return image
    
    def create_matrix_layer(self, frame_num, total_frames):
        """Create a matrix-like digital rain effect"""
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        # Digital rain parameters
        column_width = 20
        num_columns = self.width // column_width
        phase = frame_num * (2 * math.pi / total_frames)
        
        for col in range(num_columns):
            # Calculate column properties
            x = col * column_width
            offset = math.sin(phase + col * 0.5) * 50
            length = 100 + 50 * math.sin(phase * 2 + col * 0.3)
            
            # Draw digital rain
            for i in range(int(length)):
                y = (offset + i * 5) % self.height
                progress = i / length
                hue = (0.3 + 0.1 * math.sin(phase + col * 0.2)) % 1.0
                color = self.palette.hsv_to_rgb(hue, 1.0, progress)
                
                size = int(3 * (1 - progress))
                if size > 0:
                    draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
        
        return image
    
    def create_particle_field(self, frame_num, total_frames):
        """Create a flowing particle field effect"""
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        phase = frame_num * (2 * math.pi / total_frames)
        num_particles = 200
        
        for i in range(num_particles):
            # Particle position based on time
            t = i * (2 * math.pi / num_particles)
            radius = 100 + 50 * math.sin(phase + t)
            angle = t + phase
            
            x = self.width/2 + radius * math.cos(angle)
            y = self.height/2 + radius * math.sin(angle)
            
            # Calculate particle properties
            size = 2 + math.sin(phase * 2 + t) * 2
            hue = (t/(2*math.pi) + frame_num/total_frames) % 1.0
            color = self.palette.hsv_to_rgb(*self.palette.neon(hue))
            
            # Draw particle with trail
            for j in range(5):
                trail_x = x - j * math.cos(angle) * 5
                trail_y = y - j * math.sin(angle) * 5
                alpha = 1.0 - j/5
                trail_color = tuple(int(c * alpha) for c in color)
                
                draw.ellipse([trail_x-size, trail_y-size, 
                            trail_x+size, trail_y+size], 
                           fill=trail_color)
        
        return image
    
    def create_geometric_weave(self, frame_num, total_frames):
        """Create an interweaving geometric pattern"""
        image = Image.new('RGB', (self.width, self.height), 'black')
        draw = ImageDraw.Draw(image)
        
        phase = frame_num * (2 * math.pi / total_frames)
        num_lines = 12
        
        # Create weaving lines
        for i in range(num_lines):
            points = []
            angle_offset = i * (2 * math.pi / num_lines)
            
            # Generate points for each line
            for t in range(0, self.width, 5):
                x = t
                y = self.height/2 + math.sin(t/50 + phase + angle_offset) * 100
                points.append((x, y))
            
            # Draw line with color gradient
            if len(points) > 1:
                for j in range(len(points)-1):
                    progress = j / len(points)
                    hue = (progress + i/num_lines + frame_num/total_frames) % 1.0
                    color = self.palette.hsv_to_rgb(*self.palette.neon(hue))
                    draw.line(points[j:j+2], fill=color, width=2)
        
        return image

    def apply_effects(self, image, frame_num, total_frames):
        """Apply post-processing effects"""
        # Add bloom effect
        bloom = image.filter(ImageFilter.GaussianBlur(3))
        image = Image.blend(image, bloom, 0.3)
        
        # Add chromatic aberration
        r, g, b = image.split()
        r = ImageChops.offset(r, 2, 0)
        b = ImageChops.offset(b, -2, 0)
        image = Image.merge('RGB', (r, g, b))
        
        # Adjust contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.2)
        
        return image

    def create_frame(self, frame_num, total_frames):
        """Create a frame combining multiple patterns"""
        # Create base layers
        vortex = self.create_vortex_layer(frame_num, total_frames)
        matrix = self.create_matrix_layer(frame_num, total_frames)
        particles = self.create_particle_field(frame_num, total_frames)
        weave = self.create_geometric_weave(frame_num, total_frames)
        
        # Blend layers with different modes and phases
        phase = frame_num * (2 * math.pi / total_frames)
        
        # Start with vortex
        result = vortex
        
        # Blend matrix with screen mode
        alpha = abs(math.sin(phase))
        matrix_blend = ImageChops.screen(result, matrix)
        result = Image.blend(result, matrix_blend, alpha * 0.6)
        
        # Blend particles with add mode
        alpha = abs(math.sin(phase + math.pi/3))
        particle_blend = ImageChops.add(result, particles)
        result = Image.blend(result, particle_blend, alpha * 0.5)
        
        # Blend weave with screen mode
        alpha = abs(math.sin(phase + math.pi/2))
        weave_blend = ImageChops.screen(result, weave)
        result = Image.blend(result, weave_blend, alpha * 0.7)
        
        # Apply post-processing effects
        result = self.apply_effects(result, frame_num, total_frames)
        
        return result

def main():
    print("Pattern Combinations Generator")
    print("=============================")
    
    # Create and generate pattern combinations
    generator = PatternCombinations(500, 500)
    generator.generate_animation("pattern_combo", frames=60, duration=50)
    
    print("\nAnimation generated successfully!")
    print("Check the 'animated_art' directory for the output file.")

if __name__ == "__main__":
    main()
