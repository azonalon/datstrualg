class PWTree implements ADTTree{
    var preorderArr, weightArr, elements;
    function create(w) { 
        preorderArr = (MaxLength) * [NIL];
        weightArr = (MaxLength) * [NIL];
        elements = 0; 
        if(w != NIL) { 
            preorderArr[0] = w;
            weightArr[0] = 0;
            elements = 1;
        } 
    }
    function root() { 
        if(elements != 0) return 0; 
        return NIL; 
    }
    function retrieve(p) { 
        return preorderArr[p]; 
    }
    function leftMost(p) { 
        if(degreeArr[p] != 0 ) return p + 1; 
        return NIL;
    }
    function nextRight(p) {
        suspect = p + weightArr[p] + 1;
        if(parent(suspect) == parent(p)) return suspect;
        return NIL;
    }
    function nextLeft(p) {
        for(i = 0; i < p; i++) {
            if(nextRight(i) == p) return i;
        }
        return NIL;
    }
    /*function parent(p) {
        return NIL;
    }*/
    function detach(p) {
        for(i = p; i <= p + weightArr[p]; i++) {
            preorderArr[i] = preorderArr[i + weightArr[i] + 1];
            elements--;
        }
        if(p + weightArr[p] + 1 > elements) {
            for(i = p + weightArr[p] + 1; i < elements; i++) {
                preorderArr[i] = preorderArr[i + weightArr[i] + 1];
            }
        }
    }
    function empty() {
        if(elements == 0) return true;
        return false;
    }
}
