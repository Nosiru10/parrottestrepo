class Animmal:
     animal_type = 'mammal'
     counter = 0
   
   
     def __init__(self, name, number_of_ear):
          self.name = name
          self.number_of_ear = number_of_ear
          Animmal.counter += 1

     def can_sence(seif):
         print(f"Animmal {self.name} runs with {self.number_of_ear} ear")

        @classmethod
        def can_see(cls):
            print("Animmal can see!!")

            @staticmethod
            def tail_wiggle():
                print("animmal can wiggle it's tail!")

animal_one = Animmal('bird' 2)
animal_two = Animmal('lion' 4)
animal_three = Animmal('goat', 4)

animal_one.can_sence()
animal_two.can_sence()
animal_three.can_sence()


print("=" * 20) 

  print(animal_one.animal_type)
  print(animal_two.animal_type)

print("=" * 40)

animal_one.can_see()
animal_two.can_see()
animal_three.can_see()

# instance methods, class methods, static methods