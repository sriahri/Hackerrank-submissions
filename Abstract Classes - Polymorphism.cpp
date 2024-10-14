class LRUCache : Cache
{
   int sz;
public:
   LRUCache(int cap)
   {
      sz = 0;
      cp = cap;
      tail = head = NULL;
   }

   virtual void set(int k, int v) {
      map<int, Node*>::const_iterator it = mp.find(k);
      if (it != mp.cend())
      {
         it->second->value = v;
         get(k);
         return;
      }

      ++sz;
      Node* newNode = new Node(NULL, head, k, v);
      mp[k] = newNode;
      if (head != NULL)
      {
         head->prev = newNode;
      }
      head = newNode;
      if (tail == NULL)
      {
         tail = head;
      }

      if (sz > cp)
      {
         tail->prev->next = NULL;
         Node* toRemove = tail;
         mp.erase(tail->key);
         tail = tail->prev;
         delete toRemove;
         --sz;
      }

   }

   virtual int get(int k) {
      map<int, Node*>::const_iterator it = mp.find(k);
      if (it == mp.cend())
      {
         return -1;
      }

      int res = it->second->value;

      Node* thisNode = it->second;
      Node* tmp = thisNode->prev;
      if (tmp != NULL)
      {
         tmp->next = thisNode->next;

         tmp = thisNode->next;
         if (tmp != NULL)
         {
            tmp->prev = thisNode->prev;
         }

         thisNode->prev = NULL;
         thisNode->next = head;
         head = thisNode;
      }

      return res;
   }

};