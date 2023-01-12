//{ Driver Code Starts
//Initial Template for javascript

"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((string) => {
      return string.trim();
    });

  main();
});

function readLine() {
  return inputString[currentLine++];
}

/* Function to print an array */
function printArray(arr, size) {
  let i;
  let s = "";
  for (i = 0; i < size; i++) {
    if(arr[i] === -0)
      arr[i] = 0;
    s += arr[i] + " ";
  }
  console.log(s);
}

function main() {
  let t = parseInt(readLine());
  let i = 0;
  for (; i < t; i++) {
    let n = parseInt(readLine());
    let arr = new Array(n);
    let input_line = readLine().split(" ").map((x) => parseInt(x));
    for(let j = 0;j<n;j++) arr[j] = input_line[j];
    let obj = new Solution();
    obj.selectionSort(arr,n);
    printArray(arr,arr.length);
  }
}
// } Driver Code Ends


//User function Template for javascript

/**
 *
 * select
 * @param {number[]} arr
 * @param {number} i
 * @return {number}
 *
 * selectionSort
 * @param {number[]} arr
 * @param {number} n
 */
class Solution
{
  select(arr,i){
      let temp;
     // code here such that selectionSort() sorts arr[]
     for(let j=i;j<arr.length;j++){
         if(arr[j]<arr[i]){
             temp = arr[i];
             arr[i] =arr[j];
             arr[j]=temp;
         }
     }
  }

  //Function to sort the array using selection sort algorithm.
  selectionSort(arr,n){
       let print =()=>{
    let s="";
    for(let k=0;k<n;k++){
        
        s+= arr[k]+ " ";
        
    }
   
    console.log(s)
}
   //code here
   let i=0;
   while(i<n){
       this.select(arr,i);
       i++;
   }

  // print()
   
  }
  
  
  
  
  
  
}