def dec (f):
    def sub():
        print('here i need to add some step' )
        f()
        print('here is the decorator action ending ')
    return sub
@dec
def greetig():
    print('Hola amigos!!')    

greetig()