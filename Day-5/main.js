var form =document.getElementById('addForm');

var itemlist=document.getElementById('items');




form.addEventListener('submit',addItem);

// deleting the item

itemlist.addEventListener('click',removeItem);



function addItem(e){
    e.preventDefault();
    var input=document.getElementById('inputtext').value;
    var li =document.createElement('li');

    li.className='list-group-item';

    li.appendChild(document.createTextNode(input));

    itemlist.appendChild(li);

    var delbtn=document.createElement('button');
    delbtn.className='btn btn-danger btn-sm float-right delete'

    delbtn.appendChild(document.createTextNode('X'));

    li.appendChild(delbtn);
   
}

function removeItem(e){
    if(e.target.classList.contains('delete'))
    {
        var li=e.target.parentElement;
        itemlist.removeChild(li);
    }
}