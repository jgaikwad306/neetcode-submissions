class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() == t.length()){
            unordered_map<char,int> letters;
            unordered_map<char,int> lettert;

            for(char c: s){
                letters[c]++;
                
            }
            for(char c: t){
                lettert[c]++;
                
            }
            

           for (auto& [ch, count] : letters) {
            if (lettert[ch] != count) return false;
        }
            return true;
        }
      return false;  
    }
    
};
