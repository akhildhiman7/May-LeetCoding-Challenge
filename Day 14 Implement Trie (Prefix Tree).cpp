/*
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
*/

class TrieNode {
public:
    char val;
    vector<TrieNode*> children;
    bool isTerminal;
    TrieNode(char val) {
        this->val = val;
        children.assign(26, NULL);
        isTerminal = false;
    }
};

class Trie {
    TrieNode *root = NULL;
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode('\0');
        root->isTerminal = true;
    }

    /** Inserts a word into the trie. */
    void insert(TrieNode *root, string word) {
        if (word.length() == 0) {
            root->isTerminal = true;
            return;
        }
        if (root->children[word[0] - 'a'] == NULL) {
            TrieNode *children = new TrieNode(word[0]);
            root->children[word[0] - 'a'] = children;
            insert(children, word.substr(1));
        }
        else {
            TrieNode *children = root->children[word[0] - 'a'];
            insert(children, word.substr(1));
        }
    }

    void insert(string word) {
        insert(root, word);
    }

    bool search(TrieNode *root, string word) {
        if (word.length() == 0) {
            if (root->isTerminal) {
                return true;
            }
            else
                return false;
        }
        if (root->children[word[0] - 'a']) {
            return search(root->children[word[0] - 'a'], word.substr(1));
        }
        else {
            return false;
        }
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        return search(root, word);
    }

    bool startsWith(TrieNode *root, string prefix) {
        if (prefix.length() == 0) {
            return true;
        }
        if (root->children[prefix[0] - 'a'])
            return startsWith(root->children[prefix[0] - 'a'], prefix.substr(1));
        else
            return false;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return startsWith(root, prefix);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
