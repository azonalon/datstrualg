InorderTreeWalk(ADTTree T){
    S = new ADTStack;
    root = T.root();
    node = root;
    while(true) {
        if(node != NIL) {
            S.push(node);
            node = T.left(node);
        }
        else {
            if(S.empty()) {
                break;
            }
            node = S.pop();
            print(T.retrieve(node));
            node = T.right(node);
        }
    }
}
