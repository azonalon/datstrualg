function quicksortInplace(A, s, e) {
    if(s < e){
        pivot = partition(A, s, e);
        quicksortInplace(A, s        , pivot - 1);
        quicksortInplace(A, pivot + 1, e        );
    }
}

function partition(A, s, e) {
    // find pivot's index and place it correctly
    // then return it's index
    // pivot = e
    left_of_pivot = e - 1;
    for(i = s; i < pivot; ) {
        if(A[e] < A[i]) {
            swap(A[left_of_pivot], A[i]);
            left_of_pivot--;
        }
        else i++;
    }
    pivot = left_of_pivot + 1;
    swap(A[pivot], e);
    return pivot;
}
