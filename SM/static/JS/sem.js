function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  

  function myFunction2() {
    document.getElementById("myDropdown2").classList.toggle("show");
  }

  
  function myFunction3() {
    document.getElementById("myDropdown3").classList.toggle("show");
  }

  
  function myFunction4() {
    document.getElementById("myDropdown4").classList.toggle("show");
  }

  
  function myFunction5() {
    document.getElementById("myDropdown5").classList.toggle("show");
  }

  function myFunction6() {
    document.getElementById("myDropdown6").classList.toggle("show");
  }

  function myFunction7() {
    document.getElementById("myDropdown7").classList.toggle("show");
  }

  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }