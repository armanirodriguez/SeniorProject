let count = 0;
$(document).ready(function () {
    let curr = localStorage.getItem("song_checks");
    if (curr === null){
        localStorage.setItem("song_checks", "");
    }
    console.log(curr);
    if(curr !== "" && curr !== null){
        if(curr[curr.length] == ","){
            localStorage.setItem("song_checks", curr.substring(0, curr.length-1));
        }
        const myArray = localStorage.getItem("song_checks").split(",").filter(Boolean);
        console.log(localStorage.getItem("song_checks"));
        console.log(myArray);
            for(var i = 0; i < myArray.length; i++) {
                let el;
                if(document.getElementById(myArray[i])){
                    el = document.getElementById(myArray[i]);
                    el.checked = true;
                }
            }
    }
});

jQuery($ => {
    $(".box").on('click', function () {
        let clicked = localStorage.getItem("song_checks");  
        if(clicked !== null){
            if(!(clicked.includes($(this).attr('id').toString())) && count <= 3)
            {
                localStorage.setItem("song_checks", $(this).attr('id').toString() + "," + clicked);
            }
            else{
                localStorage.setItem("song_checks", clicked.replace($(this).attr('id').toString()+",",''));
            }
        }
    });
  });

//localStorage.setItem('name',string.replace(substring,''));

function clearLocal() {
    localStorage.removeItem("song_checks");
}