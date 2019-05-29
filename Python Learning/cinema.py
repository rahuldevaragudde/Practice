films={
    "Finding Dory":[3,5],
    "Tarzan":[15,5],
    "Bourne":[18,5],
    "Ghost Busters":[12,5]
    }
while True:
    choice=input("what film do you want?:").strip().title()
    if choice in films:
        age=int(input("how old are you?").strip())
        #check user age
        if age>=films[choice][0]:
            #checking seats
            num_seats=films[choice][1]
            if num_seats >0:
                print("enjoy the film")
                films[choice][1]=films[choice][1]-1
            else:      
                print("sorry we are sold out")
        else:
            print("you are too young to watch the film")
    else:
        print("we dont have that film..")
