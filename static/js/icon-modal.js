// Get the modal and reaction options
const iconModal = document.querySelector('.reaction-modal');
const iconOptions = document.querySelectorAll('.reaction-option');

// Hide the modal when a reaction is chosen
iconOptions.forEach(option => {
  option.addEventListener('click', function() {
    iconModal.style.display = 'none';
    // You can also do something with the chosen reaction here
    console.log("Reaction chosen: " + this.textContent);
  });
});

// // Hide the modal when the mouse leaves the modal area
// iconModal.addEventListener('mouseleave', function() {
//   iconModal.style.display = 'none';
// });
