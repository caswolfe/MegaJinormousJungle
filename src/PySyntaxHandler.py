import keyword

class Syntax:
    keyword_list = keyword.kwlist
    COLORS = ['navy','dark turquoise','steel blue','midnight blue','slate blue','medium blue','blue','dark violet','green2','cyan4','red4','purple4','maroon3','magenta4','DeepPink3','dark orange','indian red','SlateBlue1','forest green','dodger blue','chocolate3','IndianRed3','orange2','VioletRed3','blue4','dark green','brown4','firebrick4','PaleTurquoise4','aquamarine4','saddle brown','dark slate gray','pink4','DarkOrange3','yellow4']

    color_dict = {}
    def __init__(self):
        self.assign_colors()
        #print(self.color_dict)

    def assign_colors(self):
        if len(self.COLORS) >= len(self.keyword_list):
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