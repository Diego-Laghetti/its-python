const arr1 = [1,2,3]
console.log(arr1,...arr1)
const arr2 = [...arr1]
arr1.push(4);

arr1.unshift(0);

let[a,b] = arr1;

console.log(arr1);
console.log(arr2);

console.log(arr1);
console.log(arr2);

const prof={
    "first name":"Diego",
    cognome: "Laghettodelleur",
    eta: 20,
    indirizzo:{
        città: "Roma",
        via: "Vitaliano Rotellini" 
    }
}

let{nome, cognome}=prof;
console.log(nome, cognome)
console.log(prof.indirizzo.via)

const prof1 = new Object();
prof1.cognome = "Laghettodelleur";
prof1.nome= "Diego";
console.log(prof1);

function persona(){
    this.nome="";
    this.cognome="";
}

const Diego = new persona();

console.log();

for(var i=0;i<4;i++){
    console.log(i)
}

{
let ab="33";
console.log(ab);
}

function lista(){
    console
}

