function quicksort( arr ) {
    let l = arr.length;
    if ( l < 2 ) return arr;
    if ( l === 2 ) {
        return arr[0] <= arr[1] ? arr : arr.reverse();
    }
    // sort by pivot 
    let pivot = arr[0];
    let arr1 = [];
    let arr2 = [];
    for ( let i = 1; i < l; i++ ) {
        let val = arr[i];
        val > pivot ? arr2.push( val ) : arr1.push( val );
    }
    let sortedArr1 = quicksort( arr1 );
    let sortedArr2 = quicksort( arr2 );
    return [ ...sortedArr1, pivot, ...sortedArr2 ];
}

function count( arr ) {
    let obj = {};
    for ( let x of arr ) {
        obj[x] ? obj[x]++ : (obj[x]=1);
    }
    return obj;
}

function createArray( length, maxValue=9 ) {
    let arr = new Array(length);
    arr.fill(0);
    let maxIndex = maxValue+1;
    return arr.map( x => Math.floor( Math.random() * maxIndex ));
}