class BooleanFromString:
    def get_boolean(v):
        try:
            if(v == "true" or v == "True"):
                return True
            else:
                return False
        except:
                return False 