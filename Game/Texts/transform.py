class Transform:
    
    @staticmethod
    def get_transformated_text(text):
    
        code = ""

        start = text.index( "{{" )
        if(start > 0):
            start_text = start + 2 
            end = text.index("}}", start_text)
            code = text[start_text:end] 
            codes = code.split(".")
            val = ""

            if(codes[0] == "Character"):
                val = Transform.__get_character_transoformation(codes)

            text = text.replace("{{" + code + "}}", val)

        return text 

    @staticmethod
    def __get_character_transoformation(codes):

        from Game.Core import instance
        mem = instance.Instance.get_instance() 

        ch = mem.get_character(codes[1])
        if(ch == None):
            return "" 
        else:
            detail = codes[2]
            if( detail == "Class"):
                cl = mem.get_class( ch.get_class() )
                if( cl == None ):
                    return ""
                else:
                    detail = codes[3]
                    if(detail == "Name"):
                        return cl.get_name()


        return ""