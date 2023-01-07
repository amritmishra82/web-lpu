class Boyfriend:
    a = "If any girl need boyfriend feel free to cantact me on: 9120596609"
Xlass = Boyfriend()
print(Xlass.a)





class Student:
    def __init__(st, name, reg, sec, hostel, place ):
        st.name = name
        st.reg = reg
        st.sec = sec
        st.hostel = hostel
        st.place = place

obj = Student("Amrit Mishra", 12218375, "KOC31", "Boys Hostel-3", "Meeting place- Infront of 26 block")
print(obj.name)
print(obj.reg)
print(obj.sec)
print(obj.hostel)
print(obj.place)

def pr(st):
    print("Hello my name is "+st.name)


obj = Student("Amrit", 12218375)
obj.pr()
