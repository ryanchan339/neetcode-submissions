/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* curr = head;
        std::set<ListNode*> set;
        while (curr != nullptr) {
            if (set.contains(curr)) {
                return true;
            }
            set.insert(curr);
            curr = curr->next;
        }
        return false;
       
    }
};