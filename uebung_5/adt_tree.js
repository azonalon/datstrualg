class PVTree {
    var preorderArr, degreeArr, elements ;

    function create(w) { 
        preorderArr = ( MaxLength ) * [ NULL ];
        degreeArr = ( MaxLength ) * [ NULL ];
        elements = 0; 
        if ( w != NULL ) { 
            preorderArr [ 0 ] = w;
            degreeArr [0] = 0; elements = 1;
        } 
    }

    function root ( ) { 
        if ( elements == 0 ) 
            return NULL; 
        else return 0; 
    }

    function retrieve ( p ) { 
        return preorderArr[p]; 
    }

    function leftMost ( p ) { 
        if ( degreeArr[p] == 0 ) 
            return NULL ; 
        return p + 1 ;
    }
}
