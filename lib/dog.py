#!/usr/bin/env python3

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
    def set_name(self,name):
        # 1 to 25
        if(name == ""):
            print("Name must be string between 1 and 25 characters.")
        elif(type(name) is not str):
            print("Name must be string between 1 and 25 characters.")
        elif(len(name) > 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name
            
        # if(len(name) in range(1,26) and type(name) == str):
        #     self._name = name
        # else:
        #     print("Name must be string between 1 and 25 characters.")

    def get_name(self):
        return self._name

    def set_breed(self,breed):
        if(breed not in self.approved_breeds):
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    def get_breed(self):
        return self._breed

    name = property(get_name,set_name,)
    breed = property(get_breed,set_breed,)


