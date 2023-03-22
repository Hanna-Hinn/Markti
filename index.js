let serach = document.querySelector(".input-field");
let serachValue ;
// value of serach
serach.addEventListener("keyup",(e) => {
    if (e.key == "Enter" && serach.value != "") {
        // serachValue = serach.value;  
        console.log(serach.value)      
    }
    });

    
