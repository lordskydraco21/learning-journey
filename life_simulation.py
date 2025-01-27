from animated_art_generator import AnimatedArtGenerator, ColorPalette
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageEnhance
import math
import random
import numpy as np
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    size: float
    energy: float
    age: float
    species: int
    
class LifeSimulation(AnimatedArtGenerator):
    def __init__(self, width=800, height=600):
        super().__init__(width, height)
        self.particles = []
        self.num_particles = 100
        self.num_species = 3
        self.initialize_particles()
        
        # Simulation parameters
        self.max_speed = 4.0
        self.vision_radius = 50
        self.separation_radius = 20
        self.cohesion_strength = 0.03
        self.alignment_strength = 0.05
        self.separation_strength = 0.08
        self.energy_transfer_rate = 0.1
        self.growth_rate = 0.02
        self.max_age = 300
        
    def initialize_particles(self):
        """Initialize particles with random positions and velocities"""
        for _ in range(self.num_particles):
            particle = Particle(
                x=random.uniform(0, self.width),
                y=random.uniform(0, self.height),
                vx=random.uniform(-2, 2),
                vy=random.uniform(-2, 2),
                size=random.uniform(3, 6),
                energy=random.uniform(0.5, 1.0),
                age=0,
                species=random.randint(0, self.num_species - 1)
            )
            self.particles.append(particle)
    
    def apply_forces(self, particle: Particle, neighbors: List[Particle]):
        """Apply flocking and interaction forces to particle"""
        if not neighbors:
            return
        
        # Initialize force components
        cohesion_x = cohesion_y = 0
        align_x = align_y = 0
        separate_x = separate_y = 0
        
        # Calculate center of mass and average velocity
        com_x = com_y = 0
        avg_vx = avg_vy = 0
        separation_count = 0
        
        for neighbor in neighbors:
            dx = neighbor.x - particle.x
            dy = neighbor.y - particle.y
            distance = math.sqrt(dx*dx + dy*dy)
            
            # Cohesion
            com_x += neighbor.x
            com_y += neighbor.y
            
            # Alignment
            avg_vx += neighbor.vx
            avg_vy += neighbor.vy
            
            # Separation
            if distance < self.separation_radius:
                separate_x -= dx / (distance + 1e-6)
                separate_y -= dy / (distance + 1e-6)
                separation_count += 1
        
        # Normalize and apply forces
        num_neighbors = len(neighbors)
        
        # Cohesion
        com_x /= num_neighbors
        com_y /= num_neighbors
        cohesion_x = (com_x - particle.x) * self.cohesion_strength
        cohesion_y = (com_y - particle.y) * self.cohesion_strength
        
        # Alignment
        avg_vx /= num_neighbors
        avg_vy /= num_neighbors
        align_x = (avg_vx - particle.vx) * self.alignment_strength
        align_y = (avg_vy - particle.vy) * self.alignment_strength
        
        # Separation
        if separation_count > 0:
            separate_x = separate_x / separation_count * self.separation_strength
            separate_y = separate_y / separation_count * self.separation_strength
        
        # Update velocity
        particle.vx += cohesion_x + align_x + separate_x
        particle.vy += cohesion_y + align_y + separate_y
        
        # Limit speed
        speed = math.sqrt(particle.vx*particle.vx + particle.vy*particle.vy)
        if speed > self.max_speed:
            particle.vx = (particle.vx / speed) * self.max_speed
            particle.vy = (particle.vy / speed) * self.max_speed
    
    def update_particle(self, particle: Particle):
        """Update particle state"""
        # Find neighbors
        neighbors = []
        for other in self.particles:
            if other != particle:
                dx = other.x - particle.x
                dy = other.y - particle.y
                distance = math.sqrt(dx*dx + dy*dy)
                if distance < self.vision_radius:
                    neighbors.append(other)
        
        # Apply forces
        self.apply_forces(particle, neighbors)
        
        # Update position
        particle.x += particle.vx
        particle.y += particle.vy
        
        # Wrap around screen
        particle.x = particle.x % self.width
        particle.y = particle.y % self.height
        
        # Update energy and age
        particle.energy = max(0, min(1, particle.energy - 0.001 + 
                                   self.growth_rate * len(neighbors)))
        particle.age += 1
        
        # Adjust size based on energy
        particle.size = 3 + 3 * particle.energy
        
        # Reproduction
        if particle.energy > 0.8 and random.random() < 0.05:
            self.particles.append(Particle(
                x=particle.x + random.uniform(-10, 10),
                y=particle.y + random.uniform(-10, 10),
                vx=particle.vx + random.uniform(-1, 1),
                vy=particle.vy + random.uniform(-1, 1),
                size=particle.size * 0.5,
                energy=particle.energy * 0.5,
                age=0,
                species=particle.species
            ))
            particle.energy *= 0.5
    
    def draw_particle(self, draw: ImageDraw, particle: Particle, frame_num: int):
        """Draw a single particle"""
        # Calculate color based on species and energy
        hue = 0.2 + (particle.species * 0.3)  # Different hue for each species
        saturation = 0.7 + 0.3 * particle.energy
        value = 0.5 + 0.5 * particle.energy
        
        # Add subtle color variation
        hue += 0.05 * math.sin(frame_num * 0.1 + particle.age * 0.05)
        
        color = tuple(map(int, self.palette.hsv_to_rgb(hue, saturation, value)))
        
        # Draw particle with glow effect
        for i in range(3):
            glow_size = particle.size * (1 + i * 0.5)
            alpha = int(255 * (1 - i * 0.3) * particle.energy)
            glow_color = (*color, alpha)
            
            draw.ellipse([particle.x - glow_size, particle.y - glow_size,
                         particle.x + glow_size, particle.y + glow_size],
                        fill=glow_color)
        
        # Draw connections to nearby particles
        for other in self.particles:
            if other != particle:
                dx = other.x - particle.x
                dy = other.y - particle.y
                distance = math.sqrt(dx*dx + dy*dy)
                if distance < self.vision_radius:
                    # Draw connection with alpha based on distance
                    alpha = int(255 * (1 - distance/self.vision_radius) * 0.3)
                    connection_color = (*color, alpha)
                    draw.line([particle.x, particle.y, other.x, other.y],
                             fill=connection_color, width=1)
    
    def create_frame(self, frame_num: int, total_frames: int):
        """Create a frame of the life simulation"""
        # Create base image with alpha channel
        image = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Update and draw particles
        for particle in self.particles[:]:
            self.update_particle(particle)
            self.draw_particle(draw, particle, frame_num)
            
            # Remove old particles
            if particle.age > self.max_age or particle.energy <= 0:
                self.particles.remove(particle)
        
        # Add new particles if population is low
        while len(self.particles) < self.num_particles // 2:
            self.initialize_particles()
        
        # Apply post-processing effects
        # Add bloom
        bloom = image.filter(ImageFilter.GaussianBlur(3))
        image = Image.blend(image, bloom, 0.3)
        
        # Add subtle color aberration
        r, g, b, a = image.split()
        r = ImageChops.offset(r, 2, 0)
        b = ImageChops.offset(b, -2, 0)
        image = Image.merge('RGBA', (r, g, b, a))
        
        return image.convert('RGB')

def main():
    print("Life Simulation Generator")
    print("========================")
    
    # Create and generate life simulation
    generator = LifeSimulation(800, 600)
    generator.generate_animation("life_simulation", frames=180, duration=150)
    
    print("\nAnimation generated successfully!")
    print("Check the 'animated_art' directory for the output file.")

if __name__ == "__main__":
    main()
