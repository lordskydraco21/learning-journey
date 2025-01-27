from animated_art_generator import AnimatedArtGenerator, ColorPalette
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageEnhance
import math
import random
import numpy as np

class NeuralPattern(AnimatedArtGenerator):
    def __init__(self, width=800, height=600):
        super().__init__(width, height)
        # Define styles before creating network
        self.connection_styles = ['wave', 'spiral', 'bezier']
        self.activations = {}  # Track node activations
        self.pulses = []  # Track pulses traveling along connections
        # Create network after initializing variables
        self.nodes = self._create_network()
        self.connections = self._create_connections()

    def _create_network(self):
        """Create neural network structure"""
        nodes = []
        layers = 5
        nodes_per_layer = [4, 6, 8, 6, 4]
        
        # Create nodes for each layer
        for layer in range(layers):
            layer_nodes = nodes_per_layer[layer]
            for i in range(layer_nodes):
                x = 100 + (self.width - 200) * (layer / (layers - 1))
                spacing = (self.height - 100) / (layer_nodes + 1)
                y = 50 + spacing * (i + 1)
                nodes.append({
                    'pos': (x, y),
                    'layer': layer,
                    'index': i,
                    'size': 10
                })
        return nodes
    
    def _create_connections(self):
        """Create connections between nodes"""
        connections = []
        # Connect each node to nodes in next layer
        for node in self.nodes:
            if node['layer'] < len(set(n['layer'] for n in self.nodes)) - 1:
                next_layer_nodes = [n for n in self.nodes if n['layer'] == node['layer'] + 1]
                for next_node in next_layer_nodes:
                    # Add some randomness to connections
                    if random.random() < 0.7:
                        connections.append({
                            'start': node,
                            'end': next_node,
                            'weight': random.random(),
                            'pulses': [],  # Store pulses for this connection
                            'style': random.choice(self.connection_styles)  # Random style for each connection
                        })
        return connections
    
    def _sigmoid(self, x):
        """Sigmoid activation function"""
        return 1 / (1 + math.exp(-x))
    
    def _update_activations(self, frame_num, total_frames):
        """Update node activations"""
        phase = frame_num * (2 * math.pi / total_frames)
        
        # Update input layer with sine waves
        for node in self.nodes:
            if node['layer'] == 0:
                # Input layer activation
                freq = 1 + node['index'] * 0.5
                self.activations[(node['layer'], node['index'])] = abs(math.sin(phase * freq))
            else:
                # Hidden and output layers
                incoming = [conn for conn in self.connections if conn['end'] == node]
                if incoming:
                    weighted_sum = sum(conn['weight'] * self.activations.get((conn['start']['layer'], conn['start']['index']), 0)
                                    for conn in incoming)
                    self.activations[(node['layer'], node['index'])] = self._sigmoid(weighted_sum)
    
    def _update_pulses(self, frame_num, total_frames):
        """Update pulse positions along connections"""
        # Create new pulses
        if frame_num % 10 == 0:  # Create pulses periodically
            for conn in self.connections:
                start_activation = self.activations.get((conn['start']['layer'], conn['start']['index']), 0)
                if start_activation > 0.5 and random.random() < 0.3:  # Randomly create pulses for active nodes
                    conn['pulses'].append({
                        'position': 0.0,  # Position along the connection (0 to 1)
                        'strength': start_activation,  # Pulse intensity
                        'speed': 0.05 + random.random() * 0.05  # Random speed variation
                    })
        
        # Update existing pulses
        for conn in self.connections:
            # Update each pulse
            conn['pulses'] = [pulse for pulse in conn['pulses'] if pulse['position'] <= 1.0]
            for pulse in conn['pulses']:
                pulse['position'] += pulse['speed']
                pulse['strength'] *= 0.95  # Fade out gradually

    def _get_connection_points(self, start, end, style, frame_num, total_frames):
        """Generate points for different connection styles"""
        points = []
        steps = 50
        phase = frame_num * (2 * math.pi / total_frames)
        
        if style == 'wave':
            # Create a wavy line with dynamic amplitude
            dx = end[0] - start[0]
            dy = end[1] - start[1]
            distance = math.sqrt(dx*dx + dy*dy)
            angle = math.atan2(dy, dx)
            
            for i in range(steps + 1):
                t = i / steps
                # Add sine wave perpendicular to connection
                wave_amp = 20 * math.sin(phase) * math.sin(t * math.pi)
                x = start[0] + dx * t
                y = start[1] + dy * t + wave_amp * math.cos(angle)
                points.append((x, y))
                
        elif style == 'spiral':
            # Create a spiral pattern
            cx = (start[0] + end[0]) / 2
            cy = (start[1] + end[1]) / 2
            radius = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2) / 4
            
            for i in range(steps + 1):
                t = i / steps
                # Spiral with dynamic radius
                spiral_radius = radius * (1 - t) * (0.5 + 0.5 * math.sin(phase))
                angle = t * 4 * math.pi + phase
                x = start[0] + (end[0] - start[0]) * t + spiral_radius * math.cos(angle)
                y = start[1] + (end[1] - start[1]) * t + spiral_radius * math.sin(angle)
                points.append((x, y))
                
        else:  # bezier
            # Enhanced bezier curve with multiple control points
            cx1 = start[0] + (end[0] - start[0]) * 0.25
            cy1 = start[1] + (end[1] - start[1]) * 0.25 + 30 * math.sin(phase)
            cx2 = start[0] + (end[0] - start[0]) * 0.75
            cy2 = start[1] + (end[1] - start[1]) * 0.75 - 30 * math.sin(phase)
            
            for i in range(steps + 1):
                t = i / steps
                # Cubic bezier curve
                x = (1-t)**3 * start[0] + \
                    3*(1-t)**2 * t * cx1 + \
                    3*(1-t) * t**2 * cx2 + \
                    t**3 * end[0]
                y = (1-t)**3 * start[1] + \
                    3*(1-t)**2 * t * cy1 + \
                    3*(1-t) * t**2 * cy2 + \
                    t**3 * end[1]
                points.append((x, y))
        
        return points

    def draw_connection(self, draw, start, end, weight, activation, color, pulses, style, frame_num, total_frames):
        """Draw a connection with animation and pulses"""
        # Get points for the connection style
        points = self._get_connection_points(start, end, style, frame_num, total_frames)
        
        # Draw base connection with gradient
        if len(points) > 1:
            for i in range(len(points) - 1):
                progress = i / (len(points) - 1)
                alpha = int(255 * (0.2 + 0.3 * activation * (1 - progress)))
                conn_color = tuple(list(color[:3]) + [alpha])
                draw.line(points[i:i+2], fill=conn_color, width=2)
        
        # Draw pulses with style-specific effects
        for pulse in pulses:
            if 0 <= pulse['position'] <= 1:
                idx = int(pulse['position'] * (len(points) - 1))
                if idx < len(points) - 1:
                    x, y = points[idx]
                    
                    # Style-specific pulse effects
                    pulse_size = 4 + 4 * pulse['strength']
                    if style == 'wave':
                        pulse_size *= 1.5  # Larger pulses for wave style
                    elif style == 'spiral':
                        pulse_size *= (1 + 0.5 * math.sin(frame_num * 0.2))  # Pulsating size
                    
                    pulse_alpha = int(255 * pulse['strength'])
                    pulse_color = tuple(list(map(lambda x: int(x * 1.5), color[:3])) + [pulse_alpha])
                    
                    # Draw pulse glow with style variations
                    for size in range(int(pulse_size), 0, -1):
                        glow_alpha = int(pulse_alpha * (size / pulse_size))
                        glow_color = tuple(list(color[:3]) + [glow_alpha])
                        
                        if style == 'spiral':
                            # Rotating square pulses for spiral
                            angle = frame_num * 0.1
                            pulse_points = [
                                (x + size * math.cos(angle + i * math.pi/2),
                                 y + size * math.sin(angle + i * math.pi/2))
                                for i in range(4)
                            ]
                            draw.polygon(pulse_points, fill=glow_color)
                        else:
                            # Circle pulses for other styles
                            draw.ellipse([x - size, y - size, x + size, y + size],
                                       fill=glow_color)

    def create_frame(self, frame_num, total_frames):
        """Create a frame of the neural network animation"""
        # Create base image with alpha channel
        image = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        
        # Update activations and pulses
        self._update_activations(frame_num, total_frames)
        self._update_pulses(frame_num, total_frames)
        
        # Draw connections with pulses
        for conn in self.connections:
            start_pos = conn['start']['pos']
            end_pos = conn['end']['pos']
            activation = self.activations.get((conn['end']['layer'], conn['end']['index']), 0)
            
            # Get color based on activation
            hue = 0.6 + 0.1 * activation  # Blue to purple
            color = tuple(list(map(int, self.palette.hsv_to_rgb(hue, 0.8, 1))) + [255])
            
            self.draw_connection(draw, start_pos, end_pos, conn['weight'],
                               activation, color, conn['pulses'], conn['style'],
                               frame_num, total_frames)
        
        # Draw nodes
        for node in self.nodes:
            x, y = node['pos']
            size = node['size']
            activation = self.activations.get((node['layer'], node['index']), 0)
            
            # Node glow based on activation
            for i in range(3):
                glow_size = size * (1 + i * 0.5)
                alpha = int(100 * activation / (i + 1))
                glow_color = (100, 200, 255, alpha)
                draw.ellipse([x - glow_size, y - glow_size,
                            x + glow_size, y + glow_size],
                           fill=glow_color)
            
            # Main node
            node_color = tuple(map(int, self.palette.hsv_to_rgb(0.6, 0.8, 0.5 + 0.5 * activation)))
            draw.ellipse([x - size, y - size, x + size, y + size],
                        fill=node_color)
        
        # Apply post-processing effects
        # Add bloom
        bloom = image.filter(ImageFilter.GaussianBlur(3))
        image = Image.blend(image, bloom, 0.3)
        
        # Convert to RGB for final output
        return image.convert('RGB')

def main():
    print("Neural Network Pattern Generator")
    print("===============================")
    
    # Create and generate neural network animation
    generator = NeuralPattern(800, 600)
    generator.generate_animation("neural_network", frames=120, duration=100)
    
    print("\nAnimation generated successfully!")
    print("Check the 'animated_art' directory for the output file.")

if __name__ == "__main__":
    main()
