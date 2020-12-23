/*

let btn = document.querySelector('button');
let div = document.querySelector('div.cabildo-form');

btn.addEventListener('click',()=>{
  if (div.style.display == 'none'){
    div.stype.display = 'block';
  }else {
    div.style.display = 'none';
  }
})
*/

var a;
function show_hide_form(){
  if(a==1){
    document.getElementById("cabildo-form").style.display="none";
    return a=0;
  }
  else{
    document.getElementById("cabildo-form").style.display="inline";
    return a=1;
  }
}

//etiquetas-multiplechoice
