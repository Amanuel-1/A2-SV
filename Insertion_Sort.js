'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

function insertionSort1(n, arr) {
    // Write your code here
    //print the array
    let print =()=>{
    let s="";
    for(let k=0;k<n;k++){
        
        s+=(k!=n-1)?arr[k]+" " : arr[k];
        
    }
   
    console.log(s)
}

   let j=n-2;
  
   
   let e = arr[n-1];
    while(arr[j]>e){
        arr[j+1] = arr[j]
        print();
        j--;
    }
    arr[j+1] =e;
   // console.log(arr)
   print()




}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    insertionSort1(n, arr);
}
