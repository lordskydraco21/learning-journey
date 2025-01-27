import bpy
import random
from mathutils import Vector

class NoiseTextureGenerator:
    def __init__(self):
        self.noise_types = {
            'clouds': self.create_clouds,
            'marble': self.create_marble,
            'wood': self.create_wood,
            'voronoi': self.create_voronoi,
            'musgrave': self.create_musgrave,
            'wave': self.create_wave
        }

    def clear_scene(self):
        """Clear existing materials and textures"""
        # Remove existing materials
        for material in bpy.data.materials:
            bpy.data.materials.remove(material)
        
        # Remove existing textures
        for texture in bpy.data.textures:
            bpy.data.textures.remove(texture)

    def create_base_material(self, name):
        """Create a new material with nodes"""
        material = bpy.data.materials.new(name=name)
        material.use_nodes = True
        nodes = material.node_tree.nodes
        nodes.clear()
        return material, nodes

    def create_basic_node_setup(self, material_name):
        """Create basic node setup for material"""
        material, nodes = self.create_base_material(material_name)
        
        # Create nodes
        output = nodes.new('ShaderNodeOutputMaterial')
        principled = nodes.new('ShaderNodeBsdfPrincipled')
        texture_coord = nodes.new('ShaderNodeTexCoord')
        mapping = nodes.new('ShaderNodeMapping')
        noise_texture = nodes.new('ShaderNodeTexNoise')
        color_ramp = nodes.new('ShaderNodeValToRGB')
        
        # Position nodes
        output.location = Vector((300, 0))
        principled.location = Vector((0, 0))
        texture_coord.location = Vector((-800, 0))
        mapping.location = Vector((-600, 0))
        noise_texture.location = Vector((-400, 0))
        color_ramp.location = Vector((-200, 0))
        
        # Link nodes
        links = material.node_tree.links
        links.new(texture_coord.outputs['Generated'], mapping.inputs['Vector'])
        links.new(mapping.outputs['Vector'], noise_texture.inputs['Vector'])
        links.new(noise_texture.outputs['Fac'], color_ramp.inputs['Fac'])
        links.new(color_ramp.outputs['Color'], principled.inputs['Base Color'])
        links.new(principled.outputs['BSDF'], output.inputs['Surface'])
        
        return material, nodes, color_ramp, noise_texture, mapping

    def create_clouds(self, name="CloudNoise"):
        """Create cloud-like noise texture"""
        material, nodes, color_ramp, noise_texture, mapping = self.create_basic_node_setup(name)
        
        # Configure noise
        noise_texture.inputs['Scale'].default_value = 5.0
        noise_texture.inputs['Detail'].default_value = 8.0
        noise_texture.inputs['Roughness'].default_value = 0.7
        
        # Configure color ramp
        color_ramp.color_ramp.elements[0].position = 0.3
        color_ramp.color_ramp.elements[0].color = (0.1, 0.1, 0.1, 1)
        color_ramp.color_ramp.elements[1].position = 0.7
        color_ramp.color_ramp.elements[1].color = (1, 1, 1, 1)
        
        return material

    def create_marble(self, name="MarbleNoise"):
        """Create marble-like noise texture"""
        material, nodes, color_ramp, noise_texture, mapping = self.create_basic_node_setup(name)
        
        # Add wave texture for marble effect
        wave_texture = nodes.new('ShaderNodeTexWave')
        wave_texture.location = Vector((-400, -200))
        
        # Configure wave texture
        wave_texture.wave_type = 'RINGS'
        wave_texture.inputs['Scale'].default_value = 2.0
        wave_texture.inputs['Distortion'].default_value = 2.0
        wave_texture.inputs['Detail'].default_value = 2.0
        
        # Mix noise and wave
        mix_node = nodes.new('ShaderNodeMixRGB')
        mix_node.location = Vector((-200, -100))
        mix_node.blend_type = 'OVERLAY'
        
        # Link nodes
        links = material.node_tree.links
        links.new(wave_texture.outputs['Color'], mix_node.inputs[1])
        links.new(noise_texture.outputs['Color'], mix_node.inputs[2])
        links.new(mix_node.outputs['Color'], color_ramp.inputs['Fac'])
        
        return material

    def create_wood(self, name="WoodNoise"):
        """Create wood-like noise texture"""
        material, nodes, color_ramp, noise_texture, mapping = self.create_basic_node_setup(name)
        
        # Configure mapping for wood grain
        mapping.inputs['Scale'].default_value[0] = 20.0
        mapping.inputs['Scale'].default_value[1] = 1.0
        mapping.inputs['Scale'].default_value[2] = 1.0
        
        # Configure noise
        noise_texture.inputs['Scale'].default_value = 15.0
        noise_texture.inputs['Detail'].default_value = 10.0
        noise_texture.inputs['Roughness'].default_value = 0.8
        
        # Configure color ramp for wood colors
        color_ramp.color_ramp.elements[0].position = 0.4
        color_ramp.color_ramp.elements[0].color = (0.4, 0.2, 0.1, 1)
        color_ramp.color_ramp.elements[1].position = 0.6
        color_ramp.color_ramp.elements[1].color = (0.6, 0.3, 0.1, 1)
        
        return material

    def create_voronoi(self, name="VoronoiNoise"):
        """Create cellular/voronoi noise texture"""
        material, nodes = self.create_base_material(name)
        
        # Create nodes
        output = nodes.new('ShaderNodeOutputMaterial')
        principled = nodes.new('ShaderNodeBsdfPrincipled')
        texture_coord = nodes.new('ShaderNodeTexCoord')
        mapping = nodes.new('ShaderNodeMapping')
        voronoi = nodes.new('ShaderNodeTexVoronoi')
        color_ramp = nodes.new('ShaderNodeValToRGB')
        
        # Position nodes
        output.location = Vector((300, 0))
        principled.location = Vector((0, 0))
        texture_coord.location = Vector((-800, 0))
        mapping.location = Vector((-600, 0))
        voronoi.location = Vector((-400, 0))
        color_ramp.location = Vector((-200, 0))
        
        # Configure voronoi
        voronoi.inputs['Scale'].default_value = 10.0
        voronoi.feature = 'DISTANCE_TO_EDGE'
        
        # Link nodes
        links = material.node_tree.links
        links.new(texture_coord.outputs['Generated'], mapping.inputs['Vector'])
        links.new(mapping.outputs['Vector'], voronoi.inputs['Vector'])
        links.new(voronoi.outputs['Distance'], color_ramp.inputs['Fac'])
        links.new(color_ramp.outputs['Color'], principled.inputs['Base Color'])
        links.new(principled.outputs['BSDF'], output.inputs['Surface'])
        
        return material

    def create_musgrave(self, name="MusgraveNoise"):
        """Create Musgrave-type noise texture"""
        material, nodes = self.create_base_material(name)
        
        # Create nodes
        output = nodes.new('ShaderNodeOutputMaterial')
        principled = nodes.new('ShaderNodeBsdfPrincipled')
        texture_coord = nodes.new('ShaderNodeTexCoord')
        mapping = nodes.new('ShaderNodeMapping')
        musgrave = nodes.new('ShaderNodeTexMusgrave')
        color_ramp = nodes.new('ShaderNodeValToRGB')
        
        # Position nodes
        output.location = Vector((300, 0))
        principled.location = Vector((0, 0))
        texture_coord.location = Vector((-800, 0))
        mapping.location = Vector((-600, 0))
        musgrave.location = Vector((-400, 0))
        color_ramp.location = Vector((-200, 0))
        
        # Configure Musgrave
        musgrave.musgrave_type = 'FBM'
        musgrave.inputs['Scale'].default_value = 5.0
        musgrave.inputs['Detail'].default_value = 8.0
        musgrave.inputs['Dimension'].default_value = 2.0
        
        # Link nodes
        links = material.node_tree.links
        links.new(texture_coord.outputs['Generated'], mapping.inputs['Vector'])
        links.new(mapping.outputs['Vector'], musgrave.inputs['Vector'])
        links.new(musgrave.outputs['Fac'], color_ramp.inputs['Fac'])
        links.new(color_ramp.outputs['Color'], principled.inputs['Base Color'])
        links.new(principled.outputs['BSDF'], output.inputs['Surface'])
        
        return material

    def create_wave(self, name="WaveNoise"):
        """Create wave-based noise texture"""
        material, nodes = self.create_base_material(name)
        
        # Create nodes
        output = nodes.new('ShaderNodeOutputMaterial')
        principled = nodes.new('ShaderNodeBsdfPrincipled')
        texture_coord = nodes.new('ShaderNodeTexCoord')
        mapping = nodes.new('ShaderNodeMapping')
        wave = nodes.new('ShaderNodeTexWave')
        color_ramp = nodes.new('ShaderNodeValToRGB')
        
        # Position nodes
        output.location = Vector((300, 0))
        principled.location = Vector((0, 0))
        texture_coord.location = Vector((-800, 0))
        mapping.location = Vector((-600, 0))
        wave.location = Vector((-400, 0))
        color_ramp.location = Vector((-200, 0))
        
        # Configure wave
        wave.wave_type = 'BANDS'
        wave.bands_direction = 'DIAGONAL'
        wave.inputs['Scale'].default_value = 5.0
        wave.inputs['Distortion'].default_value = 2.0
        wave.inputs['Detail'].default_value = 2.0
        
        # Link nodes
        links = material.node_tree.links
        links.new(texture_coord.outputs['Generated'], mapping.inputs['Vector'])
        links.new(mapping.outputs['Vector'], wave.inputs['Vector'])
        links.new(wave.outputs['Color'], color_ramp.inputs['Fac'])
        links.new(color_ramp.outputs['Color'], principled.inputs['Base Color'])
        links.new(principled.outputs['BSDF'], output.inputs['Surface'])
        
        return material

    def create_test_scene(self):
        """Create a test scene with different noise materials"""
        # Clear existing scene
        self.clear_scene()
        
        # Create a grid of planes
        spacing = 3
        for i, noise_type in enumerate(self.noise_types.keys()):
            row = i // 3
            col = i % 3
            
            # Create plane
            bpy.ops.mesh.primitive_plane_add(
                size=2,
                location=(col * spacing, row * spacing, 0)
            )
            plane = bpy.context.active_object
            
            # Create and assign material
            material = self.noise_types[noise_type](f"{noise_type.capitalize()}Noise")
            plane.data.materials.append(material)
            
            # Add text label
            bpy.ops.object.text_add(
                location=(col * spacing, row * spacing - 1.2, 0)
            )
            text = bpy.context.active_object
            text.data.body = noise_type.capitalize()
            text.data.align_x = 'CENTER'
            text.scale = (0.2, 0.2, 0.2)
        
        # Set up camera
        bpy.ops.object.camera_add(
            location=(4, -6, 8),
            rotation=(0.9, 0, 0.7)
        )
        bpy.context.scene.camera = bpy.context.active_object
        
        # Add lighting
        bpy.ops.object.light_add(
            type='SUN',
            location=(5, 5, 10),
            rotation=(0.5, 0.2, 0.3)
        )

def main():
    generator = NoiseTextureGenerator()
    generator.create_test_scene()
    
    # Set render settings
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.render.film_transparent = True
    bpy.context.scene.render.resolution_x = 1920
    bpy.context.scene.render.resolution_y = 1080
    
    # Optional: Render the scene
    # bpy.ops.render.render(write_still=True)

if __name__ == "__main__":
    main()
