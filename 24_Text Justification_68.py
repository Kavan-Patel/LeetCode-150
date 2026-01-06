# 68. Text Justification
# https://leetcode.com/problems/text-justification/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        # 3 parts
        # Part 1 : Add words into the current line
        # Part 2 : Justify the current line 
        # Part 3 : Handle the last line special case

        res, current_line, current_len = [] , [] , 0

        for word in words:

            # First we'll check if we add word in current line will len of current line
            # exceed maxWidth?
            if current_len + len(current_line) + len(word) > maxWidth:
                
                # we'll check len of total space need to allocated
                total_spaces = maxWidth - current_len
                # we'll check the total gaps in current_line
                gap = len(current_line) - 1

                # If there's only one word in current_line
                if gap == 0:
                    # we need to left justify
                    res.append(current_line[0] + ' ' * total_spaces)
                else: 
                    # We'll check how many space will go between each line 
                    space_inside = total_spaces // gap
                    space_remain = total_spaces % gap
                    temp_line = ''
                    for j in range(gap):
                        temp_line += current_line[j] + ' ' * space_inside + (' ' if space_remain > 0 else '')
                        space_remain -= 1
                    temp_line += current_line[-1]
                    res.append(temp_line)

                current_line, current_len = [] , 0
            # Else we'll add word in current_line and increse len 
            current_line.append(word)
            current_len += len(word)
        
        # Now we'll handle the last line justified
        last_line = ' '.join(current_line)
        res.append(last_line + ' ' * (maxWidth - len(last_line)))

        return res
