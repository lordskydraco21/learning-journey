// Create the button to open the modal
const openModalButton = document.createElement('button');
openModalButton.textContent = 'Open Modal';
openModalButton.style.position = 'fixed';
openModalButton.style.top = '10px';
openModalButton.style.right = '10px';
openModalButton.style.padding = '10px 20px';
openModalButton.style.backgroundColor = '#007BFF';
openModalButton.style.color = '#FFF';
openModalButton.style.border = 'none';
openModalButton.style.borderRadius = '5px';
openModalButton.style.cursor = 'pointer';
openModalButton.style.zIndex = '1000';

// Create the modal container
const modal = document.createElement('div');
modal.style.display = 'none'; // Hidden by default
modal.style.position = 'fixed';
modal.style.top = '0';
modal.style.left = '0';
modal.style.width = '100%';
modal.style.height = '100%';
modal.style.backgroundColor = 'rgba(0, 0, 0, 0.9)';
modal.style.zIndex = '1001';
modal.style.justifyContent = 'center';
modal.style.alignItems = 'center';
modal.style.flexDirection = 'column';

// Create the modal content
const modalContent = document.createElement('div');
modalContent.style.backgroundColor = '#1E1E1E';
modalContent.style.width = '100%';
modalContent.style.height = '100%';
modalContent.style.display = 'flex';
modalContent.style.justifyContent = 'center';
modalContent.style.alignItems = 'center';
modalContent.style.flexDirection = 'column';

// Add a close button to the modal
const closeModalButton = document.createElement('button');
closeModalButton.textContent = 'Close';
closeModalButton.style.position = 'absolute';
closeModalButton.style.top = '20px';
closeModalButton.style.right = '20px';
closeModalButton.style.padding = '10px 20px';
closeModalButton.style.backgroundColor = '#FF0000';
closeModalButton.style.color = '#FFF';
closeModalButton.style.border = 'none';
closeModalButton.style.borderRadius = '5px';
closeModalButton.style.cursor = 'pointer';
closeModalButton.style.zIndex = '1002';

// Append the close button and modal content to the modal
modal.appendChild(modalContent);
modal.appendChild(closeModalButton);

// Add the button and modal to the body
document.body.appendChild(openModalButton);
document.body.appendChild(modal);

// Function to open the modal
openModalButton.addEventListener('click', () => {
    modal.style.display = 'flex';
    initializeP5(); // Initialize p5.js when the modal opens
});

// Function to close the modal
closeModalButton.addEventListener('click', () => {
    modal.style.display = 'none';
    if (window.p5Instance) {
        window.p5Instance.remove(); // Remove the p5.js instance when the modal closes
    }
});

// Close modal when clicking outside the modal content
modal.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
        if (window.p5Instance) {
            window.p5Instance.remove(); // Remove the p5.js instance when the modal closes
        }
    }
});

// Function to initialize p5.js
function initializeP5() {
    const sketch = (p) => {
        p.setup = () => {
            const canvas = p.createCanvas(window.innerWidth, window.innerHeight);
            canvas.parent(modalContent); // Attach the canvas to the modal content
            p.background(0);
        };

        p.draw = () => {
            p.fill(255, 50);
            p.noStroke();
            p.ellipse(p.mouseX, p.mouseY, 50, 50); // Draw circles at the mouse position
        };

        p.windowResized = () => {
            p.resizeCanvas(window.innerWidth, window.innerHeight); // Resize canvas when the window is resized
        };
    };

    window.p5Instance = new p5(sketch); // Create a new p5.js instance
}

// Load p5.js dynamically if not already loaded
if (!window.p5) {
    const p5Script = document.createElement('script');
    p5Script.src = 'https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.6.0/p5.js';
    p5Script.onload = () => console.log('p5.js loaded!');
    document.head.appendChild(p5Script);
}
