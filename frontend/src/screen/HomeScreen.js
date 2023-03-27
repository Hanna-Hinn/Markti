import React from "react";
function HomeScreen() {
    function serach(e) {
        let serach = document.querySelector(".input-field");
        let serachValue;
        if (e.key == "Enter" && serach.value != "") {
            serachValue = serach.value;
        }

    }
    let flag = false
    function Button() {
        if(flag===false){
        let array = ["Ali baba", "amazon", "Ali Express","sajed","Ali baba", "amazon","aa","qqa"
        ,"Ali baba", "amazon","aa","qqa"];
        for (let i = 0; i < array.length; i++) {
            let btn = document.createElement('button');
            btn.innerText = array[i];
            document.querySelector(".filters").appendChild(btn)
            btn.addEventListener("click", function () {
                let filter = document.querySelector(".search-icon")
                let boxbtn = `<nav class="box-filter"> <span>${array[i]}</span> 
                <i class="fa fa-times" aria-hidden="true"></i>
                </nav>`
                filter.insertAdjacentHTML("afterend", boxbtn)
                let x = document.querySelector(".fa-times")
                let y = document.querySelector(".box-filter")
                x.addEventListener("click", function () {
                    y.remove()
                })
            })

        }

    }
    flag =true
}


    return (
        <div class="home">

            <i class="fa fa-home" aria-hidden="true"></i>

            <div class="search-icon">
                <input type="search" class="input-field" onKeyUp={serach} placeholder="Search for files, plugins,and creators" ></input>
                <i class="fa fa-search" aria-hidden="true"></i>
            </div>

            <div class="filters">
                <div className="store"><span onClick={Button}>Stores</span></div>

            </div>

        </div>
    );
}

export default HomeScreen;