import importlib
import sys
import numpy



def get_all_defs(temp):
    list_of_func = []
    for i in temp:
        if(i[0] is not '_'):
            list_of_func.append(i)
    return list_of_func

#-------------------------------------
#MAIN Q1
#-------------------------------------


if __name__ == "__main__":

    """
    In order to write an HTML file from a different model and not from the example,
    you need run in the terminal somting like that:
    "python doc_to_html.py moduleName.py htmlNameToWrite.html"
    """
    
    args=sys.argv
    m_name = ""
    w_name = ""
    if(len(args)<3):
        m_name = "homeworkmodule"
        w_name = "mydoc.html"
    else:
        m_name = args[1]
        m_name = m_name[0:(len(m_name)-3)]
        w_name = args[2]
    hm = importlib.import_module(m_name)

    
    s="<!DOCTYPE html>\n\t<html>\n\t\t<head>\n\t\t\t<title>Moudle</title>\n\t\t</head>\n"
    s+="\t\t<body>\n"
    s+="\t\t\t<h1>"+str(m_name)+"</h1>\n"
    s+="\t\t\t<p>\n"+str(hm.__doc__)+"\n\t\t\t</p>\n"
    s+="\t\t\t<h2>functions:</h2>\n"
    list_of_func = get_all_defs(dir(hm))

    for i in list_of_func:
        s+="\t\t\t<h3>function name"+i+"</h3>\n"  
        def_i = getattr(hm, str(i))   
        s+="\t\t\t<p>input method name "+str(def_i.__annotations__) +"</p>\n"  
        s+="\t\t\t<p>doc:\n "+str(def_i.__doc__) +"\n\t\t\t</p>\n"  
    s+="\t\t</body>\n"
    s+="\t</html>\n"

    f = open(w_name,'w')
    f.write(s)
    f.close()


