from random import randrange

### Initialization
text = "My name is Dang and I've known Jade and Sean for $num$ years. I $ver$ all the way from $nou$ to celebrate this day. I am so $adj$ that Jade and Sean are tying the knot! They have to be the most $adj$ $nou$ and I wish them $adj$ $nou$ for years to come. My best advice? Don't forget to $ver$ before you $ver$ and $ver$ after the $nou$. Sean, you should always $ver$ Jade's $nou$, and Jade you should always $ver$ Sean's $nou$. I wish you both a lifetime of happiness and $nou$!"


### Get data
f_adj  = open('clean.adj' , 'r')
f_adv  = open('clean.adv' , 'r')
f_noun = open('clean.noun', 'r')
f_verb = open('clean.verb', 'r')

word = {'adj':f_adj.readlines(), 'adv':f_adv.readlines(), 'nou':f_noun.readlines(), 'ver':f_verb.readlines(), 'num':[str(i+1) for i in range(50)]}

f_adj.close() 
f_adv.close() 
f_noun.close() 
f_verb.close() 

### Fill in the blanks
text = text.split()
for i in range(len(text)):
    if text[i][0] == '$':
        text[i] = word[text[i][1:4]][randrange(len(word[text[i][1:4]]))]
        text[i] = text[i][:len(text[i])-1]

print(' '.join(text))
