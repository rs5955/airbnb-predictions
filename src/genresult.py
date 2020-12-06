# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import csv

def main():
    nbri = []
    if len(sys.argv) != 3:
        print("Invalid amount of inputs.")
    else:
        homezip = sys.argv[1]
        curzip = sys.argv[2]
        h_sum = 0
        h_numapp = 0
        c_sum = 0
        c_numapp = 0
        with open('income.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    if row["Zip_Code"] == homezip:
                        h_sum += int(row["Median"])
                        h_numapp += 1
                    if row["Zip_Code"] == curzip:
                        c_sum += int(row["Median"])
                        c_numapp += 1
                line_count += 1
        if h_numapp == 0:
            h_final = 0
        else:
            h_final = (h_sum * 1.0)/h_numapp
        if c_numapp == 0:
            c_final = 0
        else:
            c_final = (c_sum * 1.0)/c_numapp

        #print(h_final)
        #print(c_final)
        incindex = incomeindex(h_final,c_final)
        minscore = 0
        maxscore = 0
        top10 = []
        nlc = 0
        with open('rooms.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if (line_count != 0) and (line_count % 9 == 6):
                    nlc += 1
                    inc = 0
                    with open('nycincome.csv', mode='r') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        line_count = 0
                        for row1 in csv_reader:
                            if line_count != 0:
                                if(row["neighborhood"] in row1["neighborhood"] and row["boro"] == row1["boro"]):
                                    inc1 = row1["mhi"]
                                    inc = int(inc1[-3:])+(1000*int(inc1[1:-4]))
                                    break
                            line_count += 1
                    try:
                        newscore = genscore(0,inc,int(row["price"]),incindex,0)
                    except:
                        newscore = 0
                    if (len(top10) < 10 or newscore > minscore) and (newscore not in nbri):
                        top10.append([newscore,row])
                        nbri.append(newscore);
                        if(newscore > maxscore):
                            maxscore = newscore
                        if(len(top10) > 10):
                            lowestvalue = 10000
                            lowestindex = 55000
                            counter = 0
                            for entry in top10:
                                if(entry[0] < lowestvalue):
                                    lowestvalue = entry[0]
                                    lowestindex = counter
                                counter += 1
                            del top10[lowestindex]
                            nbri.remove(lowestvalue)
                line_count += 1
        #print nlc
        while(len(top10) > 0):
            highest = -10000
            lowestindex = 55000
            counter = 0
            for entry in top10:
                if(entry[0] > highest):
                    highest = entry[0]
                    lowestindex = counter
                counter += 1
            print(top10[lowestindex][1]["id"]+";"+str(highest)+";"+top10[lowestindex][1]["price"]+";"+top10[lowestindex][1]["boro"]+";"+top10[lowestindex][1]["neighborhood"]+";"+top10[lowestindex][1]["room_type"]+";"+top10[lowestindex][1]["name"])
            del top10[lowestindex]


# Return an income index, between 1 and 10 inclusive, that reflects the user's estimated wealth.
def incomeindex(hometown,current):
    if hometown < 1000 or current < 1000:
        if hometown >= 1000:
            current = hometown
        elif current >= 1000:
            hometown = current
        else:
            return 1
    estimate = hometown*.35 + current*.65
    index = 10 * (estimate / 200000.0)
    #if index < 1:
        #index = 1
    #else:
        #index = int(index)
    return index

def genscore(id,areaincome,price,userincome,change):
    score = change

    # (65%) How close the room’s area income is to the user’s estimated income.
    areaindex = 10 * (areaincome / 200000.0)
    #if areaindex > 10:
        #areaindex = 10
    #if areaindex < 1:
        #areaindex = 1
    #else:
        #areaindex = int(areaindex)
    #print "areaindex: "+str(areaindex)+" &userincome: "+str(userincome)
    if(abs(areaindex - userincome) < .75):
        diff = 5
    else:
        diff = abs(areaindex - userincome)
    diff = 650*(diff/9.0) # Rebalance
    #print "diff = "+str(diff)
    score += diff

    # (35%) Deprioritizing rooms that are predicted to be too expensive.
    estmaxspend = userincome**2 * (500 / (userincome+1))
    #print "estmaxspend: "+str(estmaxspend)+" &price: "+str(price)
    if price < estmaxspend:
        diff3 = 10
    else:
        diff3 = 10*(abs(price - estmaxspend))/(price*1.0)
    diff3 = 350*(diff3/10.0)
    #print "diff3 = "+str(diff3)
    score += diff3
    score = int(score)
    #print("score "+str(score))
    return score

main()
