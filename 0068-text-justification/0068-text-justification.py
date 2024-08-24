class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0

        for w in words:
            # Check if adding the current word would exceed the maxWidth
            if num_of_letters + len(w) + len(cur) > maxWidth:
                # Justify the current line and add it to the result
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            # Add the word to the current line
            cur.append(w)
            num_of_letters += len(w)

        # Last line should be left-justified
        res.append(' '.join(cur).ljust(maxWidth))
        return res
