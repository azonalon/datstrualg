function KnapsackGreedy(items, V) {
    packing_priority = new MaxHeap();
    for(i = 0; i < len(items); i++) {
        packing_priority.insert(items[i]);
    }

    backpack_value = 0;
    item = packing_priority.delMax();
    volume = item.second();
    while(volume <= V) {
        backpack_value += item.third();
        item = packing_priority.delMax();
        volume += item.second();
    }
    return backpack_value;
}
