import keyword

class Syntax:
    keyword_list = keyword.kwlist
    COLORS = [ 'azure', 'alice blue', 'lavender',
        'lavender blush', 'misty rose', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
        'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
        'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
        'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
        'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
        'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
        'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
        'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
        'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
        'indian red', 'saddle brown', 'sandy brown', 'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
        'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
        'pale violet red', 'maroon', 'medium violet red', 'violet red',
        'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
        'thistle', 'snow2', 'snow3']

    color_dict = {}
    def __init__(self):
        self.assign_colors()
        #print(self.color_dict)

    def assign_colors(self):
        if len(self.COLORS) > len(self.keyword_list):
            i = 0
            for kw in self.keyword_list:
                self.color_dict[kw] = self.COLORS[i]
                i+=1
            return True
        else:
            raise Exception("Need more colors for color scheme")


    def add_keyword(self,word):
        self.keyword_list.append(word)

    def get_keywords(self):
        return self.keyword_list

    def get_color_dict(self):
        return self.color_dict
    

#s = Syntax()