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
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function countSwaps(a) {
    // Write your code here
let temp,counter =0;
 for(let i=0;i<a.length ;i++){
        for(let j=i;j<a.length ;j++){
            if(a[j]<a[i]){
                temp =a[i];
                a[i]=a[j];
                a[j]=temp;
                counter++;
            }
        }
    }
    
    console.log("Array is sorted in %d swaps.",counter);
    console.log("First Element: %d",a[0]);
    console.log("Last Element: %d",a[a.length-1]);
}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const a = readLine().replace(/\s+$/g, '').split(' ').map(aTemp => parseInt(aTemp, 10));

    countSwaps(a);
}
