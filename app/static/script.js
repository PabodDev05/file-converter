//hANDLE THE doggler animation
const toggler = document.querySelector('.custom-toggler');
const offcanvas = document.getElementById('offcanvasNavbar');

// Handle Toggler Animation
toggler.addEventListener('click', function(){
    this.classList.toggle('active');
})
// Sync Toggler State With Offcanvas Events
offcanvas.addEventListener('shown.bs.offcanvas', function(){
    //add the "active " class to the toggler when the offcanvas is shown    
    toggler.classList.add('active');
})

offcanvas.addEventListener('hidden.bs.offcanvas', function(){
    //remove the "active" class from the toggler when the offcanvas is hidden
    toggler.classList.remove('active');
})

// Handle DropDown Menu
let dropdownMenu = document.querySelectorAll('.dropdown');
let dropGui = document.getElementById('dropdown-menu');

//fade effect animation
const observer = new IntersectionObserver((entries) =>{
    entries.forEach((entry) =>{
        console.log(entry)
        if (entry.isIntersecting){
            entry.target.classList.add('show');
        }else{
            entry.target.classList.remove('show');  
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));