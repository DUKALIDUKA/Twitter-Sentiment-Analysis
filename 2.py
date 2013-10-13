import sys  
import json  
import operator  
   
def main():  
      tweet_file = open(sys.argv[1])  
   
      tags = {} #pair tag, occurrences in all tweets  
      #poplate our dict object  
      for line in tweet_file:  
           #convert the line from file into a json object  
           mystr = json.loads(line)  
           #search for tags and count them  
           if 'entities' in mystr.keys() and mystr["entities"]["hashtags"] != []:  
                for hashtag in mystr["entities"]["hashtags"]:  
                     if hashtag["text"] not in tags.keys():  
                          tags[hashtag["text"]]=1  
                     else:  
                          tags[hashtag["text"]]+=1  
      #sort our dict object by descending values  
      sorted_dict = sorted(tags.iteritems(), key=operator.itemgetter(1), reverse=True)  
      #print top 10 hashtag count values  
      for i in range(10):  
           tag, count = sorted_dict[i]  
           count+=0.0  
           strprint = tag+' '+str(count)  
           encoded_str=strprint.encode('utf-8')  
           print encoded_str  
        
             
   
 if __name__ == '__main__':  
      main()
