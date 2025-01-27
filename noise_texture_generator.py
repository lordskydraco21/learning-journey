import numpy as np
from PIL import Image
import os
from datetime import datetime

class NoiseTextureGenerator:
    def __init__(self, width=512, height=512):
        self.width = width
        self.height = height
        self.output_dir = 'generated_textures'
        os.makedirs(self.output_dir, exist_ok=True)

    def save_texture(self, texture_array, name):
        """Save the texture array as an image"""
        # Normalize to 0-255 range
        normalized = ((texture_array - texture_array.min()) * (255.0 / (texture_array.max() - texture_array.min()))).astype(np.uint8)
        img = Image.fromarray(normalized)
        
        # Add timestamp to filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.output_dir, filename)
        
        img.save(filepath)
        print(f"Saved: {filepath}")
        return filepath

    def perlin_noise(self, scale=100.0, octaves=6):
        """Generate Perlin-like noise using multiple octaves of simplex noise"""
        print("Generating Perlin-like noise texture...")
        
        texture = np.zeros((self.height, self.width))
        frequency = 1.0
        amplitude = 1.0
        max_value = 0.0
        
        for _ in range(octaves):
            noise_layer = np.random.rand(
                int(self.height/frequency), 
                int(self.width/frequency)
            )
            # Resize to full size
            noise_layer = Image.fromarray((noise_layer * 255).astype(np.uint8))
            noise_layer = noise_layer.resize((self.width, self.height), Image.Resampling.BILINEAR)
            noise_layer = np.array(noise_layer) / 255.0
            
            texture += noise_layer * amplitude
            max_value += amplitude
            amplitude *= 0.5
            frequency *= 2
        
        texture /= max_value
        return self.save_texture(texture, "perlin_noise")

    def fractal_noise(self, scale=100.0, octaves=6):
        """Generate fractal noise using multiple layers"""
        print("Generating fractal noise texture...")
        
        texture = np.zeros((self.height, self.width))
        frequency = 1.0
        amplitude = 1.0
        max_value = 0.0
        
        for _ in range(octaves):
            noise_layer = np.random.rand(
                int(self.height/frequency), 
                int(self.width/frequency)
            )
            # Apply turbulence
            noise_layer = np.abs(noise_layer * 2 - 1)
            
            # Resize to full size
            noise_layer = Image.fromarray((noise_layer * 255).astype(np.uint8))
            noise_layer = noise_layer.resize((self.width, self.height), Image.Resampling.BILINEAR)
            noise_layer = np.array(noise_layer) / 255.0
            
            texture += noise_layer * amplitude
            max_value += amplitude
            amplitude *= 0.5
            frequency *= 2
        
        texture /= max_value
        return self.save_texture(texture, "fractal_noise")

    def marble_texture(self, scale=100.0, turbulence=5.0):
        """Generate marble-like texture"""
        print("Generating marble texture...")
        
        # Create base gradient
        x = np.linspace(0, 1, self.width)
        gradient = np.tile(x, (self.height, 1))
        
        # Add turbulence
        noise = np.random.rand(self.height, self.width)
        turbulence_layer = Image.fromarray((noise * 255).astype(np.uint8))
        turbulence_layer = turbulence_layer.resize((self.width, self.height), Image.Resampling.BILINEAR)
        turbulence = np.array(turbulence_layer) / 255.0
        
        # Combine gradient with turbulence
        texture = gradient + turbulence * turbulence
        texture = np.sin(texture * np.pi * 2)
        
        return self.save_texture(texture, "marble_texture")

    def wood_texture(self, scale=50.0, rings=20):
        """Generate wood-like texture"""
        print("Generating wood texture...")
        
        # Create radial gradient
        x = np.linspace(-1, 1, self.width)
        y = np.linspace(-1, 1, self.height)
        xx, yy = np.meshgrid(x, y)
        radius = np.sqrt(xx**2 + yy**2)
        
        # Create ring pattern
        texture = np.sin(radius * rings)
        
        # Add noise for wood grain
        noise = np.random.rand(self.height, self.width)
        wood_grain = Image.fromarray((noise * 255).astype(np.uint8))
        wood_grain = wood_grain.resize((self.width, self.height), Image.Resampling.BILINEAR)
        wood_grain = np.array(wood_grain) / 255.0
        
        texture = texture * 0.7 + wood_grain * 0.3
        
        return self.save_texture(texture, "wood_texture")

    def cloud_texture(self, scale=100.0, octaves=6):
        """Generate cloud-like texture"""
        print("Generating cloud texture...")
        
        texture = np.zeros((self.height, self.width))
        frequency = 1.0
        amplitude = 1.0
        max_value = 0.0
        
        for _ in range(octaves):
            # Generate noise at current frequency
            noise_layer = np.random.rand(
                int(self.height/frequency), 
                int(self.width/frequency)
            )
            
            # Smooth the noise
            noise_layer = Image.fromarray((noise_layer * 255).astype(np.uint8))
            noise_layer = noise_layer.resize((self.width, self.height), Image.Resampling.BILINEAR)
            noise_layer = np.array(noise_layer) / 255.0
            
            # Add to texture
            texture += noise_layer * amplitude
            max_value += amplitude
            amplitude *= 0.5
            frequency *= 2E
        
        # Normalize and apply cloud-like transformation
        texture /= max_value
        texture = 1 - np.exp(-texture * 3)  # Create cloud-like appearance
        
        return self.save_texture(texture, "cloud_texture")

    def cellular_texture(self, scale=50.0, points=20):
        """Generate cellular/Worley noise texture"""
        print("Generating cellular texture...")
        
        # Generate random points
        points = np.random.rand(points, 2) * [self.width, self.height]
        
        # Create distance field
        x = np.arange(self.width)
        y = np.arange(self.height)
        xx, yy = np.meshgrid(x, y)
        texture = np.ones((self.height, self.width)) * np.inf
        
        # Calculate minimum distance to points
        for p in points:
            distance = np.sqrt((xx - p[0])**2 + (yy - p[1])**2)
            texture = np.minimum(texture, distance)
        
        # Normalize distances
        texture /= np.max(texture)
        
        return self.save_texture(texture, "cellular_texture")

    def gradient_noise(self, scale=50.0):
        """Generate gradient noise texture"""
        print("Generating gradient noise texture...")
        
        # Create base noise
        noise = np.random.rand(
            int(self.height/scale), 
            int(self.width/scale)
        )
        
        # Create gradients
        angles = np.random.rand(
            int(self.height/scale), 
            int(self.width/scale)
        ) * 2 * np.pi
        
        gradients_x = np.cos(angles)
        gradients_y = np.sin(angles)
        
        # Resize to full size
        noise = Image.fromarray((noise * 255).astype(np.uint8))
        noise = noise.resize((self.width, self.height), Image.Resampling.BILINEAR)
        texture = np.array(noise) / 255.0
        
        # Add gradient influence
        gradients_x = Image.fromarray(((gradients_x + 1) * 127.5).astype(np.uint8))
        gradients_y = Image.fromarray(((gradients_y + 1) * 127.5).astype(np.uint8))
        
        gradients_x = gradients_x.resize((self.width, self.height), Image.Resampling.BILINEAR)
        gradients_y = gradients_y.resize((self.width, self.height), Image.Resampling.BILINEAR)
        
        gradients_x = (np.array(gradients_x) / 127.5 - 1)
        gradients_y = (np.array(gradients_y) / 127.5 - 1)
        
        texture = texture + (gradients_x + gradients_y) * 0.5
        
        return self.save_texture(texture, "gradient_noise")

def main():
    # Create texture generator
    generator = NoiseTextureGenerator(512, 512)
    
    print("Noise Texture Generator")
    print("======================")
    print(f"Output directory: {generator.output_dir}")
    print("Generating textures...")
    
    # Generate different types of textures
    generator.perlin_noise(scale=100.0, octaves=6)
    generator.fractal_noise(scale=100.0, octaves=8)
    generator.marble_texture(scale=100.0, turbulence=5.0)
    generator.wood_texture(scale=50.0, rings=20)
    generator.cloud_texture(scale=100.0, octaves=6)
    generator.cellular_texture(scale=50.0, points=20)
    generator.gradient_noise(scale=50.0)
    
    print("\nAll textures generated successfully!")
    print("Check the 'generated_textures' directory for the output files.")

if __name__ == "__main__":
    main()
