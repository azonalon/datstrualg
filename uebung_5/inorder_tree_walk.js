public void inorderItr(Node root){
	Deque<Node> ADT-Stack = new LinkedList<Node>();
	Node node = root;
	while(true){
		if(node != null){
		  S.push(node);
			node = T.left(node);
		}
		else{
			if(S.empty()){
				break;
			}
			node = S.pop();
			println(node.data);
			node = T.right(node);
		}
	}
}
