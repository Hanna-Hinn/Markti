function main(){
    let flag1 = false
    let flag2 = false    
    let flag3 = false
    function btnClick(){    
           if(flag1===false){
            let filter = document.querySelector(".search-icon")        
            let boxbtn = `<nav class="box-filter"> <span>Ali Baba</span> 
            <i class="fa fa-times" aria-hidden="true"></i>
            </nav>`
            filter.insertAdjacentHTML("afterend",boxbtn)
            let x =  document.querySelector(".fa-times")
            let y = document.querySelector(".box-filter") 
            flag1 = true  
            x.addEventListener("click",function(){
                y.remove()
                flag1 = false
            })
           
           }
                
    }   
    
    function btnClick2(){  
        if(flag2 === false){
            let filter = document.querySelector(".search-icon")
        let boxbtn = `<nav class="box-filter"> <span>amzone</span> 
        <i class="fa fa-times" aria-hidden="true"></i>
        </nav>`
        filter.insertAdjacentHTML("afterend",boxbtn)
        let x =  document.querySelector(".fa-times")
        let y = document.querySelector(".box-filter")
        flag2 = true
        x.addEventListener("click",function(){
            y.remove()
            flag2 = false
        })
        
        }
                
    }
    
    function btnClick3(){ 
        if(flag3 === false){
            let filter = document.querySelector(".search-icon")
            let boxbtn = `<nav class="box-filter"> <span class="ali3">Ali express</span> 
            <i class="fa fa-times" aria-hidden="true"></i>
            </nav>`
            filter.insertAdjacentHTML("afterend",boxbtn)
            let x =  document.querySelector(".fa-times")
            let y = document.querySelector(".box-filter")
            flag3 = true
            x.addEventListener("click",function(){
                y.remove()
                flag3 = false
            })
            
        }
                
    }

     function serach(e){
        let serach = document.querySelector(".input-field");
        let serachValue ;
        if (e.key == "Enter" && serach.value != "") {
            serachValue = serach.value;              
     }

  }


return <nav class="home"><i class="fa fa-home" aria-hidden="true"></i>

<nav class="search-icon">           
<input type="search" class="input-field" onKeyUp={serach} placeholder="Search for files, plugins,and creators" ></input>
<i class="fa fa-search" aria-hidden="true"></i>
</nav>

<nav class="filters">
<h1>Stores:</h1>
<button class="btn1" onClick={btnClick}>Ali baba</button>
<button class="btn2" onClick={btnClick2}>amazon</button>
<button class="btn3" onClick={btnClick3}>Ali Express</button>
</nav>

</nav>

}

export default main;