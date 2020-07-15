#include <iostream>
using namespace std;

class Node {
    public:
        int data;
        Node* next;
};

Node* buildLL(){
    
    Node* node1 = NULL;
    Node* node2 = NULL;
    Node* node3 = NULL;

    node1 = new Node();
    node2 = new Node();
    node3 = new Node();

    node1->next = node2;
    node2->next = node3;

    node1->data = 3;

    return node1;
}

int main() {
    
    
    
    buildLL()

    cout << node1->data;

    return 0;
}
