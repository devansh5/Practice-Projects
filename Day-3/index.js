let colorchange=document.getElementById('mousehover')

colorchange.addEventListener('mousemove',colorchan);

function colorchan(e){
    document.body.style.backgroundColor="rgb("+e.clientX+","+e.clientY+","+"105)";
}