function searchSequence(A, M, n, S, m) {
    last_marker = -1;
    
    for (i = 0; i < n; i++) { 
    // initialize the last marker
        if (M[i] == 0) {
            last_marker = i;
        }
    }

    for(s = 0; s < m; s++) {
    // search for elements in S
        s_in_A = false;
        for (i = 0; i < n; i++) { 
            if(A[i] == S[s]) {
                s_in_A = true;
                if(M[i] == 1) {
                    print("Found", S[s]);
                }
                else {
                    print("Not Found", S[s]);
                }

                if(i > 0) {
                    // transpose method
                    // update marker
                    if(i == last_marker && M[i-1] != 0)
                        last_marker--;
                    swap(A[i], A[i-1]);
                    swap(M[i], M[i-1]);
                }
                break;
            }
        }
        if(!s_in_A) {
            if(last_marker != -1) {
                A[last_marker] = S[s];
            }
        }
    }
}
