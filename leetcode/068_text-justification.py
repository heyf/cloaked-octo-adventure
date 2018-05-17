'''
068. Text Justification - LeetCode
https://leetcode.com/problems/text-justification/description/
'''

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret = []
        while words:
            line = []
            count = 0
            tick = 0
            # get words
            while count < maxWidth:
                w = words.pop(0)
                line.append(w)
                count += len(w)
                if len(words) == 0: # final line
                    if count < maxWidth:
                        line.append( " " )
                        count += 1
                    while count < maxWidth:
                        line[-1] += " "
                        count += 1
                    break
                if count >= maxWidth:
                    break
                if count + len(words[0]) + 1 > maxWidth:
                    if len(line) == 1:
                        line.append(" ")
                        count += 1
                        tick += 1
                    break
                line.append(" ")
                count += 1
                tick += 1
            # append space
            tock = 0
            while count < maxWidth and tick:
                line[(tock%tick)*2+1] += " "
                count += 1
                tock += 1
            ret.append( "".join(line) )
        return ret
            
ans = [
    [
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
        [
           "This    is    an",
           "example  of text",
           "justification.  "
        ]
    ],[
        ["What","must","be","acknowledgment","shall","be"], 
        16,
        [
          "What   must   be",
          "acknowledgment  ",
          "shall be        "
        ]
#         Explanation: Note that the last line is "shall be    " instead of "shall     be",
#              because the last line must be left-justified instead of fully-justified.
#              Note that the second line is also left-justified becase it contains only one word.
    ],[
        ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"],
        20,
        [
          "Science  is  what we",
          "understand      well",
          "enough to explain to",
          "a  computer.  Art is",
          "everything  else  we",
          "do                  "
        ]
    ],[
        ["ab","c","defg","h","ijk"],
        4,
        ["ab c","defg","h   ","ijk "]
    ],[
        ["ab"],
        2,
        ["ab"]
    ]
]

s = Solution()
for i in ans:
    ret = s.fullJustify( i[0], i[1] )
    print( "O" if ret == i[2] else "X", ret )