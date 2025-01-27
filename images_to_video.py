import cv2
import os
from pathlib import Path
import numpy as np
from PIL import Image

class ImageVideoConverter:
    def __init__(self, image_folder, output_file='output_video.mp4', fps=30):
        """
        Initialize the converter
        :param image_folder: Folder containing the images
        :param output_file: Output video file name
        :param fps: Frames per second for the output video
        """
        self.image_folder = Path(image_folder)
        self.output_file = output_file
        self.fps = fps
        
        # Supported image formats
        self.image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}

    def get_image_files(self):
        """Get all image files from the folder"""
        image_files = []
        for ext in self.image_extensions:
            image_files.extend(list(self.image_folder.glob(f'*{ext}')))
            image_files.extend(list(self.image_folder.glob(f'*{ext.upper()}')))
        return sorted(image_files)

    def get_image_size(self, image_path):
        """Get the size of an image using PIL"""
        with Image.open(image_path) as img:
            return img.size

    def resize_image(self, image, target_size):
        """Resize image to target size"""
        return cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)

    def create_video(self, target_size=None, transition_frames=10):
        """
        Create video from images with smooth transitions
        :param target_size: Target size for the video (width, height)
        :param transition_frames: Number of frames for transitions
        """
        # Get image files
        image_files = self.get_image_files()
        if not image_files:
            print("No image files found!")
            return False

        print(f"Found {len(image_files)} images")

        # Determine video size if not specified
        if target_size is None:
            # Get size of first image
            target_size = self.get_image_size(image_files[0])
            print(f"Using size from first image: {target_size}")

        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_file, fourcc, self.fps, target_size)

        try:
            prev_frame = None
            for i, image_path in enumerate(image_files):
                print(f"Processing image {i+1}/{len(image_files)}: {image_path.name}")

                # Read and resize current image
                current_image = cv2.imread(str(image_path))
                if current_image is None:
                    print(f"Error reading image: {image_path}")
                    continue

                current_frame = self.resize_image(current_image, target_size)

                # If this is not the first image, create transition
                if prev_frame is not None:
                    for t in range(transition_frames):
                        # Calculate alpha for smooth transition
                        alpha = t / transition_frames
                        # Create transition frame
                        transition_frame = cv2.addWeighted(
                            prev_frame, 1 - alpha,
                            current_frame, alpha,
                            0
                        )
                        out.write(transition_frame)

                # Write the current frame multiple times for duration
                for _ in range(self.fps):  # Show each image for 1 second
                    out.write(current_frame)

                prev_frame = current_frame

            # Release video writer
            out.release()
            print(f"\nVideo created successfully: {self.output_file}")
            print(f"Video properties:")
            print(f"- Resolution: {target_size}")
            print(f"- FPS: {self.fps}")
            print(f"- Duration: ~{len(image_files)} seconds (not including transitions)")
            return True

        except Exception as e:
            print(f"Error creating video: {str(e)}")
            if out:
                out.release()
            return False

def main():
    # Get current directory
    current_dir = Path.cwd()
    image_folder = current_dir / "project_files_20250127_121908"  # Using the folder from previous script
    
    print("Image to Video Converter")
    print("=======================")
    print(f"Image folder: {image_folder}")
    
    # Create converter instance
    converter = ImageVideoConverter(
        image_folder=image_folder,
        output_file='combined_images.mp4',
        fps=30
    )
    
    # Create video with transitions
    converter.create_video(transition_frames=15)  # 15 frames for smooth transitions

if __name__ == "__main__":
    main()
