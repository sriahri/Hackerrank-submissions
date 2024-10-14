// Complete the has_cycle function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */
bool has_cycle(SinglyLinkedListNode* h) {
    
    unordered_set<SinglyLinkedListNode*> s; 
    while (h != NULL) { 
        if (s.find(h) != s.end()) 
            return true;
        s.insert(h); 
  
        h = h->next; 
    } 
  
    return false; 

}