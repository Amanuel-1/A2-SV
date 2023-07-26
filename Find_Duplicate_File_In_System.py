import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
      file_ = {}
      result =[]
      def getcontent(string):
        content =""
        i= len(string)-2
        while string[i]!="(":
          content+=string[i]
          i-=1
          
            
        return (content,string[:i])
          
          
      for path in paths:
        nodes = path.split(" ")
        dir_ = nodes[0]
        for n in range(1,len(nodes)):
          content,name =getcontent(nodes[n])
          if content in file_:
            file_[content].append(dir_+"/"+name)
          else:
            file_[content] =[dir_+"/"+name]
      for value in file_.values():
        if len(value) >1:
          result.append(value)
      return result

      
