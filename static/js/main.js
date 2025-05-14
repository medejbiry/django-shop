let nav = document.getElementById("nav");
let hideenNav = document.getElementById("hidden-nav")
nav.addEventListener("mouseover", function () {
  
    hideenNav.style.display = "block"
  
});
hideenNav.addEventListener("mouseleave",function(){
     hideenNav.style.display = "none"
})
console.log("test");
