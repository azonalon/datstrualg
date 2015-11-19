LevelOrderTreeWalk(ADT Tree T)


root = T.root();
node = root;


function LevelOrderTreeWalk(ADTTree T){


	Q = new Queue;

		Q.enqueue(T.root());

			repeat LevelOrderTreeWalkRecursiv{node}

				Q.dequeue(node);

				node = T.left(node)
				
				if (node =/ NIL){
					Q.enqueue(node)

					node = T.right (node)
					Q.enqueue(node)
				} else {
				break
				}
}
