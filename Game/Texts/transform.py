from Game.Core import instance

class Transform:
    
    @staticmethod
    def get_transformated_text(text):
    
        code = ""
        start = text.find( "{{" )
        while(start > -1):
            start_text = start + 2 
            end = text.find("}}", start_text)
            if(end > -1):
                code = text[start_text:end] 
                codes = code.split(".")
                val = ""

                if(codes[0] == "BR"):
                    val = "\n\n"
                elif(codes[0] == "Character"):
                    val = Transform.__get_character_transoformation(codes)
                elif(codes[0] == "Items"):
                    val = Transform.__get_items_transoformation(codes)

                text = text.replace("{{" + code + "}}", val)
                start = text.find( "{{" )
            else:
                start = -1

        return text 

    @staticmethod
    def __get_items_transoformation(codes):
        mem = instance.Instance.get_instance() 
        cmd = codes[1]
        if(cmd == "Drop"):
            items = mem.get_drops(mem.get_cur_screen())
            return ', '.join(items)

        return ""

    @staticmethod
    def __get_character_transoformation(codes):
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
                    elif(detail == "Skill"):
                        detail = codes[4]
                        sk = cl.get_skill(detail)
                        if(sk == None):
                            return ""
                        else:
                            return sk.get_value()

        return ""