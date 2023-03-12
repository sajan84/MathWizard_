from word2number import w2n


operator_map = {
    "plus": "+",
    "substract": "-",
    "multiple": "*",
    "division": "/",

}




# with open('input4small.txt', 'r') as file:
with open('input4large.txt', 'r') as file:

    file.readline()
    lines=file.readlines()


    for line in lines:
        
        
        words = line


        equalSplit = []
        if words.find('equals'):
                equalSplit = words.split("equals")

        if words.find('=') != -1:
                equalSplit = words.split("=")
               
    

        leftExpression = equalSplit[0].strip()
        rightExpression = equalSplit[1].strip()
        split_string = leftExpression.split(" ")
   

        s = ""
        i = 0
        mylist = []
        for word in split_string:

                if word == 'multiple' or word == 'division' or word == 'plus' or word == 'substract':
                    if s!="":
                        number = w2n.word_to_num(s)
                        p = str(number)
                        mylist.insert(i, p)
                        i = i+1
                        s = ""
                    operator = operator_map.get(word)
                    mylist.insert(i, operator)
                    i = i+1


                elif word.isdigit():
                    if (s != ""):
                        number = w2n.word_to_num(s)
                        p = str(number)
                        mylist.insert(i, p)
                        i = i+1
                        s = ""
                    mylist.insert(i, word)
                    i = i+1
           

                elif word == '+' or word == '-' or word == '*' or word == '/':
                    if (s != ""):
                        number = w2n.word_to_num(s)
                        p = str(number)
                        mylist.insert(i, p)
                        i = i+1
                        s = ""

                    mylist.insert(i, word)
                    i = i+1
            

                else:
                    s = (s+' '+word).strip()
                    

        if (s != ""):

                number = w2n.word_to_num(s)
                p = str(number)
                mylist.insert(i, p)
                i = i+1
                s = ""

  
        expression = ""
        for i in mylist:
                expression = expression+i


        output = eval(expression)
   
        output = str(output)

        output = float(output)
        output = str(output)

        rightExpression = float(rightExpression)
        rightExpression = str(rightExpression)

        
        # with open('output4small.txt', 'a') as file:
        with open('output4large.txt', 'a') as file:
            if output == rightExpression:
                    file.write('true\n')
            else:
                file.write('false\n')
        file.close()

