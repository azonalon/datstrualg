function LevelOrderTreeWalk(ADT Tree T){}
    Q = new Queue;
    root = T.root();
    Q.enqueue(root);
    LevelOrderTreeWalkRecurse(root, Q);
}

function LevelOrderTreeWalkRecurse(ADTTree T, ADTQueue Q){
    node = Q.dequeue();
    left = T.left(node);
    right = T.right(node);

    print(T.retrieve(node));

    if (left != NIL) {
        Q.enqueue(left);
        LevelOrderTreeWalkRecurse(T, Q);
    }
    if (right != NIL) {
        Q.enqueue(right);
        LevelOrderTreeWalkRecurse(T, Q);
    }
}
